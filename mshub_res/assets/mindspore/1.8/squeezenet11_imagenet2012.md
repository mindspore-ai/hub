# squeezenet1_1

---

model-name: squeezenet1_1

backbone-name: squeezenet1_1

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: imagenet2012

evaluation: top1acc58.52 | top5acc80.82

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/squeezenet1_1>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/squeezenet11_ascend_v180_imagenet2012_research_cv_top1acc58.52_top5acc80.82.ckpt>
    asset-sha256: c50c0293a9efbe2a9338bf41df6e8c399c4ef40511e9d27a5ebef83deea61252

license: Apache2.0

summary: squeezenet1_1 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of squeezenet1_1 from the MindSpore model zoo on Gitee at research/cv/squeezenet1_1.

squeezenet1_1 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/squeezenet1_1](https://gitee.com/mindspore/models/blob/r1.8/research/cv/squeezenet1_1/README.md).

All parameters in the module are trainable.

## Citation

Forrest N. Iandola and Song Han and Matthew W. Moskewicz and Khalid Ashraf and William J. Dally and Kurt Keutzer. "SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and <0.5MB model size"

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
