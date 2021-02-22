# MobileNetV2

---

模型名称：MobileNetV2

骨干网络：MobileNetV2

模块类型：cv-classification

可微调：True

输入形状： [224, 224, 3]

模型版本：1.0

作者：MindSpore团队

更新时间：2020-9-10

代码仓链接： <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/mobilenetv2>

用户ID：MindSpore

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：1.0

MindSpore Lite：True

资源：

- 文件格式：.mslite  
  资源链接： <https://download.mindspore.cn/model_zoo/official/lite/mobilenetv2_scene_detection_lite/mobilenetv2.ms>  
  资源SHA256校验码： 0bf5fc563c18044a67ad467f401e8c036cb381e20ab9631e0ad9c49b1a9c6a7c

许可证：Apache 2.0

摘要：训练MobileNetV2进行场景检测。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的MobileNetV2实现，目录为model_zoo/official/cv/mobilenetv2。

该训练模型适用于场景检测。

模块中所有参数均可训练。

## 用法

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

      //使用SSD模型工具处理模型分支输出
      SSDModelUtil ssdUtil(srcImageWidth, srcImageHeight);

      std::string retStr = ssdUtil.getDecodeResult(tmpscores2, tmpdata);
      MS_PRINT("retStr %s", retStr.c_str());

      return retStr;
    }

    std::string ProcessRunnetResult(const int RET_CATEGORY_SUM, const char *const labels_name_map[],
                                std::unordered_map<std::string, mindspore::tensor::MSTensor *> msOutputs) {
    // 获取模型输出分支
    // 使用迭代器获取mAP元素
    std::unordered_map<std::string, mindspore::tensor::MSTensor *>::iterator iter;
    iter = msOutputs.begin();

    // mobilenetv2.ms模型只输出一个分支
    auto outputTensor = iter->second;

    int tensorNum = outputTensor->ElementsNum();
    MS_PRINT("Number of tensor elements:%d", tensorNum);

    // 指向第一个得分的指针
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

    // 分类得分
    // 转换为APP显示的文本信息
    std::string categoryScore = "";
    categoryScore += labels_name_map[cat_loc];
    categoryScore += ":";
    std::string score_str = std::to_string(scores);
    categoryScore += score_str;
    return categoryScore;
    }
    ```

## 参考论文

1. Howard, Andrew, Mark Sandler, Grace Chu, Liang-Chieh Chen, Bo Chen, Mingxing Tan, Weijun Wang et al. "Searching for MobileNetV2." In Proceedings of the IEEE International Conference on Computer Vision, pp. 1314-1324. 2019.
