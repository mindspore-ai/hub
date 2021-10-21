# ncf

---

model-name: ncf

backbone-name: ncf

module-type: recommend

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: movielens

accuracy: 70

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/recommend/ncf>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/ncf_ascend_v120_movielens_official_recommend_bs256_hracc70_ndcgacc42/ncf_ascend_v120_movielens_official_recommend_bs256_hracc70_ndcgacc42.ckpt>
    asset-sha256: ff7bd040b8e269a8a81b1dcc2f96e157bc4c279c7ecc84fe9c9a9f166690e99d

license: Apache2.0

summary: ncf is used for recommend

---

## Introduction

This MindSpore Hub model uses the implementation of ncf from the MindSpore model zoo on Gitee at model_zoo/official/recommend/ncf.

ncf is a recommend network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/recommend/ncf](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/recommend/ncf/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/ncf_v1.2_movielens"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. He X, Liao L, Zhang H, et al. Neural collaborative filtering[C]//Proceedings of the 26th international conference on world wide web. 2017: 173-182.
