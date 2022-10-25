# tacotron2

---

model-name: tacotron2

backbone-name: tacotron2

module-type: audio

fine-tunable: True

model-version: 1.9

train-dataset: LJSpeech-1.1

evaluation: -

author: MindSpore team

update-time: 2022-10-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/audio/tacotron2>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/tacotron2_ascend_v190_ljspeech11_official_audio.ckpt>
    asset-sha256: d787066f14f9465676d5c3260221d4ff251a56909744bed6862c062f77ece26d

license: Apache2.0

summary: tacotron2 is used for audio

---

## Introduction

This MindSpore Hub model uses the implementation of tacotron2 from the MindSpore model zoo on Gitee at official/audio/tacotron2.

tacotron2 is a audio network. More details please refer to the MindSpore model zoo on Gitee at [official/audio/tacotron2](https://gitee.com/mindspore/models/blob/r1.9/official/audio/tacotron2/README.md).

All parameters in the module are trainable.

## Citation

[NATURAL TTS SYNTHESIS BY CONDITIONING WAVENET ON MEL SPECTROGRAM PREDICTIONS](https://arxiv.org/pdf/1712.05884.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
