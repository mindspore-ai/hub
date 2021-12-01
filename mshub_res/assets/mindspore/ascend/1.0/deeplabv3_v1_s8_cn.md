# DeepLabv3

---

模型名称： DeepLab_v3_s8

骨干网络：ResNet-101

模块类型：cv-semantic_segmentation

可微调：True

输入形状： [897, 897, 3]

模型版本：1.0

准确率：0.798

作者：MindSpore团队

更新时间：2020-9-4

代码仓链接： <https://gitee.com/mindspore/models/tree/master/official/cv/deeplabv3>

用户ID：MindSpore

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：1.0

许可证：Apache 2.0

摘要：使用DeepLabv3进行图像语义分割。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的DeepLabv3实现，目录为model_zoo/official/cv/deeplabv3。

模块中所有参数均可训练。

## 用法

```python
import mindspore_hub as mshub
model = "mindspore/ascend/1.0/deeplabv3_v1"
# 根据预训练模型初始化类数
network = mshub.load(model, pretrained=False, num_classes=21)
#...
```

具体用法请参考ModelZoo的README描述： <https://gitee.com/mindspore/models/tree/master/official/cv/deeplabv3>

## 参考论文

1. Chen L C, Papandreou G, Schroff F, et al. Rethinking atrous convolution for semantic image segmentation[J]. arXiv preprint arXiv:1706.05587, 2017.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.