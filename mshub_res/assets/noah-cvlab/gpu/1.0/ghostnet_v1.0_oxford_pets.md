# GhostNet

---

model-name: GhostNet

backbone-name: GhostNet

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.0

train-dataset: Oxford-IIIT Pet

accuracy: 0.824

author: Noah's Ark Lab

update-time: 2020-09-08

repo-link: <https://gitee.com/mindspore/models/tree/master/research/cv/ghostnet>

user-id: noah-cvlab

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-version: 1.0

mindspore-lite: true

asset:

- file-format: ckpt  
  asset-link: <https://download.mindspore.cn/model_zoo/research/cv/ghostnet/ghostnet_1x_pets.ckpt>  
  asset-sha256: 722e13be6cd6186dddcd68d5c0a50776d9a8ad8e79db3870556f68d4d2f179e4  
- file-format: mslite  
  asset-link: <https://download.mindspore.cn/model_zoo/official/lite/ghostnet_lite/ghostnet.ms>  
  asset-sha256: 1cff3c6586fa840eab0223634df8ade44226ae8b3245052b90e1437c68bf1380  

license: Apache2.0

summary: GhostNet classifies 37 classes of Oxford-IIIT Pet

---

## Introduction

This MindSpore Hub model uses the implementation of
GhostNet from the MindSpore model zoo on Gitee at
model_zoo/official/cv/ghostnet. The GhostNet architecture is based on
Ghost module structure which generate more features from cheap operations.
Base on a set of intrinsic features. Experiments conducted on benchmarks
demonstrate the superiority of GhostNet in terms of speed and accuracy.

### Performance

#### GhostNet on ImageNet2012

| Parameters                 |                                        |   |
| -------------------------- | -------------------------------------- |---------------------------------- |
| Model Version              | GhostNet                                             |GhostNet-600|
| Uploaded Date              | 09/08/2020 (month/day/year)                          | 09/08/2020 (month/day/year) |
| Dataset                    | ImageNet2012                                                    | ImageNet2012|
| Parameters (M)             | 5.2                                                   | 11.9 |
| FLOPs (M) | 142 | 591 |
| Accuracy (Top1) | 73.9 |80.2   |
![flops_latency](https://gitee.com/mindspore/hub/raw/master/mshub_res/assets/noah-cvlab/static/images/ghostnet_static_img.png)

#### GhostNet on Oxford-IIIT Pet

| Parameters                 |                                        |   |
| -------------------------- | -------------------------------------- |---------------------------------- |
| Model Version              | GhostNet                                             |GhostNet-600|
| Uploaded Date              | 09/08/2020 (month/day/year)                         | 09/08/2020 (month/day/year) |
| Dataset                    | Oxford-IIIT Pet                                                   | Oxford-IIIT Pet|
| Parameters (M)             | 3.9                                                    | 10.6 |
| FLOPs (M) | 140 | 590 |
| Accuracy (Top1) |            82.4              |86.9   |

#### Comparison with other methods on Oxford-IIIT Pet

| Model           | FLOPs (M) | Latency (ms)* | Accuracy (Top1) |
| --------------- | --------- | ------------- | --------------- |
| MobileNetV2-1x  | 300       | 28.2          | 78.5            |
| Ghost-1x w\o SE | 138       | 19.1          | 81.1            |
| Ghost-1x        | 140       | 25.3          | 82.4            |
| Ghost-600       | 590       | -             | 86.9            |

*The latency is measured on Huawei Kirin 990 chip under single-threaded mode with batch size 1.

## Usage

```python
import mindspore_hub as mshub

from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="GPU",
                    device_id=0)

model = "noah-cvlab/gpu/1.0/ghostnet_v1.0_oxford_pets"
network = mshub.load(model, num_classes=37)

network.set_train(False)
```

## Lite Inference  Usage

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
    auto names = mSession->GetOutputTensorNames();
    std::unordered_map<std::string,mindspore::tensor::MSTensor *> msOutputs;
    for (const auto &name : names) {
      auto temp_dat =mSession->GetOutputByTensorName(name);
      msOutputs.insert(std::pair<std::string, mindspore::tensor::MSTensor *> {name, temp_dat});
    }
    ```

    - Perform post-processing of the output data.

    ```cpp
    // `RET_CATEGORY_SUM` is the number of labels, and `labels_name_map` is the name correspondingly.
    // Give your own `RET_CATEGORY_SUM` and `labels_name_map` needed in the project.
    std::string retStr = ProcessRunnetResult(RET_CATEGORY_SUM, labels_name_map, msOutputs);
    ```

4. The process of image and output data can refer to methods showing below.

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
      // scale the image to hava a length of 256.
      float length = (*width) >= (*height) ? *width : *height;
      ret = ResizeBilinear(lite_mat_bgr, lite_mat_resize, 256 * (*width) / length, 256 * (*height) / length);
      if (!ret) {
        MS_PRINT("ResizeBilinear error");
        return false;
      }
      LiteMat lite_mat_crop;
      // crop the image to 224 * 224.
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
      * The mean data and variance data shown below is just for reference.
      * You are encouraged to calculate it from the dataset.
      */
      std::vector<float> means = {0.485, 0.456, 0.406};
      std::vector<float> stds = {0.229, 0.224, 0.225};
      SubStractMeanNormalize(lite_mat_convert_float, lite_norm_mat, means, stds);
      return true;
    }

    std::string ProcessRunnetResult(const int RET_CATEGORY_SUM, const char *const labels_name_map[],
                                    std::unordered_map<std::string, mindspore::tensor::MSTensor *> msOutputs) {
      // Get the branch of the model output.
      // Use iterators to get map elements.
      std::unordered_map<std::string, mindspore::tensor::MSTensor *>::iterator iter;
      iter = msOutputs.begin();

      // The ghostnet_int8.ms model output just one branch.
      auto outputTensor = iter->second;

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

1. Kai Han, Yunhe Wang, Qi Tian, Jianyuan Guo, Chunjing Xu, Chang Xu; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2020, pp. 1580-1589
