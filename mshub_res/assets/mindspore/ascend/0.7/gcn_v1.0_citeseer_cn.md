# GCN

---

模型名称：GCN

骨干网络：GCN

模块类型：NLP

可微调：True

输入形状： [3327, 3703, 6]

模型版本：1.0

作者：MindSpore团队

更新时间：2020-9-19

代码仓链接：<https://gitee.com/mindspore/models/tree/master/official/gnn/gcn>。

用户ID：MindSpore

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：0.7

许可证：Apache 2.0

摘要：使用GCN进行文本分类。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的GCN实现，目录为model_zoo/official/gnn/gcn。

更多详情参见[码云MindSpore ModelZoo](https://gitee.com/mindspore/models/blob/master/official/gnn/gcn/README.md)。

## 用法

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms
from src.config import ConfigGCN

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/0.7/gcn_v1.0_citeseer"

config = ConfigGCN
input_dim = 3703
class_num = 6
network = mshub.load(model, config, input_dim, class_num)
network.set_train(False)
# 推理与MindSpore模型相同，请参考 <https://gitee.com/mindspore/models/tree/master/official/gnn/gcn>。
```

## 参考论文

1. Kipf T N , Welling M . Semi-Supervised Classification with Graph Convolutional Networks[J]. 2016.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.