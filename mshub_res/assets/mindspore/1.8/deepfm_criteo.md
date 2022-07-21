# deepfm

---

model-name: deepfm

backbone-name: deepfm

module-type: recommend

fine-tunable: True

model-version: 1.8

train-dataset: criteo

evaluation: acc80.5

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/official/recommend/deepfm>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/deepfm_ascend_v180_criteo_official_recommend_acc80.5.ckpt>
    asset-sha256: 57e11deb538dd32a8612ee655c14fe1438afe993ecd1a98c6ba6cf9e9c73e22d

license: Apache2.0

summary: deepfm is used for recommend

---

## Introduction

This MindSpore Hub model uses the implementation of deepfm from the MindSpore model zoo on Gitee at official/recommend/deepfm.

deepfm is a recommend network. More details please refer to the MindSpore model zoo on Gitee at [official/recommend/deepfm](https://gitee.com/mindspore/models/blob/r1.8/official/recommend/deepfm/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.8/deepfm_criteo"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Huifeng Guo, Ruiming Tang, Yunming Ye, Zhenguo Li, Xiuqiang He. DeepFM: A Factorization-Machine based Neural Network for CTR Prediction

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
