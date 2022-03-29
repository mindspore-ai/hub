# SiamFC

---

model-name: SiamFC

backbone-name: SiamFC

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: ilsvrc2015vid

evaluation: acc58.6

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/cv/SiamFC>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/siamfc_ascend_v130_ilsvrc2015vid_research_cv_acc58.6.ckpt>
    asset-sha256: 082586450b38aa49f4794fde27bb1368d65a515f9e9549ef78a37d74ff7e36aa

license: Apache2.0

summary: SiamFC is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of SiamFC from the MindSpore model zoo on Gitee at research/cv/SiamFC.

SiamFC is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/SiamFC](https://gitee.com/mindspore/models/blob/r1.3/research/cv/SiamFC/README.md).

All parameters in the module are trainable.

## Citation

Luca Bertinetto Jack Valmadre Jo˜ao F. Henriques Andrea Vedaldi Philip H. S. Torr Department of Engineering Science, University of Oxford

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
