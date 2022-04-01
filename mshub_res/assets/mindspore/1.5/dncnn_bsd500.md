# DnCNN

---

model-name: DnCNN

backbone-name: DnCNN

module-type: cv

fine-tunable: True

model-version: 1.5

train-dataset: bsd500

evaluation: bsd68acc29 | set12acc30

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/research/cv/DnCNN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/dncnn_ascend_v150_bsd500_research_cv_bsd68acc29_set12acc30.ckpt>
    asset-sha256: e02c3010a0e6f8b5750e5de1fb5c12fa98ab932133cb1dbb62dfdd77f69607cd

license: Apache2.0

summary: DnCNN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of DnCNN from the MindSpore model zoo on Gitee at research/cv/DnCNN.

DnCNN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/DnCNN](https://gitee.com/mindspore/models/blob/r1.5/research/cv/DnCNN/README.md).

All parameters in the module are trainable.

## Citation

K. Zhang, W. Zuo, Y. Chen, D. Meng and L. Zhang, "Beyond a Gaussian Denoiser: Residual Learning of Deep CNN for Image Denoising," in IEEE Transactions on Image Processing, vol. 26, no. 7, pp. 3142-3155, July 2017, doi: 10.1109/TIP.2017.2662206.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
