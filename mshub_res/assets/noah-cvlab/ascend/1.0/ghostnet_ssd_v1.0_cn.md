# GhostNet-SSD

---

模型名称：GhostNet_SSD

骨干网络：GhostNet1.3x

模块类型：cv-object_detection

可微调：True

输入形状： [3, 300, 300]

模型版本：1.0

mAP：0.241

作者：Noah CVLab

更新时间：2020-9-8

代码仓链接： <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/research/cv/ssd_ghostnet>

用户ID：noah-cvlab

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：1.0

MindSpore Lite：True

资源：

- 文件格式：.mslite  
  资源链接： <https://download.mindspore.cn/model_zoo/official/lite/ssd_ghostnet_lite/ssd.ms>  
  资源SHA256校验码：f7663907e1006fe1458d702c05177ff3107c4b4ee94d4bfbc3d753e359443660

许可证：Apache 2.0

摘要：ssd_ghostnet是主干为GhostNet的SSD模型。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的ssd_ghostnet实现，目录为model_zoo/official/cv/ssd_ghostnet。

模块中所有参数均可训练。

## 用法

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "noah-cvlab/ascend/1.0/ghostnet_ssd_v1.0"
network = mshub.load(model)
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
    void MSNetWork::CreateSessionMS(char* modelBuffer, size_t bufferLen, std::string name,    mindspore::lite::Context* ctx)
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
    if (!ObjectBitmapToLiteMat(env, srcBitmap, &lite_mat_bgr)) {
      MS_PRINT("ObjectBitmapToLiteMat error");
      return NULL;
    }
    int srcImageWidth = lite_mat_bgr.width_;
    int srdImageHeight = lite_mat_bgr.height;
    if (!ObjectPreProcessImageData(lite_mat_bgr, &lite_norm_mat_cut)) {
      MS_PRINT("ObjectPreProcessImageData error");
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
    std::string retStr = ProcessRunnetResult(msOutputs, srcImageWidth, srcImageHeight);
    ```

4. 图像和输出数据的处理可以参考下面的方法。

    ```cpp

    bool ObjectBitmapToLiteMat(JNIEnv *env, const jobject &srcBitmap, LiteMat *lite_mat) {
      bool ret = false;
      AndroidBitmapInfo info;
      void *pixels = nullptr;
      LiteMat &lite_mat_bgr = *lite_mat;
      AndroidBitmap_getInfo(env, srcBitmap, &info);
      if (info.format != ANDROID_BITMAP_FORMAT_RGBA_8888) {
        MS_PRINT("Image Err, Request RGBA");
        return false;
      }
      AndroidBitmap_lockPixels(env, srcBitmap, &pixels);
      if (info.stride == info.width * 4) {
        ret = InitFromPixel(reinterpret_cast<const unsigned char *>(pixels),
                            LPixelType::RGBA2RGB, LDataType::UINT8,
                            info.width, info.height, lite_mat_bgr);
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
                            LPixelType::RGBA2RGB, LDataType::UINT8,
                            info.width, info.height, lite_mat_bgr);
        if (!ret) {
          MS_PRINT("Init From RGBA error");
        }
        delete[] (pixels_ptr);
      }
      AndroidBitmap_unlockPixels(env, srcBitmap);
      return ret;
    }

    bool ObjectPreProcessImageData(const LiteMat &lite_mat_bgr, LiteMat *lite_norm_mat_ptr) {
      bool ret = false;
      LiteMat lite_mat_resize;
      LiteMat &lite_norm_mat_cut = *lite_norm_mat_ptr;
      ret = ResizeBilinear(lite_mat_bgr, lite_mat_resize, 300, 300);
      if (!ret) {
        MS_PRINT("ResizeBilinear error");
        return false;
      }
      LiteMat lite_mat_convert_float;
      ret = ConvertTo(lite_mat_resize, lite_mat_convert_float, 1.0 / 255.0);
      if (!ret) {
        MS_PRINT("ConvertTo error");
        return false;
      }

      std::vector<float> means = {0.485, 0.456, 0.406};
      std::vector<float> stds = {0.229, 0.224, 0.225};
      SubStractMeanNormalize(lite_mat_convert_float, lite_norm_mat_cut, means, stds);
      return true;
    }

    std::string ProcessRunnetResult(std::unordered_map<std::string, mindspore::tensor::MSTensor *> msOutputs,
                                    int srcImageWidth, int srcImageHeight) {
      std::unordered_map<std::string, mindspore::tensor::MSTensor *>::iterator iter;
      iter = msOutputs.begin();
      auto branch2_string = iter->first;
      auto branch2_tensor = iter->second;

      ++iter;
      auto branch1_string = iter->first;
      auto branch1_tensor = iter->second;
      MS_PRINT("%s %s", branch1_string.c_str(), branch2_string.c_str());

      float *tmpscores2 = reinterpret_cast<float *>(branch1_tensor->MutableData());
      float *tmpdata = reinterpret_cast<float *>(branch2_tensor->MutableData());

      //使用SSD模型工具处理模型分支输出
      SSDModelUtil ssdUtil(srcImageWidth, srcImageHeight);

      std::string retStr = ssdUtil.getDecodeResult(tmpscores2, tmpdata);
      MS_PRINT("retStr %s", retStr.c_str());

      return retStr;
    }
    ```

## 参考论文

1. [论文](https://arxiv.org/abs/1512.02325)：   Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott Reed, Cheng-Yang Fu, Alexander C. Berg.European Conference on Computer Vision (ECCV), 2016 (In press).
2. [论文](https://openaccess.thecvf.com/content_CVPR_2020/html/Han_GhostNet_More_Features_From_Cheap_Operations_CVPR_2020_paper.html)：   Kai Han, Yunhe Wang, Qi Tian, Jianyuan Guo, Chunjing Xu, Chang Xu.Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2020, pp. 1580-1589.
