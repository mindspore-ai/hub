# mnasnet

---

model-name: mnasnet

backbone-name: mnasnet

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: imagenet2012

evaluation: top1acc73.98 | top5acc91.68

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/mnasnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/mnasnet_ascend_v180_imagenet2012_research_cv_top1acc73.98_top5acc91.68.ckpt>
    asset-sha256: d72b9a520a7687c0017289dc80cb480f84c01d8542fee1fa367ab914467f69c2

license: Apache2.0

summary: mnasnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of mnasnet from the MindSpore model zoo on Gitee at research/cv/mnasnet.

mnasnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/mnasnet](https://gitee.com/mindspore/models/blob/r1.8/research/cv/mnasnet/README_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.8/mnasnet_imagenet2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Mingxing Tan, Bo Chen, Ruoming Pang, Vijay Vasudevan, Mark Sandler, Andrew Howard, Quoc V. Le. MnasNet: Platform-Aware Neural Architecture Search for Mobile 2018.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
