# mobilenetv3_large

---

model-name: mobilenetv3_large

backbone-name: mobilenetv3_large

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: imagenet2012

evaluation: top1acc74.55 | top5acc91.76

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/mobilenetv3_large>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/mobilenetv3large_ascend_v160_imagenet2012_research_cv_top1acc74.55_top5acc91.76.ckpt>
    asset-sha256: 7f979e6256886df0070f9f4286ec0b32f21119b1430a127afddefeb10dd7bc31

license: Apache2.0

summary: mobilenetv3_large is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of mobilenetv3_large from the MindSpore model zoo on Gitee at research/cv/mobilenetv3_large.

mobilenetv3_large is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/mobilenetv3_large](https://gitee.com/mindspore/models/blob/r1.6/research/cv/mobilenetv3_large/README_CN.md).

All parameters in the module are trainable.

## Citation

Howard, Andrew, Mark Sandler, Grace Chu, Liang-Chieh Chen, Bo Chen, Mingxing Tan, Weijun Wang et al."Searching for mobilenetv3."In Proceedings of the IEEE International Conference on Computer Vision, pp. 1314-1324.2019.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
