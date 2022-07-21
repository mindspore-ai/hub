# ncf

---

model-name: ncf

backbone-name: ncf

module-type: recommend

fine-tunable: True

model-version: 1.8

train-dataset: movielens

evaluation: hr69.56 | ndcg41.54

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/official/recommend/ncf>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/ncf_ascend_v180_movielens_official_recommend_hr69.56_ndcg41.54.ckpt>
    asset-sha256: ff7bd040b8e269a8a81b1dcc2f96e157bc4c279c7ecc84fe9c9a9f166690e99d

license: Apache2.0

summary: ncf is used for recommend

---

## Introduction

This MindSpore Hub model uses the implementation of ncf from the MindSpore model zoo on Gitee at official/recommend/ncf.

ncf is a recommend network. More details please refer to the MindSpore model zoo on Gitee at [official/recommend/ncf](https://gitee.com/mindspore/models/blob/r1.8/official/recommend/ncf/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.8/ncf_movielens"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

He X, Liao L, Zhang H, et al. Neural collaborative filtering[C]//Proceedings of the 26th international conference on world wide web. 2017: 173-182.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
