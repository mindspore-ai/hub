# dem

---

model-name: dem

backbone-name: dem

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: cub

evaluation: acc59.63

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/dem>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/dem_att_ascend_v160_cub_research_cv_acc59.63.ckpt>
    asset-sha256: b355ea64eabc6f4ba8462c952a8973885dcbb06623879a921f11b3e9d14ff474

license: Apache2.0

summary: dem is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of dem from the MindSpore model zoo on Gitee at research/cv/dem.

dem is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/dem](https://gitee.com/mindspore/models/blob/r1.6/research/cv/dem/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.6/dem_att_cub"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Li Zhang, Tao Xiang, Shaogang Gong."Learning a Deep Embedding Model for Zero-Shot Learning" *Proceedings of the CVPR*.2017.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
