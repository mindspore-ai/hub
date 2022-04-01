# inception_resnet_v2

---

model-name: inception_resnet_v2

backbone-name: inception_resnet_v2

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: imagenet2012

evaluation: top1acc80.04 | top5acc94.54

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/inception_resnet_v2>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/inceptionresnetv2_ascend_v160_imagenet2012_research_cv_top1acc80.04_top5acc94.54.ckpt>
    asset-sha256: cf282d78635945173a79accf2068b0c651aff1253eeae556f31428190b7e3dbd

license: Apache2.0

summary: inception_resnet_v2 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of inception_resnet_v2 from the MindSpore model zoo on Gitee at research/cv/inception_resnet_v2.

inception_resnet_v2 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/inception_resnet_v2](https://gitee.com/mindspore/models/blob/r1.6/research/cv/inception_resnet_v2/README.md).

All parameters in the module are trainable.

## Citation

Christian Szegedy, Sergey Ioffe, Vincent Vanhoucke, Alex Alemi. Computer Vision and Pattern Recognition[J]. 2016.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
