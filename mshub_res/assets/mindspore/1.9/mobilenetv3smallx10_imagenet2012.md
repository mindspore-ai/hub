# mobilenetV3_small_x1_0

---

model-name: mobilenetV3_small_x1_0

backbone-name: mobilenetV3_small_x1_0

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: imagenet2012

evaluation: top1acc67 | top5acc87

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/mobilenetV3_small_x1_0>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/mobilenetv3smallx10_ascend_v190_imagenet2012_research_cv_top1acc67_top5acc87.ckpt>
    asset-sha256: 76d176503f5a18bf60b5ee0ad23f150b36306b616c5798aef4df4ff917538a5f

license: Apache2.0

summary: mobilenetV3_small_x1_0 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of mobilenetV3_small_x1_0 from the MindSpore model zoo on Gitee at research/cv/mobilenetV3_small_x1_0.

mobilenetV3_small_x1_0 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/mobilenetV3_small_x1_0](https://gitee.com/mindspore/models/blob/r1.9/research/cv/mobilenetV3_small_x1_0/README.md).

All parameters in the module are trainable.

## Citation

Howard, Andrew, Mark Sandler, Grace Chu, Liang-Chieh Chen, Bo Chen, Mingxing Tan, Weijun Wang et al."Searching for mobilenetv3."In Proceedings of the IEEE International Conference on Computer Vision, pp. 1314-1324.2019.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
