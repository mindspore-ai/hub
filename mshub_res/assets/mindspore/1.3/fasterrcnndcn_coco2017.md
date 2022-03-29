# faster_rcnn_dcn

---

model-name: faster_rcnn_dcn

backbone-name: faster_rcnn_dcn

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: coco2017

evaluation: acc40.2

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/cv/faster_rcnn_dcn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/fasterrcnndcn_ascend_v130_coco2017_research_cv_acc40.2.ckpt>
    asset-sha256: 5f78ead585bb3772c49afcd525ac2f696819eea5864c33054ebd6cdf7eae3226

license: Apache2.0

summary: faster_rcnn_dcn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of faster_rcnn_dcn from the MindSpore model zoo on Gitee at research/cv/faster_rcnn_dcn.

faster_rcnn_dcn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/faster_rcnn_dcn](https://gitee.com/mindspore/models/blob/r1.3/research/cv/faster_rcnn_dcn/README_CN.md).

All parameters in the module are trainable.

## Citation

Ren S , He K , Girshick R , et al. Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks[J]. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2015, 39(6).

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
