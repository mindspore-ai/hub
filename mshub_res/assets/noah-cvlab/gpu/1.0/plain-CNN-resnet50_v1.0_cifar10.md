# ResNet50 Resiudal Distillation

---

model-name: plain-CNN-resnet50

backbone-name: resnet50

module-type: cv-classification

fine-tunable: False

input-shape: [32, 32, 3]

model-version: 1.0

train-dataset: cifar10

accuracy: 0.9446

author: Noah CVLab

update-time: 2020-11-17

repo-link:

user-id: noah-cvlab

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-lite: true

mindspore-version: 1.0

asset:

- file-format: mslite
  asset-link: <https://download.mindspore.cn/model_zoo/official/lite/residual_distill_lite/residual_distill_res50_cifar10_bs_1_update.ms>
  asset-sha256: 449498ecf5201d46d4eaee2754d69db89b656573f4e74ab42a9f8597299bb63b

license: Apache2.0

summary: ResNet50-plain derived by resiudal distillation method, and is used to classify 10 classes of CIFAR-10

---

## Introduction

This MindSpore Hub model uses the implementation of Residual Distillation on ResNet50.

## Lite Inference Usage

1. Load the MindSpore Lite model file and build the context, session, and computational graph for inference.

    - Load a model file. Create and configure the context for model inference.

    ```cpp
    // Buffer is the model data passed in by the Java layer
    jlong bufferLen = env->GetDirectBufferCapacity(buffer);
    char *modelBuffer = CreateLocalModelBuffer(env, buffer);
    ```

    - Create a session.

    ```cpp
    void **labelEnv = new void *;
    MSNetWork *labelNet = new MSNetWork;
    *labelEnv = labelNet;

    // Create context.
    mindspore::lite::Context *context = new mindspore::lite::Context;
    context->thread_num_ = num_thread;

    // Create the mindspore session.
    labelNet->CreateSessionMS(modelBuffer, bufferLen, "device label", context);
    delete(context);
    ```

    - Load the model file and build a computational graph for inference.

    ```cpp
    void MSNetWork::CreateSessionMS(char* modelBuffer, size_t bufferLen, std::string name,
                                    mindspore::lite::Context* ctx) {
       CreateSession(modelBuffer, bufferLen, ctx);
       session = mindspore::session::LiteSession::CreateSession(ctx);
       auto model = mindspore::lite::Model::Import(modelBuffer, bufferLen);
       int ret = session->CompileGraph(model);
     }
     ```

2. Convert the input image into the Tensor format of the MindSpore model.

    - Convert the image data to be detected into the Tensor format of the MindSpore model.

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

    // Get the mindsore inference environment which created in loadModel().
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
    // Copy dataHWC to the model input tensor.
    memcpy(inTensor->MutableData(), dataHWC,
           inputDims.channel * inputDims.width * inputDims.height * sizeof(float));
    ```

3. Perform inference on the input tensor based on the model, obtain the output tensor, and perform post-processing.

    - Perform graph execution and on-device inference.

    ```cpp
    // After the model and image tensor data is loaded, run inference.
    auto status = mSession->RunGraph();
    ```

    - Obtain the output data.

    ```cpp
    // The model only has one output.
    auto output = mSession->GetOutputs().front();
    ```

    - Perform post-processing of the output data.

    ```cpp
    // RET_CATEGORY_SUM is the number of labels, and labels_name_map is all the labels.
    std::string retStr = ProcessRunnetResult(RET_CATEGORY_SUM, labels_name_map, output);
    ```

4. The process of image and output data can refer to methods showing bellow.

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
      * The mean data and variance data shown below is just for reference.
      * You are encouraged to caculate it from the dataset.
      */
      std::vector<float> means = {0.491, 0.482, 0.447};
      std::vector<float> stds = {0.247, 0.243, 0.262};
      SubStractMeanNormalize(lite_mat_convert_float, lite_norm_mat, means, stds);
      return true;
    }

    std::string ProcessRunnetResult(const int RET_CATEGORY_SUM, const char *const labels_name_map[], mindspore::tensor::MSTensor outputTensor) {
      // Get the branch of the model output.
      int tensorNum = outputTensor->ElementsNum();
      MS_PRINT("Number of tensor elements:%d", tensorNum);

      // Get a pointer to the first score.
      float *scores = static_cast<float *>(outputTensor->MutableData());

      // Output the category with the highest probability and convert to text information that needs to be displayed in the APP.
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

## Citation

1. Guilin Li, Junlei Zhang, Yunhe Wang, Chuanjian Liu, Matthias Tan, Yunfeng Lin, Wei Zhang, Jiashi Feng, Tong Zhang. Residual Distillation: Towards Portable Deep Neural Networks without Shortcuts. Accepted by NeurIPS 2020.
