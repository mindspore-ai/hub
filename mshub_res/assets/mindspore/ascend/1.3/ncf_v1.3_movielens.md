# ncf

---

model-name: ncf

backbone-name: ncf

module-type: recommend

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: movielens

accuracy: 70.25

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/recommend/ncf>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/temp/ncf_ascend_v130_movielens_official_recommend_bs256_acchr%3D70.25_ndcg%3D42.23/ncf_ascend_v130_movielens_official_recommend_bs256_acchr%3D70.25_ndcg%3D42.23.ckpt>
    asset-sha256: ff7bd040b8e269a8a81b1dcc2f96e157bc4c279c7ecc84fe9c9a9f166690e99d

license: Apache2.0

summary: ncf is used for recommend

---

## Introduction

This MindSpore Hub model uses the implementation of ncf from the MindSpore model zoo on Gitee at model_zoo/official/recommend/ncf.

ncf is a recommend network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/recommend/ncf](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/recommend/ncf/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore
import mindspore_hub as mshub
from mindspore import Tensor
from mindspore import nn
from mindspore import context
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.3/ncf_v1.3_movielens"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. He X, Liao L, Zhang H, et al. Neural collaborative filtering[C]//Proceedings of the 26th international conference on world wide web. 2017: 173-182.
