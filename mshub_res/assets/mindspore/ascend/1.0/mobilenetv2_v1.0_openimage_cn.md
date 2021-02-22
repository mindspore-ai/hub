# MobileNetV2

---

模型名称：MobileNetV2

骨干网络：MobileNetV2

模块类型：cv-classification

可微调：True

输入形状： [224, 224, 3]

模型版本：1.0

训练数据集：openimage

f1: 0.55

作者：MindSpore团队

更新时间：2020-9-10

代码仓链接：<https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/mobilenetv2>

用户ID：MindSpore

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：1.0

MindSpore Lite：True

资源：

-
    文件格式：.ckpt  
    资源链接：<https://download.mindspore.cn/model_zoo/official/lite/mobilenetv2_openimage_lite/mobilenetv2_ascend.ckpt>  
    资源SHA256校验码： 0ce485e2ed61602d8bf15332db9801f114e820c142744b18f02491879421ecb3

-
    文件格式：.mindir  
    资源链接：<https://download.mindspore.cn/model_zoo/official/lite/mobilenetv2_openimage_lite/mobilenetv2.mindir>  
    资源SHA256校验码：aba47ddc769ffac130bcea855e9b3553e15e4ed83c716314fa15f546ebac9d45

-
    文件格式：.mslite  
    资源链接：<https://download.mindspore.cn/model_zoo/official/lite/mobilenetv2_openimage_lite/mobilenetv2.ms>  
    资源SHA256校验码： 1158a5eadfa6bb729500f7de89c33b1e264f4514a70780055afa1355541b5766

许可证：Apache 2.0

摘要：使用MobileNetV2对openimage的600个类进行分类。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的MobileNetV2实现，目录为model_zoo/official/cv/mobilenetv2。

使用[class table](https://storage.googleapis.com/openimages/v5/class-descriptions-boxable.csv)中的600类在openimage数据集上训练该模型。

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

model = "mindspore/ascend/1.0/mobilenetv2_v1.0_openimage"

network = mshub.load(model, num_classes=601, include_top=True, activation="Sigmoid")
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

   将待检测的图像数据转换为MindSpore模型的Tensor格式。

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
     auto names = mSession->GetOutputTensorNames();
     std::unordered_map<std::string,mindspore::tensor::MSTensor *> msOutputs;
     for (const auto &name : names) {
         auto temp_dat =mSession->GetOutputByTensorName(name);
         msOutputs.insert(std::pair<std::string, mindspore::tensor::MSTensor *> {name, temp_dat});
       }
     std::string retStr = ProcessRunnetResult(msOutputs, ret);
     ```

   - 对输出数据进行后处理。

     ```cpp
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

      // 分类得分
      // 转换为APP显示的文本信息
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

## 参考论文

1. Howard, Andrew, Mark Sandler, Grace Chu, Liang-Chieh Chen, Bo Chen, Mingxing Tan, Weijun Wang et al. "Searching for MobileNetV2." In Proceedings of the IEEE International Conference on Computer Vision, pp. 1314-1324. 2019.
