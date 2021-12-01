# deepfm

---

model-name: deepfm

backbone-name: deepfm

module-type: recommend

fine-tunable: True

input-shape: [[1000, 39], [1000, 39]]

model-version: 1

author: MindSpore team

update-time: 2020-09-19

repo-link: <https://gitee.com/mindspore/models/tree/master/official/recommend/deepfm>

user-id: MindSpore

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-version: 1.0

license: Apache2.0

summary: deepfm used in recommend system

---

## Introduction

This MindSpore Hub model uses the implementation of deepfm from the MindSpore model zoo on Gitee at model_zoo/official/recommend/deepfm.

deepfm is a recommend network. More details please refer to the [MindSpore model zoo on Gitee](https://gitee.com/mindspore/models/blob/master/official/recommend/deepfm/README.md).

All parameters in the module are trainable.

## Citation

1. Huifeng Guo, Ruiming Tang, Yunming Ye, Zhenguo Li, Xiuqiang He. DeepFM: A Factorization-Machine based Neural Network for CTR Prediction.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.