# GhostNet-600

---

模型名称： GhostNet-600

骨干网络： GhostNet-600

模块类型：cv-classification

可微调：True

输入形状： [240, 240, 3]

模型版本：1.0

训练数据集：Oxford-IIIT Pet

准确率： 0.869

作者：Noah CVLab

更新时间：2020-9-8

代码仓链接： <https://gitee.com/mindspore/models/tree/master/research/cv/ghostnet>

用户ID：noah-cvlab

用途：推理

训练后端：GPU

推理后端：GPU

MindSpore版本：1.0

MindSpore Lite：True

资源：

- 文件格式：.ckpt  
  资源链接： <https://download.mindspore.cn/model_zoo/research/cv/ghostnet/ghostnet600M_pets.ckpt>  
  资源SHA256校验码：a37ea724eed747ef2f36961e1fdb0deec892643cb2b1d6826ea738539259c139

- 文件格式：.mslite  
  资源链接： <https://download.mindspore.cn/model_zoo/official/lite/ghostnet_lite/ghostnet600.ms>  
  资源SHA256校验码： 6503b41666fd871532cdf558e9a3fe25f1d5dc0236dd116e4738c847a46e813c

许可证：Apache 2.0

摘要：使用GhostNet-600对Oxford-IIIT Pet数据集的37个类进行分类。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的GhostNet实现，目录为model_zoo/research/cv/ghostnet。

## 用法

```python
import mindspore_hub as mshub

from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="GPU",
                    device_id=0)

model = "noah-cvlab/gpu/1.0/ghostnet-600_v1.0_oxford_pets"
network = mshub.load(model, num_classes=37)

network.set_train(False)
```

## Lite推理用法

1. 加载MindSpore Lite模型文件，构建上下文、会话和计算图进行推理。

    - 加载模型文件。创建并配置模型推理上下文。

    ```cpp
    // Buffer是Java层传入的模型数据
    jlong bufferLen = env->GetDirectBufferCapacity(buffer);
    char *modelBuffer = CreateLocalModelBuffer(env, buffer);
    ```

    - 创建会话。

    ```cpp
    void **labelEnv = new void *;
    MSNetWork *labelNet = new MSNetWork;
    *labelEnv = labelNet;

    // 创建上下文
    mindspore::lite::Context *context = new mindspore::lite::Context;
    context->thread_num_ = num_thread;

    // 创建MindSpore会话
    labelNet->CreateSessionMS(modelBuffer, bufferLen, "device label", context);
    delete(context);
    ```

    - 加载模型文件，构建计算图进行推理。

    ```cpp
    void MSNetWork::CreateSessionMS(char* modelBuffer, size_t bufferLen, std::string name, mindspore::lite::Context* ctx)
    {
      CreateSession(modelBuffer, bufferLen, ctx);
      session = mindspore::session::LiteSession::CreateSession(ctx);
      auto model = mindspore::lite::Model::Import(modelBuffer, bufferLen);
      int ret = session->CompileGraph(model);
    }
    ```

2. 将输入的图片转换为MindSpore模型的Tensor格式。

    - 将待检测的图像数据转换为MindSpore模型的Tensor格式。

    ```cpp
    float *width;
    float *height;
    if (!BitmapToLiteMat(env, srcBitmap, &lite_mat_bgr, width, height)) {
      MS_PRINT("BitmapToLiteMat error");
      return NULL;
    }
    if (!PreProcessImageData(lite_mat_bgr, &lite_norm_mat_cut, width, height)) {
      MS_PRINT("PreProcessImageData error");
      return NULL;
    }

    ImgDims inputDims;
    inputDims.channel = lite_norm_mat_cut.channel_;
    inputDims.width = lite_norm_mat_cut.width_;
    inputDims.height = lite_norm_mat_cut.height_;

    // 获取loadModel()中创建的MindSpore推理环境
    void **labelEnv = reinterpret_cast<void **>(netEnv);
    if (labelEnv == nullptr) {
      MS_PRINT("MindSpore error, labelEnv is a nullptr.");
      return NULL;
    }
    MSNetWork *labelNet = static_cast<MSNetWork *>(*labelEnv);

    auto mSession = labelNet->session();
    if (mSession == nullptr) {
      MS_PRINT("MindSpore error, Session is a nullptr.");
      return NULL;
    }
    MS_PRINT("MindSpore get session.");

    auto msInputs = mSession->GetInputs();
    if (msInputs.size() == 0) {
      MS_PRINT("MindSpore error, msInputs.size() equals 0.");
      return NULL;
    }
    auto inTensor = msInputs.front();

    float *dataHWC = reinterpret_cast<float *>(lite_norm_mat_cut.data_ptr_);
    // 拷贝dataHWC到模型输入tensor
    memcpy(inTensor->MutableData(), dataHWC,
           inputDims.channel * inputDims.width * inputDims.height * sizeof(float));
    ```

