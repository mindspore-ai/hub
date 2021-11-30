# ResNeXt50

---

model-name: resnext50

backbone-name: resnext50

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.0

author: MindSpore team

update-time: 2020-09-22

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/cv/resnext50>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/resnext50_ascend_v111_imagenet2012_offical_cv_bs128_acc78/resnext50_ascend_v111_imagenet2012_offical_cv_bs128_acc78.ckpt>
    asset-sha256: 581d3e7a97d408d4f690ef5f362e5435d853348f1f0f18c351931ab77e8f3e45

license: Apache2.0

summary: resnext50 for image classification

---

## Introduction

This MindSpore Hub model uses the implementation of ResNeXt50 from the MindSpore model zoo on Gitee at model_zoo/official/cv/resnext50.

More details please refer to the [MindSpore model zoo on Gitee](https://gitee.com/mindspore/mindspore/blob/r1.0/model_zoo/official/cv/resnext50/README.md).

## Citation

1. Xie S, Girshick R, Dollár, Piotr, et al. Aggregated Residual Transformations for Deep Neural Networks. 2016.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.