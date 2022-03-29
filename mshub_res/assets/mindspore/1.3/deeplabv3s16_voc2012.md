# deeplabv3

---

model-name: deeplabv3

backbone-name: deeplabv3

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: voc2012

evaluation: acc78.68

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/official/cv/deeplabv3>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/deeplabv3s16_ascend_v130_voc2012_official_cv_acc78.68.ckpt>
    asset-sha256: 46e997f97de3d6d4e35405be59bbb621c12d3ce62a688939f9046179473bfd9e

license: Apache2.0

summary: deeplabv3 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of deeplabv3 from the MindSpore model zoo on Gitee at official/cv/deeplabv3.

deeplabv3 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/deeplabv3](https://gitee.com/mindspore/models/blob/r1.3/official/cv/deeplabv3/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.3/deeplabv3s16_voc2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Chen L C, Papandreou G, Schroff F, et al. Rethinking atrous convolution for semantic image segmentation[J]. arXiv preprint arXiv:1706.05587, 2017.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
