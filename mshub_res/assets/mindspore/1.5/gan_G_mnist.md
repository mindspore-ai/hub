# gan

---

model-name: gan

backbone-name: gan

module-type: cv

fine-tunable: True

model-version: 1.5

train-dataset: mnist

evaluation: likelihood220.47 | se2.33

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/research/cv/gan>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/gan_G_ascend_v150_mnist_research_cv_likelihood220.47_se2.33.ckpt>
    asset-sha256: 78dd2421ad81e2088cbb43ee11a019eb3ac74c27e1e75fff597cb3f659840c6b

license: Apache2.0

summary: gan is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of gan from the MindSpore model zoo on Gitee at research/cv/gan.

gan is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/gan](https://gitee.com/mindspore/models/blob/r1.5/research/cv/gan/README_CN.md).

All parameters in the module are trainable.

## Citation

Goodfellow I, Pouget-Abadie J, Mirza M, et al. Generative adversarial nets[J]. Advances in neural information processing systems, 2014, 27.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
