# GhostNet-SSD

---

模型名称：GhostNet_SSD

骨干网络：GhostNet1.3x

模块类型：cv-object_detection

可微调：True

输入形状： [3, 300, 300]

模型版本：1.0

mAP：0.241

作者：Noah's Ark Lab

更新时间：2020-9-8

代码仓链接： <https://gitee.com/mindspore/models/tree/master/research/cv/ssd_ghostnet>

用户ID：noah-cvlab

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：0.7

许可证：Apache 2.0

摘要：ssd_ghostnet是主干为GhostNet的SSD模型。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的ssd_ghostnet实现，目录为model_zoo/official/cv/ssd_ghostnet。

模块中所有参数均可训练。

## 用法

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "noah-cvlab/ascend/0.7/ghostnet_ssd_v1.0"
network = mshub.load(model)
network.set_train(False)

```

## 参考论文

1. [论文](https://arxiv.org/abs/1512.02325)：   Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott Reed, Cheng-Yang Fu, Alexander C. Berg.European Conference on Computer Vision (ECCV), 2016 (In press).
2. [论文](https://openaccess.thecvf.com/content_CVPR_2020/html/Han_GhostNet_More_Features_From_Cheap_Operations_CVPR_2020_paper.html)：   Kai Han, Yunhe Wang, Qi Tian, Jianyuan Guo, Chunjing Xu, Chang Xu.Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2020, pp. 1580-1589.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.