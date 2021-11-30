# WarpCTC

---

模型名称：WarpCTC

骨干网络： LSTM

模块类型：cv

可微调： False

输入形状： [64, 3, 64, 160]

模型版本：1.0

训练数据集：captcha 0.1.1

作者：MindSpore团队

更新时间：2020-9-23

代码仓链接：<https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/cv/warpctc>

用户ID：MindSpore

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：1.0

许可证：Apache 2.0

摘要：使用WarpCTC对captcha进行识别。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的Warpctc模型实现，目录为model_zoo/official/cv/warpctc。

使用已在码云上发布的代码在captcha数据集上训练该模型。
模块中所有参数均可训练。

## 用法

具体用法请参考ModelZoo的README描述和代码：
<https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/cv/warpctc>

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.