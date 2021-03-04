# MobileNetV2

---

model-name: mobilenetV2

backbone-name: mobilenetV2

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.0

train-dataset: openimage

f1: 0.55

author: MindSpore team

update-time: 2020-09-10

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/cv/mobilenetv2>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

mindspore-lite: true

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/official/lite/mobilenetv2_openimage_lite/1.1/mobilenetv2_ascend.ckpt>  
    asset-sha256: 808636dd9da7a34ad70296fb4be023ee024d27bbba51b637b80ea2a979e5e12c  

-
    file-format: mindir  
    asset-link: <https://download.mindspore.cn/model_zoo/official/lite/mobilenetv2_openimage_lite/mobilenetv2.mindir>  
    asset-sha256: aba47ddc769ffac130bcea855e9b3553e15e4ed83c716314fa15f546ebac9d45  

-
    file-format: mslite  
    asset-link: <https://download.mindspore.cn/model_zoo/official/lite/mobilenetv2_openimage_lite/mobilenetv2.ms>  
    asset-sha256: 1158a5eadfa6bb729500f7de89c33b1e264f4514a70780055afa1355541b5766  

license: Apache2.0

summary: mobilenetv2 used to classify 600 classes of openimage.

---

## Introduction

This MindSpore Hub model uses the implementation of MobileNetV2 from the MindSpore model zoo on Gitee at model_zoo/official/cv/mobilenetv2.

This model has been trained on openimage, and we use 600 class from [class table](https://storage.googleapis.com/openimages/v5/class-descriptions-boxable.csv).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms
from PIL import Image
import cv2

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.0/mobilenetv2_v1.0_openimage"

network = mshub.load(model, num_classes=500, include_top=True, activation="Sigmoid")
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
     void MSNetWork::CreateSessionMS(char* modelBuffer, size_t bufferLen, std::string name, mindspore::lite::Context* ctx)
     {
         CreateSession(modelBuffer, bufferLen, ctx);
         session = mindspore::session::LiteSession::CreateSession(ctx);
         auto model = mindspore::lite::Model::Import(modelBuffer, bufferLen);
         int ret = session->CompileGraph(model);
     }
     ```

2. Convert the input image into the Tensor format of the MindSpore model.

   Convert the image data to be detected into the Tensor format of the MindSpore model.

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
     auto names = mSession->GetOutputTensorNames();
     std::unordered_map<std::string,mindspore::tensor::MSTensor *> msOutputs;
     for (const auto &name : names) {
         auto temp_dat =mSession->GetOutputByTensorName(name);
         msOutputs.insert(std::pair<std::string, mindspore::tensor::MSTensor *> {name, temp_dat});
       }
     std::string retStr = ProcessRunnetResult(msOutputs, ret);
     ```

   - Perform post-processing of the output data.

     ```cpp
     std::string ProcessRunnetResult(const int RET_CATEGORY_SUM, const char *const labels_name_map[],
              std::unordered_map<std::string, mindspore::tensor::MSTensor *> msOutputs) {
      // Get the branch of the model output.
      // Use iterators to get map elements.
      std::unordered_map<std::string, mindspore::tensor::MSTensor *>::iterator iter;
      iter = msOutputs.begin();

      // The mobilenetv2.ms model output just one branch.
      auto outputTensor = iter->second;

      int tensorNum = outputTensor->ElementsNum();
      MS_PRINT("Number of tensor elements:%d", tensorNum);

      // Get a pointer to the first score.
      float *temp_scores = static_cast<float *>(outputTensor->MutableData());
      // RescaleProbs(temp_scores);
      float scores[RET_CATEGORY_SUM];
      for (int i = 0; i < RET_CATEGORY_SUM; ++i) {
       scores[i] = temp_scores[i];
      }

      float unifiedThre = 0.5;
      float probMax = 1.0;
      for (size_t i = 0; i < RET_CATEGORY_SUM; ++i) {
       float threshold = g_thres_map[i];
       float tmpProb = scores[i];
       if (tmpProb < threshold) {
        tmpProb = tmpProb / threshold * unifiedThre;
       } else {
        tmpProb = (tmpProb - threshold) / (probMax - threshold) * unifiedThre + unifiedThre;
      }
       scores[i] = tmpProb;
     }

      for (int i = 0; i < RET_CATEGORY_SUM; ++i) {
      if (scores[i] > 0.5) {
          MS_PRINT("MindSpore scores[%d] : [%f]", i, scores[i]);
       }
      }

      // Score for each category.
      // Converted to text information that needs to be displayed in the APP.
      std::string categoryScore = "";
      for (int i = 0; i < RET_CATEGORY_SUM; ++i) {
       categoryScore += labels_name_map[i];
       categoryScore += ":";
       std::string score_str = std::to_string(scores[i]);
       categoryScore += score_str;
       categoryScore += ";";
      }
        return categoryScore;
     }

     ```

## Citation

1. Howard, Andrew, Mark Sandler, Grace Chu, Liang-Chieh Chen, Bo Chen, Mingxing Tan, Weijun Wang et al. "Searching for MobileNetV2." In Proceedings of the IEEE International Conference on Computer Vision, pp. 1314-1324. 2019.
