# siamRPN

---

model-name: siamRPN

backbone-name: siamRPN

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: vid

evaluation: vot2015acc59.59 | vot2015robustness32.16 | vot2015eao31.69 | vot2016acc56.48 | vot2016robustness34.49 | vot2016eao29.91

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/siamRPN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/siamrpn_ascend_v190_vid_research_cv_vot2015acc59.59_vot2015robustness32.16_vot2015eao31.69_vot2016acc56.48_vot2016robustness34.49_vot2016eao29.91.ckpt>
    asset-sha256: 7a7dc5779cdbcc40ccb5cda33810b745600b8c4f10b22c4687b3512e5a30e065

license: Apache2.0

summary: siamRPN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of siamRPN from the MindSpore model zoo on Gitee at research/cv/siamRPN.

siamRPN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/siamRPN](https://gitee.com/mindspore/models/blob/r1.9/research/cv/siamRPN/README_CN.md).

All parameters in the module are trainable.

## Citation

[High Performance Visual Tracking with Siamese Region Proposal Network](https://openaccess.thecvf.com/content_cvpr_2018/papers/Li_High_Performance_Visual_CVPR_2018_paper.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
