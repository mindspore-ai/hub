# UNet2D

---

模型名称：UNet2D

骨干网络：U-Net

模块类型：cv-semantic_segmentation

可微调：True

输入形状： [388, 388, 3]

模型版本：1

Dice系数：0.908

作者：MindSpore团队

更新时间：2020-9-22

代码仓链接： <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/unet>

用户ID：MindSpore

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：1.0

许可证：Apache 2.0

摘要：使用UNet对ISBI challenge进行二维图像分割。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的Unet2D实现，目录为model_zoo/official/cv/unet。

使用已在码云上发布的代码在ISBI Challenge数据集上训练该模型。

模块中所有参数均可训练。

## 用法

具体用法请参考ModelZoo的README描述和代码：
<https://gitee.com/mindspore/mindspore/blob/master/model_zoo/official/cv/unet/README.md>

## 参考论文

论文： Olaf Ronneberger, Philipp Fischer, Thomas Brox. "U-Net: Convolutional Networks for Biomedical Image Segmentation." *conditionally accepted at MICCAI 2015*. 2015.
