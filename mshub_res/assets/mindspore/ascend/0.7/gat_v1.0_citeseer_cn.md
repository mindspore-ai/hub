# GAT

---

模型名称：GAT

骨干网络：GAT

模块类型：NLP

可微调：True

输入形状： [3327, 3703, 6]

模型版本：1.0

作者：MindSpore团队

更新时间：2020-9-19

代码仓链接：<https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/gnn/gat>。

用户ID：MindSpore

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：0.7

许可证：Apache 2.0

摘要：使用GAT进行文本分类。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的GAT实现，目录为model_zoo/official/gnn/gat。

更多详情参见[码云MindSpore ModelZoo](https://gitee.com/mindspore/mindspore/blob/master/model_zoo/official/gnn/gat/README.md)

模块中所有参数均可训练。

## 用法

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms
from src.config import GatConfig

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/0.7/gat_v1.0_citeseer"

config = GatConfig
config.feature_size = 3703
config.num_class = 6
config.num_nodes = 3327
network = mshub.load(model, config.feature_size, config.num_class, config.num_nodes,
                     config.hid_units, config.n_heads, 0.0, 0.0)
network.set_train(False)
# 推理与MindSpore模型相同，请参考 <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/gnn/gat>。
```

## 参考论文

1. Velikovi P , Cucurull G , Casanova A , et al. Graph Attention Networks[J]. 2017.
