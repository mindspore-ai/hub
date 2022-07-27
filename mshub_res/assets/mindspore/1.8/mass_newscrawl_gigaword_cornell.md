# mass

---

model-name: mass

backbone-name: mass

module-type: nlp

fine-tunable: True

model-version: 1.8

train-dataset: newscrawl_gigaword_cornell

evaluation: RG1acc51.77 | RG2acc34.46 | RGL49.89

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/official/nlp/mass>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/mass_ascend_v180_newscrawl_gigaword_cornell_official_nlp_RG1acc51.77_RG2acc34.46_RGL49.89.ckpt>
    asset-sha256: 98414b2c2e27d7b8ee51754e5bf251fedb10f8700ed86ce25503df9b976b63ce

license: Apache2.0

summary: mass is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of mass from the MindSpore model zoo on Gitee at official/nlp/mass.

mass is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [official/nlp/mass](https://gitee.com/mindspore/models/blob/r1.8/official/nlp/mass/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.8/mass_newscrawl_gigaword_cornell"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Song, Kaitao, Xu Tan, Tao Qin, Jianfeng Lu and Tie-Yan Liu.“MASS: Masked Sequence to Sequence Pre-training for Language Generation.”ICML (2019).

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
