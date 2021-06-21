# CenterNet

---

模型名称：CenterNet

骨干网络：DLA-34

模块类型：cv

可微调：True

输入形状： [512, 512, 3]

模型版本：1

作者：MindSpore团队

更新时间：2020-12-21

代码仓链接： <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/research/cv/centernet>

用户ID：MindSpore

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：1.0

许可证：Apache 2.0

摘要：使用CenterNet检测多人姿势。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的centernet实现，目录为model_zoo/research/cv/centernet。

CenterNet是一个无锚点检测网络。对象作为边框的单个中心点进行建模，检测器使用关键点估计找到中心点并回归到所有其他对象属性。更多详情参见[码云MindSpore ModelZoo](https://gitee.com/mindspore/mindspore/tree/master/model_zoo/research/cv/centernet/README.md)。

模块中所有参数均可训练。

## 用法

具体用法请参考ModelZoo的README描述和代码：
<https://gitee.com/mindspore/mindspore/tree/master/model_zoo/research/cv/centernet>

## 参考论文

1. Xingyi Zhou, Dequan Wang, Philipp Krahenbuhl. Objects as Points. arXiv:1904.07850v2[cs.CV], 2019. 4.
