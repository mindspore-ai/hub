# FasterRcnn

---

模型名称：faster_rcnn

骨干网络：ResNet-50

模块类型：cv-object_detection

可微调：True

输入形状： [768, 1280, 3]

模型版本：1

mAP(0.5)：0.576

作者：MindSpore团队

更新时间：2020-9-10

代码仓链接：<https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/faster_rcnn>

用户ID：MindSpore

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：0.7

许可证：Apache 2.0

摘要：使用Faster R-CNN检测COCO 2017中的80个类。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的FasterRcnn实现，目录为model_zoo/official/cv/faster_rcnn。

使用已在码云上发布的代码在COCO 2017数据集上训练该模型。

模块中所有参数均可训练。

## 用法

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms
from PIL import Image
import cv2

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/0.7/fasterrcnn_v1_coco2017"

network = mshub.load(model, is_training=False)
network.set_train(False)
```

## 参考论文

1. Ren S , He K , Girshick R , et al. Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks[J]. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2015, 39(6).
