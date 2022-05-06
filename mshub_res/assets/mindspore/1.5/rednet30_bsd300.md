# REDNet30

---

model-name: REDNet30

backbone-name: REDNet30

module-type: cv

fine-tunable: True

model-version: 1.5

train-dataset: bsd300

evaluation: psnr27.15 | ssim0.7783

author: MindSpore team

update-time: 2022-04-18

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/research/cv/REDNet30>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/rednet30_ascend_v150_bsd300_research_cv_psnr27.15_ssim0.7783.ckpt>
    asset-sha256: 535f724f7417fefb3edbcc9cf81555178b33e73f1897c40e89d0dde4e0159a5b

license: Apache2.0

summary: REDNet30 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of REDNet30 from the MindSpore model zoo on Gitee at research/cv/REDNet30.

REDNet30 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/REDNet30](https://gitee.com/mindspore/models/blob/r1.5/research/cv/REDNet30/README_CN.md).

All parameters in the module are trainable.

## Citation

Mao X J ,  Shen C ,  Yang Y B . [Image Restoration Using Very Deep Convolutional Encoder-Decoder Networks with Symmetric Skip Connections[J]](https://arxiv.org/pdf/1603.09056v2.pdf).  2016.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
