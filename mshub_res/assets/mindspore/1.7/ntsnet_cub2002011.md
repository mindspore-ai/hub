# ntsnet

---

model-name: ntsnet

backbone-name: ntsnet

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: cub2002011

evaluation: acc87

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/research/cv/ntsnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/ntsnet_ascend_v170_cub2002011_research_cv_acc87.ckpt>
    asset-sha256: 4b29c87a6402cab44efcc499e46dcec2eddf2f35c84002434c4f66be8b0968cc

license: Apache2.0

summary: ntsnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ntsnet from the MindSpore model zoo on Gitee at research/cv/ntsnet.

ntsnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/ntsnet](https://gitee.com/mindspore/models/blob/r1.7/research/cv/ntsnet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.7/ntsnet_cub2002011"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Z. Yang, T. Luo, D. Wang, Z. Hu, J. Gao, and L. Wang, Learning to navigate for fine-grained classification, in Proceedings of the European Conference on Computer Vision (ECCV), 2018.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
