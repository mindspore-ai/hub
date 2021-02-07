# GCN

---

模型名称：GCN

骨干网络：GCN

模块类型：NLP

可微调：True

输入形状： [2708, 1433, 7]

模型版本：1.0

作者：MindSpore团队

更新时间：2020-9-19

代码仓链接：<https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/gnn/gcn>。

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

更多详情参见[码云MindSpore ModelZoo](https://gitee.com/mindspore/mindspore/blob/master/model_zoo/official/gnn/gcn/README.md)。

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

model = "mindspore/ascend/0.7/gcn_v1.0_cora"

config = ConfigGCN
input_dim = 1433
class_num = 7
network = mshub.load(model, config, input_dim, class_num)
network.set_train(False)
# 推理与MIndSpore模型相同，请参考 <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/gnn/gcn>。
```

## 参考论文

1. Kipf T N , Welling M . Semi-Supervised Classification with Graph Convolutional Networks[J]. 2016.
