# BGCF

---

模型名称：BGCF

骨干网络：BGCF

模块类型：推荐

可微调：True

输入形状： [7068, 3570]

模型版本：1.0

作者：MindSpore团队

更新时间：2020-9-19

代码仓链接：<https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/gnn/bgcf>

用户ID：MindSpore

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：1.0

许可证：Apache 2.0

摘要：使用BGCF进行物品推荐。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的BGCF实现，目录为model_zoo/official/gnn/bgcf。

更多详情参见[码云MindSpore ModelZoo](https://gitee.com/mindspore/mindspore/blob/master/model_zoo/official/gnn/bgcf/README.md)。

模块中所有参数均可训练。

## 用法

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms
from src.config import parser_args

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.0/bgcf_v1.0"

config = parser_args()
config.num_user = 7068
config.num_item = 3570
network = mshub.load(model, [config.input_dim, config.num_user, config.num_item], config.embedded_dimension, config.activation, [0.0, 0.0, 0.0], config.num_user, config.num_item, config.input_dim)
network.set_train(False)
# 推理与MindSpore模型相同，请参考 <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/gnn/bgcf>.
```

## 参考论文

1. Sun J , Guo W , Zhang D , et al. A Framework for Recommending Accurate and Diverse Items Using Bayesian Graph Convolutional Neural Networks[C]// KDD '20: The 26th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. ACM, 2020.
