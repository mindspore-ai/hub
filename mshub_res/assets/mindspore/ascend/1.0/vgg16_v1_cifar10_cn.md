# VGG16

---

模型名称： VGG16

骨干网络： VGG16

模块类型：cv-classification

可微调：True

输入形状： [224, 224, 3]

模型版本：1.0

训练数据集：CIFAR-10

准确率： 0.93

作者：MindSpore团队

更新时间：2020-9-22

代码仓链接：<https://gitee.com/mindspore/models/tree/master/official/cv/vgg16>

用户ID：MindSpore

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：1.0

资源：

-
    文件格式：.ckpt  
    资源链接：<https://download.mindspore.cn/model_zoo/official/cv/vgg/vgg16_ascend_1.0_cifar10_official_classification_20200923/vgg16.ckpt>  
    资源SHA256校验码：8f24d2782b3f6ec0380c1ea597ba24c1cf8749d1b0411e147263e266788869e4

-
    文件格式：.air  
    资源链接：<https://download.mindspore.cn/model_zoo/official/cv/vgg/vgg16_ascend_1.0_cifar10_official_classification_20200923/vgg16.geir>  
    资源SHA256校验码：2ebff88197f0fdefbb3249fa8770a48fe8242b3e69333a2e76af147158108cf9

许可证：Apache 2.0

摘要：使用VGG16对CIFAR-10的10个类进行分类。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的VGG16实现，目录为model_zoo/official/cv/vgg16。

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

model = "mindspore/ascend/1.0/vgg16_v1_cifar10"
# 根据预训练模型初始化类数
network = mshub.load(model, num_classes=10)
network.set_train(False)

# 推理与MindSpore模型相同。
# ...
```

## 参考论文

Simonyan K, zisserman A. Very Deep Convolutional Networks for Large-Scale Image Recognition[J]. arXiv preprint arXiv:1409.1556, 2014.
