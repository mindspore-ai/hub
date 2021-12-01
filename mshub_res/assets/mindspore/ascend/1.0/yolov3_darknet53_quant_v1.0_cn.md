# yolov3_darknet53_quant

---

模型名称：yolov3_darknet53_quant

骨干网络：darknet53_quent

模块类型：cv-object_detection

可微调：True

输入形状： [608, 608, 3]

模型版本：1

作者：MindSpore团队

更新时间：2020-9-19

代码仓链接：<https://gitee.com/mindspore/models/tree/master/official/cv/yolov3_darknet53_quant>。

用户ID：MindSpore

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：1.0

许可证：Apache 2.0

摘要：使用yolov3_darknet53_quant进行目标检测，减小权重，提升低比特计算性能。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的yolov3_darknet53_quent实现，目录为model_zoo/official/cv/yolov3_darknet53_quent。

yolov3_darknet53_quant支持10种不同的输入形状，提高了准确率。更多详情参见[码云MindSpore ModelZoo](https://gitee.com/mindspore/models/blob/master/official/cv/yolov3_darknet53_quant/README.md)。

模块中所有参数均可训练。

## 参考论文

1. Joseph Redmon, Ali Farhadi. arXiv preprint arXiv:1804.02767, 2018. 2, 4, 7, 11.
2. Krishnamoorthi R. Quantizing deep convolutional networks for efficient inference: A whitepaper. arXiv preprint arXiv:1806.08342, 2018

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.