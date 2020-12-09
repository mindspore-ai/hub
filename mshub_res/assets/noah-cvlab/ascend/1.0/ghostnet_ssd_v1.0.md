# GhostNet-SSD

---

model-name: GhostNet_SSD

backbone-name: ghostnet1.3x

module-type: cv-object_detection

fine-tunable: True

input-shape: [3, 300, 300]

model-version: 1.0

mAP: 0.241

author: Noah CVLab

update-time: 2020-09-08

repo-link: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/research/cv/ssd_ghostnet>

user-id: noah-cvlab

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

mindspore-lite: true

asset:

- file-format: mslite
  asset-link: <https://download.mindspore.cn/model_zoo/official/lite/ssd_ghostnet_lite/ssd.ms>
  asset-sha256: f7663907e1006fe1458d702c05177ff3107c4b4ee94d4bfbc3d753e359443660

license: Apache2.0

summary: ssd_ghostnet is ssd model with ghostnet backbone

---

## Introduction

This MindSpore Hub model uses the implementation of ssd_ghostnet from the MindSpore model zoo on Gitee at model_zoo/official/cv/ssd_ghostnet.

All Parameters in the module are trainable.

## Usage

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
    std::string retStr = ProcessRunnetResult(msOutputs, srcImageWidth, srcImageHeight);
    ```

4. The process of image and output data can refer to methods showing bellow.

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

      // Using ssd model util to process model branch outputs.
      SSDModelUtil ssdUtil(srcImageWidth, srcImageHeight);

      std::string retStr = ssdUtil.getDecodeResult(tmpscores2, tmpdata);
      MS_PRINT("retStr %s", retStr.c_str());

      return retStr;
    }
    ```

## Citation

1. [Paper](https://arxiv.org/abs/1512.02325):   Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott Reed, Cheng-Yang Fu, Alexander C. Berg.European Conference on Computer Vision (ECCV), 2016 (In press).
2. [Paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Han_GhostNet_More_Features_From_Cheap_Operations_CVPR_2020_paper.html):   Kai Han, Yunhe Wang, Qi Tian, Jianyuan Guo, Chunjing Xu, Chang Xu.Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2020, pp. 1580-1589.
