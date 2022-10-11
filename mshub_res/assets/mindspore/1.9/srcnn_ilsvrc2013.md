# srcnn

---

model-name: srcnn

backbone-name: srcnn

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: ilsvrc2013

evaluation: set5acc36.65 | set14acc32.57 | bsd200acc33.77

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/cv/srcnn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/srcnn_ascend_v190_ilsvrc2013_official_cv_set5acc36.65_set14acc32.57_bsd200acc33.77.ckpt>
    asset-sha256: a55d5c782c1d131cefca86ad0c823fcbe610496429a552a39e0276b47428f212

license: Apache2.0

summary: srcnn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of srcnn from the MindSpore model zoo on Gitee at official/cv/srcnn.

srcnn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/srcnn](https://gitee.com/mindspore/models/blob/r1.9/official/cv/srcnn/README_CN.md).

All parameters in the module are trainable.

## Citation

Chao Dong, Chen Change Loy, Kaiming He, Xiaoou Tang. Image Super-Resolution Using Deep Convolutional Networks. 2014.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
