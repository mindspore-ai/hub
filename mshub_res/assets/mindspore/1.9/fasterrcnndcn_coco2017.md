# faster_rcnn_dcn

---

model-name: faster_rcnn_dcn

backbone-name: faster_rcnn_dcn

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: coco2017

evaluation: mAP40.0

author: MindSpore team

update-time: 2022-10-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/faster_rcnn_dcn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/fasterrcnndcn_ascend_v190_coco2017_research_cv_mAP40.0.ckpt>
    asset-sha256: 68d2aaec8feaf841ff6b61be07b45b3a03a7fd44ec77cc3192f8f3f11101ea53

license: Apache2.0

summary: faster_rcnn_dcn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of faster_rcnn_dcn from the MindSpore model zoo on Gitee at research/cv/faster_rcnn_dcn.

faster_rcnn_dcn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/faster_rcnn_dcn](https://gitee.com/mindspore/models/blob/r1.9/research/cv/faster_rcnn_dcn/README.md).

All parameters in the module are trainable.

## Citation

1. [Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks](https://arxiv.org/pdf/1506.01497.pdf)
2. [Deformable ConvNets v2: More Deformable, Better Results](https://arxiv.org/pdf/1811.11168.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
