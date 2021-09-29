# GoogleNet

---

模型名称： GoogleNet

骨干网络：GoogleNet

模块类型：cv-classification

可微调：True

输入形状： [224, 224, 3]

模型版本：1.0

训练数据集：CIFAR-10

准确率： 0.934

作者：MindSpore团队

更新时间：2020-9-22

代码仓链接： <https://gitee.com/mindspore/models/tree/master/official/cv/googlenet>

用户ID：MindSpore

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：0.7

资源：

  -
    文件格式：.ckpt  
    资源链接： <https://download.mindspore.cn/model_zoo/official/cv/googlenet/googlenet_ascend_0.7.0_cifar10_official_classification_20200922/googlenet.ckpt>  
    资源SHA256校验码：2dac4b4867080821d170f43e2d64dcdc9e75bb4d5760b00c4f88eaffd4dd9424

许可证：Apache 2.0

摘要：使用GoogleNet对CIFAR-10的10个类进行分类。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的GoogleNet实现，目录为model_zoo/official/cv/googlenet。

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

model = "mindspore/ascend/0.7/googlenet_v1_cifar10"
# 根据预训练模型初始化类数
network = mshub.load(model, num_classes=10)
network.set_train(False)

# 推理与MindSpore模型相同。
# ...
```

## 参考论文

1. Szegedy C, Liu W, Jia Y, et al. Going deeper with convolutions[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2015: 1-9.
2. Krizhevsky A, Hinton G. Learning multiple layers of features from tiny images[J].2009.
