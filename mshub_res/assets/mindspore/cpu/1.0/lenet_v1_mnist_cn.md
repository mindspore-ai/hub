# LeNet

---

模型名称： LeNet

骨干网络： LeNet

模块类型：cv-classification

可微调：True

输入形状： [32, 32, 1]

模型版本：1.0

训练数据集：MNIST

准确率： 0.986

作者：MindSpore团队

更新时间：2020-10-29

代码仓链接： <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/lenet>

用户ID：MindSpore

用途：推理

训练后端：CPU

推理后端：CPU

MindSpore版本：1.0

资源：

-
    文件格式：.ckpt  
    资源链接： <https://download.mindspore.cn/model_zoo/official/cv/lenet/lenet_cpu_1.0.0_mnist_official_classification_20201029/lenet.ckpt>  
    资源SHA256校验码：b0771234226405a68f1c9ce3ecbffb1ee371dd3cb13ae85b7a26870031c05ec8

许可证：Apache 2.0

摘要：使用LeNet对MNIST的10个类进行分类。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的LeNet实现，目录为model_zoo/official/cv/lenet。

使用已在码云上发布的代码在MNSIT上数据集上训练该模型。

模块中所有参数均可训练。

## 用法

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE, device_target="CPU")

model = "mindspore/cpu/1.0/lenet_v1_mnist"
# 根据预训练模型初始化类数
network = mshub.load(model)
network.set_train(False)

# 推理与MindSpore模型相同。
# ...
```

## 参考论文

1. Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner. "Gradient-based learning applied to document recognition." Proceedings of the IEEE, 86(11):2278-2324, November 1998.
