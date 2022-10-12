# fishnet99

---

model-name: fishnet99

backbone-name: fishnet99

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: imagenet2012

evaluation: top1acc78.22 | top5acc94.02

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/fishnet99>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/fishnet99_ascend_v190_imagenet2012_research_cv_top1acc78.22_top5acc94.02.ckpt>
    asset-sha256: aa663ae5de67b24a6c447ce5b35f0873649d03eb31269703dfc4d087cf8f595c

license: Apache2.0

summary: fishnet99 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of fishnet99 from the MindSpore model zoo on Gitee at research/cv/fishnet99.

fishnet99 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/fishnet99](https://gitee.com/mindspore/models/blob/r1.9/research/cv/fishnet99/README_CN.md).

All parameters in the module are trainable.

## Citation

FishNet: a versatile backbone for image, region, and pixel level prediction. In Proceedings of the 32nd International Conference on Neural Information Processing Systems (NIPS'18). Curran Associates Inc., Red Hook, NY, USA, 762–772.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
