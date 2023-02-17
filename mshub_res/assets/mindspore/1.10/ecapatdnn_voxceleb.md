# ecapa_tdnn

---

model-name: ecapa_tdnn

backbone-name: ecapa_tdnn

module-type: audio

fine-tunable: True

model-version: 1.10

train-dataset: voxceleb

evaluation: EER0.82

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/official/audio/ecapa_tdnn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/ecapatdnn_ascend_v1100_voxceleb_official_audio_EER0.82.ckpt>
    asset-sha256: 4b91b353611810494d9625ec54739eacbfbccc83b647bf5dac048452fe5a773a

license: Apache2.0

summary: ecapa_tdnn is used for audio

---

## Introduction

This MindSpore Hub model uses the implementation of ecapa_tdnn from the MindSpore model zoo on Gitee at official/audio/ecapa_tdnn.

ecapa_tdnn is a audio network. More details please refer to the MindSpore model zoo on Gitee at [official/audio/ecapa_tdnn](https://gitee.com/mindspore/models/blob/r1.10/official/audio/ecapa_tdnn/README.md).

All parameters in the module are trainable.

## Citation

[ECAPA-TDNN: Emphasized Channel Attention, Propagation and Aggregation in TDNN Based Speaker Verification](https://arxiv.org/pdf/2005.07143.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
