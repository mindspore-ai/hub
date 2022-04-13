# ESRGAN

---

model-name: ESRGAN

backbone-name: ESRGAN

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: div2k

evaluation: set5psnr32.57 | set14psnr28.78

author: MindSpore team

update-time: 2022-04-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/ESRGAN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/esrgan_generator_ascend_v160_div2k_research_cv_set5psnr32.57_set14psnr28.78.ckpt>
    asset-sha256: aae12ae5679874a8fa5bded531ba528851d32f1e9d860a354584e11a7218a133

license: Apache2.0

summary: ESRGAN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ESRGAN from the MindSpore model zoo on Gitee at research/cv/ESRGAN.

ESRGAN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/ESRGAN](https://gitee.com/mindspore/models/blob/r1.6/research/cv/ESRGAN/README.md).

All parameters in the module are trainable.

## Citation

Xintao Wang, Ke Yu, Shixiang Wu, Jinjin Gu, Yihao Liu, Chao Dong, Chen Change Loy, Yu Qiao, Xiaoou Tang.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
