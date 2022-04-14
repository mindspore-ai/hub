# cspdarknet53

---

model-name: cspdarknet53

backbone-name: cspdarknet53

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: imagenet2012

evaluation: top1acc78.48 | top5acc94.00

author: MindSpore team

update-time: 2022-04-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/official/cv/cspdarknet53>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/cspdarknet53_ascend_v160_imagenet2012_official_cv_top1acc78.48_top5acc94.00.ckpt>
    asset-sha256: 03a80383ab6b3dda366af837b2bf1edcb54255d7a21cc613bbb107525d242025

license: Apache2.0

summary: cspdarknet53 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of cspdarknet53 from the MindSpore model zoo on Gitee at official/cv/cspdarknet53.

cspdarknet53 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/cspdarknet53](https://gitee.com/mindspore/models/blob/r1.6/official/cv/cspdarknet53/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.6/cspdarknet53_imagenet2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Chien-Yao Wang, Hong-Yuan Mark Liao, Yueh-Hua Wu, Ping-Yang Chen, Jun-Wei Hsieh, and I-Hau Yeh. CSPNet: A new backbone that can enhance learning capability of cnn. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition Workshop (CVPR Workshop), 2020. 2, 7

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