3. 根据模型对输入tensor进行推理，得到输出tensor，并进行后处理。

    - 进行图执行和端侧推理。

    ```cpp
    // 模型和图片tensor数据加载完成后，运行推理。
    auto status = mSession->RunGraph();
    ```

    - 获取输出数据。

    ```cpp
    auto names = mSession->GetOutputTensorNames();
    std::unordered_map<std::string,mindspore::tensor::MSTensor *> msOutputs;
    for (const auto &name : names) {
      auto temp_dat =mSession->GetOutputByTensorName(name);
      msOutputs.insert(std::pair<std::string, mindspore::tensor::MSTensor *> {name, temp_dat});
    }
    ```

    - 对输出数据进行后处理。

    ```cpp
    // `RET_CATEGORY_SUM`为标签个数，`labels_name_map`为对应名称
    // 给出自己在项目中需要的`RET_CATEGORY_SUM`和`labels_name_map`
    std::string retStr = ProcessRunnetResult(RET_CATEGORY_SUM, labels_name_map, msOutputs);
    ```

4. 图像和输出数据的处理可以参考下面的方法。

    ```cpp
    bool BitmapToLiteMat(JNIEnv *env, const jobject &srcBitmap, LiteMat *lite_mat, float *width, float *height) {
      bool ret = false;
      AndroidBitmapInfo info;
      void *pixels = nullptr;
      LiteMat &lite_mat_bgr = *lite_mat;
      AndroidBitmap_getInfo(env, srcBitmap, &info);
      if (info.format != ANDROID_BITMAP_FORMAT_RGBA_8888) {
        MS_PRINT("Image Err, Request RGBA");
        return false;
      }
      *width = info.width;
      *height = info.height;
      AndroidBitmap_lockPixels(env, srcBitmap, &pixels);
      if (info.stride == info.width*4) {
        ret = InitFromPixel(reinterpret_cast<const unsigned char *>(pixels),
                            LPixelType::RGBA2RGB, LDataType::UINT8, info.width, info.height, lite_mat_bgr);
        if (!ret) {
          MS_PRINT("Init From RGBA error");
        }
      } else {
        unsigned char *pixels_ptr = new unsigned char[info.width * info.height * 4];
        unsigned char *ptr = pixels_ptr;
        unsigned char *data = reinterpret_cast<unsigned char *>(pixels);
        for (int i = 0; i < info.height; i++) {
          memcpy(ptr, data, info.width * 4);
          ptr += info.width * 4;
          data += info.stride;
        }
        ret = InitFromPixel(reinterpret_cast<const unsigned char *>(pixels_ptr),
                            LPixelType::RGBA2RGB, LDataType::UINT8, info.width, info.height, lite_mat_bgr);
        if (!ret) {
          MS_PRINT("Init From RGBA error");
        }
        delete[] (pixels_ptr);
      }
      AndroidBitmap_unlockPixels(env, srcBitmap);
      return ret;
    }

    bool PreProcessImageData(const LiteMat &lite_mat_bgr, LiteMat *lite_norm_mat_ptr, float *width, float *height) {
      bool ret = false;
      LiteMat lite_mat_resize;
      LiteMat &lite_norm_mat = *lite_norm_mat_ptr;
      // 将图像缩长度放至256
      float length = (*width) >= (*height) ? *width : *height;
      ret = ResizeBilinear(lite_mat_bgr, lite_mat_resize, 256 * (*width) / length, 256 * (*height) / length);
      if (!ret) {
        MS_PRINT("ResizeBilinear error");
        return false;
      }
      LiteMat lite_mat_crop;
      // 裁剪图片至224 x 224
      ret = Crop(lite_mat_resize, lite_mat_crop,0, 0, 224, 224);
      if (!ret) {
        MS_PRINT("ResizeBilinear error");
        return false;
      }
      LiteMat lite_mat_convert_float;
      ret = ConvertTo(lite_mat_crop, lite_mat_convert_float, 1.0 / 255.0);
      if (!ret) {
        MS_PRINT("ConvertTo error");
        return false;
      }

      /*
      * 以下均值数据和方差数据仅供参考。
      * 建议您从数据集中进行计算。
      */
      std::vector<float> means = {0.485, 0.456, 0.406};
      std::vector<float> stds = {0.229, 0.224, 0.225};
      SubStractMeanNormalize(lite_mat_convert_float, lite_norm_mat, means, stds);
      return true;
    }

    std::string ProcessRunnetResult(const int RET_CATEGORY_SUM, const char *const labels_name_map[],
                                    std::unordered_map<std::string, mindspore::tensor::MSTensor *> msOutputs) {
      // 获取模型输出分支
      // 使用迭代器获取mAP元素
      std::unordered_map<std::string, mindspore::tensor::MSTensor *>::iterator iter;
      iter = msOutputs.begin();

      // ghostnet_int8.ms模型只输出一个分支。
      auto outputTensor = iter->second;

      int tensorNum = outputTensor->ElementsNum();
      MS_PRINT("Number of tensor elements:%d", tensorNum);

      // 指向第一个得分的指针
      float *scores = static_cast<float *>(outputTensor->MutableData());

      // 输出概率最大的分类，并转换为在APP中显示的文本信息。
      std::string categoryScore = "";
      float max_score = 0;
      int idx = 0;
      for (int i = 0; i < RET_CATEGORY_SUM; ++i) {
        if (scores[i] > max_score) {
          max_score = scores[i];
          idx = i;
        }
        categoryScore += labels_name_map[i];
        categoryScore += ":";
        std::string score_str = std::to_string(scores[idx]);
        categoryScore += score_str;
        categoryScore += ";";
      return categoryScore;
    }
    ```

## 参考论文

1. Kai Han, Yunhe Wang, Qi Tian, Jianyuan Guo, Chunjing Xu, Chang Xu; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2020, pp. 1580-1589
