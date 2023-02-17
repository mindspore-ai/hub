# ssd_ghostnet

---

model-name: ssd_ghostnet

backbone-name: ssd_ghostnet

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: coco2017

evaluation: acc24.26

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/ssd_ghostnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/ssdghostnet_ascend_v1100_coco2017_research_cv_acc24.26.ckpt>
    asset-sha256: a1893fc926f7d721952733e7c42557520e7933060b5eb35bb0fec31d0b19dd1a

license: Apache2.0

summary: ssd_ghostnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ssd_ghostnet from the MindSpore model zoo on Gitee at research/cv/ssd_ghostnet.

ssd_ghostnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/ssd_ghostnet](https://gitee.com/mindspore/models/blob/r1.10/research/cv/ssd_ghostnet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.10/ssdghostnet_coco2017"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[SSD: Single Shot MultiBox Detector](https://arxiv.org/pdf/1512.02325.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
