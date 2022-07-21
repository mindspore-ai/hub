# ISyNet

---

model-name: ISyNet

backbone-name: ISyNet

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: imagenet2012

evaluation: top1acc76.00

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/ISyNet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/isynet_N1_ascend_v180_imagenet2012_research_cv_top1acc76.00.ckpt>
    asset-sha256: 7eeff09fcf17bfb5b64e39f304c433fc565c023d1e46e78d5424a5d370c0dbd5

license: Apache2.0

summary: ISyNet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ISyNet from the MindSpore model zoo on Gitee at research/cv/ISyNet.

ISyNet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/ISyNet](https://gitee.com/mindspore/models/blob/r1.8/research/cv/ISyNet/README.md).

All parameters in the module are trainable.

## Citation

Alexey Letunovskiy, Vladimir Korviakov, Vladimir Polovnikov, Anastasiia Kargapoltseva, Ivan Mazurenko, Yepan Xiong. ISyNet: Convolutional Neural Networks design for AI accelerator.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
