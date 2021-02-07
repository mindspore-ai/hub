# ResNet-18残差蒸馏

---

模型名称：plain-CNN-resnet18

骨干网络：ResNet-18

模块类型：cv-classification

可微调： False

输入形状： [32, 32, 3]

模型版本：1.0

训练数据集：CIFAR-10

准确率： 0.9536

作者：Noah CVLab

更新时间：2020-11-17

代码仓链接：

用户ID：noah-cvlab

用途：推理

训练后端：GPU

推理后端：GPU

MindSpore Lite：True

MindSpore版本：1.0

资源：

- 文件格式：.mslite  
  资源链接： <https://download.mindspore.cn/model_zoo/official/lite/residual_distill_lite/residual_distill_res18_cifar10_bs_1_update.ms>  
  资源SHA256校验码： 95fd81a9ea5e1a8c5a3020a4b4a14e480571283de27d4ca5943556edf4d0692e

许可证：Apache 2.0

摘要：使用残差蒸馏法推导出的ResNet18-plain对CIFAR-10的10个类进行分类。

---

## 简介

该MindSpore Hub模型使用ResNet18残差蒸馏实现。

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
    void MSNetWork::CreateSessionMS(char* modelBuffer, size_t bufferLen, std::string name,
                                    mindspore::lite::Context* ctx) {
       CreateSession(modelBuffer, bufferLen, ctx);
       session = mindspore::session::LiteSession::CreateSession(ctx);
       auto model = mindspore::lite::Model::Import(modelBuffer, bufferLen);
       int ret = session->CompileGraph(model);
     }
     ```

2. 将输入的图片转换为MindSpore模型的Tensor格式。

    - 将待检测的图像数据转换为MindSpore模型的Tensor格式。

    ```cpp
    if (!BitmapToLiteMat(env, srcBitmap, &lite_mat_bgr)) {
      MS_PRINT("BitmapToLiteMat error");
      return NULL;
    }
    if (!PreProcessImageData(lite_mat_bgr, &lite_norm_mat_cut)) {
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
    // 模型只有一个输出
    auto output = mSession->GetOutputs().front();
    ```

    - 对输出数据进行后处理。

    ```cpp
    // RET_CATEGORY_SUM为标签个数，labels_name_map为所有标签。
    std::string retStr = ProcessRunnetResult(RET_CATEGORY_SUM, labels_name_map, output);
    ```

4. 图像和输出数据的处理可以参考下面的方法。

    ```cpp
    bool BitmapToLiteMat(JNIEnv *env, const jobject &srcBitmap, LiteMat *lite_mat) {
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

    bool PreProcessImageData(const LiteMat &lite_mat_bgr, LiteMat *lite_norm_mat_ptr) {
      bool ret = false;
      LiteMat lite_mat_resize;
      LiteMat &lite_norm_mat = *lite_norm_mat_ptr;
      ret = ResizeBilinear(lite_mat_bgr, lite_mat_resize, 32, 32);
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

      /*
      * 以下均值数据和方差数据仅供参考。
      * 建议您从数据集中进行计算。
      */
      std::vector<float> means = {0.491, 0.482, 0.447};
      std::vector<float> stds = {0.247, 0.243, 0.262};
      SubStractMeanNormalize(lite_mat_convert_float, lite_norm_mat, means, stds);
      return true;
    }

    std::string ProcessRunnetResult(const int RET_CATEGORY_SUM, const char *const labels_name_map[], mindspore::tensor::MSTensor outputTensor) {
      // 获取模型输出分支
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

1. Guilin Li, Junlei Zhang, Yunhe Wang, Chuanjian Liu, Matthias Tan, Yunfeng Lin, Wei Zhang, Jiashi Feng, Tong Zhang. Residual Distillation: Towards Portable Deep Neural Networks without Shortcuts. Accepted by NeurIPS 2020.
