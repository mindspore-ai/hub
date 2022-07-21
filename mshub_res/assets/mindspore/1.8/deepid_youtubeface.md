# DeepID

---

model-name: DeepID

backbone-name: DeepID

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: youtubeface

evaluation: acc96.82

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/DeepID>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/deepid_ascend_v180_youtubeface_research_cv_acc96.82.ckpt>
    asset-sha256: 95b49d68c57f11284b49089cd8cb4c55896c5c0f2d1f0af2c720f08ab811ed86

license: Apache2.0

summary: DeepID is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of DeepID from the MindSpore model zoo on Gitee at research/cv/DeepID.

DeepID is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/DeepID](https://gitee.com/mindspore/models/blob/r1.8/research/cv/DeepID/README.md).

All parameters in the module are trainable.

## Citation

Sun Y, Wang X, Tang X. Deep learning face representation from predicting 10,000 classes[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2014: 1891-1898.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
