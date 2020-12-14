# MobileNetV2

---

model-name: mobilenetV2

backbone-name: mobilenetV2

module-type: cv-scene_detection

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.0

author: MindSpore team

update-time: 2020-09-10

repo-link: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/mobilenetv2>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

mindspore-lite: true

asset:

- file-format: mslite
  asset-link: <https://download.mindspore.cn/model_zoo/official/lite/mobilenetv2_scene_detection_lite/mobilenetv2.ms>
  asset-sha256: 0bf5fc563c18044a67ad467f401e8c036cb381e20ab9631e0ad9c49b1a9c6a7c

license: Apache2.0

summary: mobilenetv2 trained to be used for scene detection

---

## Introduction

This MindSpore Hub model uses the implementation of MobileNetV2 from the MindSpore model zoo on Gitee at model_zoo/official/cv/mobilenetv2.

This model has been trained to be used for scene detection.

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

model = "mindspore/ascend/1.0/mobilenetv2_v1.0"

network = mshub.load(model, num_classes=365, include_top=True, activation="Sigmoid")
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
    void MSNetWork::CreateSessionMS(char* modelBuffer, size_t bufferLen, std::string name,    mindspore::lite::Context* ctx)
    {
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
    int srcImageWidth = lite_mat_bgr.width_;
    int srdImageHeight = lite_mat_bgr.height;
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
    ```

    - Perform post-processing of the output data.

    ```cpp
    // `RET_CATEGORY_SUM` is the number of labels, and `labels_name_map` is the name correspondingly.
    // Give your own `RET_CATEGORY_SUM` and `labels_name_map` needed in the project.
    std::string retStr = ProcessRunnetResult(RET_CATEGORY_SUM, labels_name_map, msOutputs);
    ```

4. The process of image and output data can refer to methods showing bellow.

    ```cpp

    bool PreProcessImageData(const LiteMat &lite_mat_bgr, LiteMat *lite_norm_mat_ptr) {
    bool ret = false;
    LiteMat lite_mat_resize;
    LiteMat &lite_norm_mat_cut = *lite_norm_mat_ptr;
    ret = ResizeBilinear(lite_mat_bgr, lite_mat_resize, 256, 256);
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
    LiteMat lite_mat_cut;
    ret = Crop(lite_mat_convert_float, lite_mat_cut, 16, 16, 224, 224);
    if (!ret) {
      MS_PRINT("Crop error");
      return false;
    }
    std::vector<float> means = {0.485, 0.456, 0.406};
    std::vector<float> stds = {0.229, 0.224, 0.225};
    SubStractMeanNormalize(lite_mat_cut, lite_norm_mat_cut, means, stds);
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

      // Using ssd model util to process model branch outputs.
      SSDModelUtil ssdUtil(srcImageWidth, srcImageHeight);

      std::string retStr = ssdUtil.getDecodeResult(tmpscores2, tmpdata);
      MS_PRINT("retStr %s", retStr.c_str());

      return retStr;
    }

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

    // float scores[RET_CATEGORY_SUM];
    float scores = temp_scores[0];
    int cat_loc = 0;
    for (int i = 0; i < RET_CATEGORY_SUM; ++i) {
      if (scores < temp_scores[i]) {
        scores = temp_scores[i];
        cat_loc = i;
      }
      if (temp_scores[i] > 0.5) {
        MS_PRINT("MindSpore scores[%d] : [%f]", i, temp_scores[i]);
      }
    }

    // Score for each category.
    // Converted to text information that needs to be displayed in the APP.
    std::string categoryScore = "";
    categoryScore += labels_name_map[cat_loc];
    categoryScore += ":";
    std::string score_str = std::to_string(scores);
    categoryScore += score_str;
    return categoryScore;
    }
    ```

## Citation

1. Howard, Andrew, Mark Sandler, Grace Chu, Liang-Chieh Chen, Bo Chen, Mingxing Tan, Weijun Wang et al. "Searching for MobileNetV2." In Proceedings of the IEEE International Conference on Computer Vision, pp. 1314-1324. 2019.
