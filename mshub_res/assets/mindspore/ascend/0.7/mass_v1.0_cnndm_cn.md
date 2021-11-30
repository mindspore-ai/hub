# MASS

---

模型名称：MASS

骨干网络： MassModel

模块类型：NLP

可微调：True

输入形状： [[1, 128], [1, 128], [1, 128], [1, 128], [1, 128], [1, 128]]

模型版本：1.0

作者：MindSpore团队

更新时间：2020-9-21

代码仓链接： <https://gitee.com/mindspore/mindspore/tree/r0.7/model_zoo/official/nlp/mass>

用户ID：MindSpore

用途：推理/迁移学习

训练后端：Ascend

推理后端：Ascend

MindSpore版本：0.7

许可证：Apache 2.0

摘要：使用MASS对各种数据集进行对话响应。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的MASSModel实现，目录为model_zoo/official/nlp/mass。

使用已在码云上发布的代码在cnndm数据集上训练该模型。

模块中所有参数均可训练。

## 用法

具体用法请参考ModelZoo的README描述和代码：
<https://gitee.com/mindspore/mindspore/blob/r0.7/model_zoo/official/nlp/mass/README.md>

## 参考论文

论文： Song, Kaitao, Xu Tan, Tao Qin, Jianfeng Lu and Tie-Yan Liu. “MASS: Masked Sequence to Sequence Pre-training for Language Generation.” ICML (2019).

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.