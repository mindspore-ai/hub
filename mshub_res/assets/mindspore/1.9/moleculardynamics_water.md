# molecular_dynamics

---

model-name: molecular_dynamics

backbone-name: molecular_dynamics

module-type: hpc

fine-tunable: True

model-version: 1.9

train-dataset: water

evaluation: -

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/hpc/molecular_dynamics>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/moleculardynamics_ascend_v190_water_research_hpc.ckpt>
    asset-sha256: 75e23f40dd5077257331f93f1d85b70aa071e843acd604a382b39590662b0b39

license: Apache2.0

summary: molecular_dynamics is used for hpc

---

## Introduction

This MindSpore Hub model uses the implementation of molecular_dynamics from the MindSpore model zoo on Gitee at research/hpc/molecular_dynamics.

molecular_dynamics is a hpc network. More details please refer to the MindSpore model zoo on Gitee at [research/hpc/molecular_dynamics](https://gitee.com/mindspore/models/blob/r1.9/research/hpc/molecular_dynamics/README.md).

All parameters in the module are trainable.

## Citation

1. [Deep Potential Molecular Dynamics: a scalable model with the accuracy of quantum mechanics](https://arxiv.org/pdf/1707.09571v2.pdf)
2. [DeePMD-kit: A deep learning package for many-body potential energy representation and molecular dynamics](https://arxiv.org/pdf/1712.03641v2.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
