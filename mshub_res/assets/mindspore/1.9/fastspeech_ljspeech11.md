# FastSpeech

---

model-name: FastSpeech

backbone-name: FastSpeech

module-type: audio-TTS

fine-tunable: True

model-version: 1.9

train-dataset: LJSpeech-1.1

evaluation: Frechet203.9 | Kernel0.0239

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/audio/FastSpeech>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/fastspeech_ascend_v190_ljspeech11_research_audio_Frechet203.9_Kernel0.0239.ckpt>
    asset-sha256: 0671311718e41aae5d14b16ca938187b1a690c6d5dce047693b3e022f550a183

license: Apache2.0

summary: FastSpeech is used for audio

---

## Introduction

This MindSpore Hub model uses the implementation of FastSpeech from the MindSpore model zoo on Gitee at research/audio/FastSpeech.

FastSpeech is a audio network. More details please refer to the MindSpore model zoo on Gitee at [research/audio/FastSpeech](https://gitee.com/mindspore/models/blob/r1.9/research/audio/FastSpeech/README.md).

All parameters in the module are trainable.

## Citation

[FastSpeech: Fast, Robust and Controllable Text to Speech](https://arxiv.org/pdf/1905.09263v5.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
