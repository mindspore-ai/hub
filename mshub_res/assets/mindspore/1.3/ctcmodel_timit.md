# ctcmodel

---

model-name: ctcmodel

backbone-name: ctcmodel

module-type: audio

fine-tunable: True

model-version: 1.3

train-dataset: timit

evaluation: bestpathLER30.38 | prefixsearchLER30.05

author: MindSpore team

update-time: 2022-04-24

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/audio/ctcmodel>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/ctcmodel_ascend_v130_timit_research_audio_bestpathLER30.38_prefixsearchLER30.05.ckpt>
    asset-sha256: 761c07b1d379ccd020690788dcbc54bcac9ea25662ab412711c8e5042f672569

license: Apache2.0

summary: ctcmodel is used for audio

---

## Introduction

This MindSpore Hub model uses the implementation of ctcmodel from the MindSpore model zoo on Gitee at research/audio/ctcmodel.

ctcmodel is a audio network. More details please refer to the MindSpore model zoo on Gitee at [research/audio/ctcmodel](https://gitee.com/mindspore/models/blob/r1.3/research/audio/ctcmodel/README_CN.md).

All parameters in the module are trainable.

## Citation

Alex Graves, Santiago Fernández, Faustino J. Gomez, Jürgen Schmidhuber: Connectionist temporal classification: labelling unsegmented sequence data with recurrent neural networks. ICML 2006: 369-376

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
