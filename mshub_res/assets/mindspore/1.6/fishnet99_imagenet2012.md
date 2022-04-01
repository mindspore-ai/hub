# fishnet99

---

model-name: fishnet99

backbone-name: fishnet99

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: imagenet2012

evaluation: top1acc77.88 | top5acc93.88

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/fishnet99>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/fishnet99_ascend_v160_imagenet2012_research_cv_top1acc77.88_top5acc93.88.ckpt>
    asset-sha256: 95e536ca3b4b1f1fa9061b5f9cf75bdc15fb2a1fc8e1a820442516c980ebf7d3

license: Apache2.0

summary: fishnet99 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of fishnet99 from the MindSpore model zoo on Gitee at research/cv/fishnet99.

fishnet99 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/fishnet99](https://gitee.com/mindspore/models/blob/r1.6/research/cv/fishnet99/README_CN.md).

All parameters in the module are trainable.

## Citation

FishNet: a versatile backbone for image, region, and pixel level prediction. In Proceedings of the 32nd International Conference on Neural Information Processing Systems (NIPS'18). Curran Associates Inc., Red Hook, NY, USA, 762–772.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
