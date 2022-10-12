# gan

---

model-name: gan

backbone-name: gan

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: mnist

evaluation: likelihood224.61 | se2.27

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/gan>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/gan_G_ascend_v190_mnist_research_cv_likelihood224.61_se2.27.ckpt>
    asset-sha256: c1dec359395c05b810ad2b7a3edc367834e931d282ba481bd3fd13710156c95a

license: Apache2.0

summary: gan is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of gan from the MindSpore model zoo on Gitee at research/cv/gan.

gan is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/gan](https://gitee.com/mindspore/models/blob/r1.9/research/cv/gan/README_CN.md).

All parameters in the module are trainable.

## Citation

Goodfellow I, Pouget-Abadie J, Mirza M, et al. Generative adversarial nets[J]. Advances in neural information processing systems, 2014, 27.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
