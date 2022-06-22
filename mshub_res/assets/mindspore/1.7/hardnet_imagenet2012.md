# hardnet

---

model-name: hardnet

backbone-name: hardnet

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: imagenet2012

evaluation: top1acc77.65 | top5acc93.27

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/research/cv/hardnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/hardnet_ascend_v170_imagenet2012_research_cv_top1acc77.65_top5acc93.27.ckpt>
    asset-sha256: 299aad036e2bab5a7dc97b621756b9a0985e2ecb03e26ff7492565c655ce7dc9

license: Apache2.0

summary: hardnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of hardnet from the MindSpore model zoo on Gitee at research/cv/hardnet.

hardnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/hardnet](https://gitee.com/mindspore/models/blob/r1.7/research/cv/hardnet/README_CN.md).

All parameters in the module are trainable.

## Citation

Chao P , Kao C Y , Ruan Y , et al. HarDNet: A Low Memory Traffic Network[C]// 2019 IEEE/CVF International Conference on Computer Vision (ICCV). IEEE, 2020.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
