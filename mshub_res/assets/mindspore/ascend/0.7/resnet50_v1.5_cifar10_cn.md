# ResNet-50

---

模型名称：ResNet-50

骨干网络：ResNet-50

模块类型：cv-classification

可微调：True

输入形状： [224, 224, 3]

模型版本：1.5

训练数据集：CIFAR-10

准确率：0.91

作者：MindSpore团队

更新时间：2020-8-26

代码仓链接：<https://gitee.com/mindspore/models/tree/master/official/cv/resnet>。

用户ID：MindSpore

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：0.7

资源：

-
    文件格式：.ckpt  
    资源链接：<https://download.mindspore.cn/model_zoo/official/cv/resnet/resnet50_v1.5_ascend_0.3.0_cifar10_official_classification_20200718/resnet50.ckpt>  
    资源SHA256校验码： 242da26be495f09ac8571811ba163ca22cda86025e800f1c04c4cddeaa3fa55b

-
    文件格式：.air  
    资源链接：<https://download.mindspore.cn/model_zoo/official/cv/resnet/resnet50_v1.5_ascend_0.3.0_cifar10_official_classification_20200718/resnet50.geir>  
    资源SHA256校验码：b06031e2970316597f4f3c4f89ccfd859b9ef665fd21e001a5e8d46a886dbf67

许可证：Apache 2.0

摘要：使用ResNet-50对CIFAR-10的10个类进行分类。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的ResNet50实现，目录为model_zoo/official/cv/resnet。

使用已在码云上发布的代码在CIFAR-10数据集上训练该模型。

模块中所有参数均可训练。

## 用法

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

model = "mindspore/ascend/0.7/resnet50_v1.5_cifar10"
network = mshub.load(model, class_num=10)
network.set_train(False)

# 推理与MindSpore模型相同。
# ...
```

## 参考论文

1. He K , Zhang X , Ren S , et al. Deep Residual Learning for Image Recognition[J]. 2016.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.