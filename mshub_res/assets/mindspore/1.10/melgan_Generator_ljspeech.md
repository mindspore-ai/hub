# melgan

---

model-name: melgan

backbone-name: melgan

module-type: audio

fine-tunable: True

model-version: 1.10

train-dataset: ljspeech

evaluation: 3.2mos

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/official/audio/melgan>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/melgan_Generator_ascend_v1100_ljspeech_official_audio_3.2mos.ckpt>
    asset-sha256: 2cd5e14bd200a5c87f1277382e209d887012d240c390c14690f708bc61ade819

license: Apache2.0

summary: melgan is used for audio

---

## Introduction

This MindSpore Hub model uses the implementation of melgan from the MindSpore model zoo on Gitee at official/audio/melgan.

melgan is a audio network. More details please refer to the MindSpore model zoo on Gitee at [official/audio/melgan](https://gitee.com/mindspore/models/blob/r1.10/official/audio/melgan/README.md).

All parameters in the module are trainable.

## Citation

[MelGAN: Generative Adversarial Networks for Conditional Waveform Synthesis](https://arxiv.org/pdf/1910.06711.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
