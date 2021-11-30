# Warpctc

---

model-name: warpctc

backbone-name: LSTM

module-type: cv

fine-tunable: False

input-shape: [64, 3, 64, 160]

model-version: 1.0

train-dataset: captcha 0.1.1

author: MindSpore team

update-time: 2020-09-23

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/cv/warpctc>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

license: Apache2.0

summary: warpctc used to do captcha recognition.

---

## Introduction

This MindSpore Hub model uses the implementation of Warpctc Model from the MindSpore model zoo on Gitee at model_zoo/official/cv/warpctc.

This model has been trained on captcha using the code published on Gitee.
All Parameters in the module are trainable.

## Usage

Refer to the readme description and code of modelzoo for specific usage:
<https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/cv/warpctc>

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.