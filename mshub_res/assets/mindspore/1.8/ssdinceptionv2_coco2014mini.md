# ssd_inceptionv2

---

model-name: ssd_inceptionv2

backbone-name: ssd_inceptionv2

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: coco2014mini

evaluation: mAP24

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/ssd_inceptionv2>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/ssdinceptionv2_ascend_v180_coco2014mini_research_cv_mAP24.ckpt>
    asset-sha256: c081a75c11307ace671e36168a17aa14c0d862736b96c9853329add2af7c9dfc

license: Apache2.0

summary: ssd_inceptionv2 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ssd_inceptionv2 from the MindSpore model zoo on Gitee at research/cv/ssd_inceptionv2.

ssd_inceptionv2 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/ssd_inceptionv2](https://gitee.com/mindspore/models/blob/r1.8/research/cv/ssd_inceptionv2/README_CN.md).

All parameters in the module are trainable.

## Citation

Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott Reed, Cheng-Yang Fu, Alexander C. Berg.European Conference on Computer Vision (ECCV), 2016 (In press).

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
