# lpcnet

---

model-name: lpcnet

backbone-name: lpcnet

module-type: audio

fine-tunable: True

model-version: 1.6

train-dataset: librispeech

evaluation: MSE0.34

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/official/audio/lpcnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/lpcnet_ascend_v160_librispeech_official_audio_MSE0.34.ckpt>
    asset-sha256: 1b0912d8944ad2a817100caf798b415e628a1a7348bd554498fe7262cd8f6a29

license: Apache2.0

summary: lpcnet is used for audio

---

## Introduction

This MindSpore Hub model uses the implementation of lpcnet from the MindSpore model zoo on Gitee at official/audio/lpcnet.

lpcnet is a audio network. More details please refer to the MindSpore model zoo on Gitee at [official/audio/lpcnet](https://gitee.com/mindspore/models/blob/r1.6/official/audio/lpcnet/README.md).

All parameters in the module are trainable.

## Citation

J.-M. Valin, J. Skoglund, A Real-Time Wideband Neural Vocoder at 1.6 kb/s Using LPCNet, Proc. INTERSPEECH, arxiv:1903.12087, 2019.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
