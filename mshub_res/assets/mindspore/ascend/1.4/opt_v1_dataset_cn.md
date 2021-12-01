# OPT

---

模型名称: OPT

网络: BertModel

模型类型: 检索和图片描述

可微调: True

input-shape: [, 2048]

模型版本: 1.0

预训练数据集:
CC3M 提供大约300万个图像-文本对，我们将英文字幕翻译成中文。

COCO Captions 提供大约40万个图像-文本对，我们将英文字幕翻译成中文。

AIC 提供大约100万个中文的图像-文本对。

检索数据集: COCO Captions

图像描述数据集：COCO Captions

准确率:

作者: 中国科学院自动化所iva组

更新时间: 2021-12-2

代码仓链接:

用户ID: MindSpore

用途: 推理

训练后端: ascend

推理后端: ascend

mindspore版本: 1.4

asset:

-
    file-format: ckpt  
    asset-link:
    asset-sha256:

license: Apache2.0

总结: 基于OPT三模态预训练大模型来进行检索和图像描述。

---

## Introduction

MindSpore Hub模型采用了gitee上的MindSpore model zoo(model_zoo/ )的实现。

该模型已使用Gitee上发布的代码在 cc3m、coco 和 aic 上进行了预训练和两个下游任务的finetune。

模型中所有的参数都是可训练的。

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.0/"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Liu J, Zhu X, Liu F, et al. OPT: Omni-Perception Pre-Trainer for Cross-Modal Understanding and Generation[J]. arXiv preprint arXiv:2107.00249, 2021.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.