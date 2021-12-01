# PSENet

---

模型名称：PSENet

骨干网络：ResNet-50

模块类型：cv

可微调：True

输入形状： [640, 640, 3]

模型版本：1

调和平均数： 0.81

作者：MindSpore团队

更新时间：2020-12-31

代码仓链接： <https://gitee.com/mindspore/models/tree/master/official/cv/psenet>

用户ID：MindSpore

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：1.0

资源:

  -
    文件格式: .ckpt  
    资源链接: <https://download.mindspore.cn/model_zoo/official/cv/psenet/psenet_ascend_1.1.0_icdar2015_official_text_detection_20210111/psenet.ckpt>  
    资源SHA256校验码: f5cf126c1059b9d4aa1ad9f30a954a385882ea79f25ea3d19c13c67ead4f1a2y  

许可证：Apache 2.0

摘要：使用PSENet对ICDAR2015数据集进行cv文本检测。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的PSENet实现，目录为model_zoo/official/cv/psenet。

使用已在码云上发布的代码在ICDAR2015数据集上训练该模型。更多详情参见[码云MindSpore ModelZoo](https://gitee.com/mindspore/models/tree/master/official/cv/psenet/README.md)。

模块中所有参数均可训练。

## 用法

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms
from src.config import config

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.0/psenet_v1.0_icdar2015"

network = mshub.load(model, config=config)
network.set_train(False)
# 推理与MindSpore模型相同, 请参考 <https://gitee.com/mindspore/models/tree/master/official/cv/psenet>。
```

## 参考论文

论文： Wenhai Wang, Enze Xie, Xiang Li, Wenbo Hou, Tong Lu, Gang Yu, Shuai Shao; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2019, pp. 9336-9345

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.