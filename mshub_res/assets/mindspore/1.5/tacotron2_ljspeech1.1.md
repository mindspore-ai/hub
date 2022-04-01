# tacotron2

---

model-name: tacotron2

backbone-name: tacotron2

module-type: audio

fine-tunable: True

model-version: 1.5

train-dataset: ljspeech1.1

evaluation: -

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/research/audio/tacotron2>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/tacotron2_ascend_v150_ljspeech1.1_research_audio.ckpt>
    asset-sha256: 12176c49d868e86841b96f9f6517f1e28287a203ec67137b76d59bfdc1e19a62

license: Apache2.0

summary: tacotron2 is used for audio

---

## Introduction

This MindSpore Hub model uses the implementation of tacotron2 from the MindSpore model zoo on Gitee at research/audio/tacotron2.

tacotron2 is a audio network. More details please refer to the MindSpore model zoo on Gitee at [research/audio/tacotron2](https://gitee.com/mindspore/models/blob/r1.5/research/audio/tacotron2/README.md).

All parameters in the module are trainable.

## Citation

Jonathan, et al. Natural TTS Synthesis by Conditioning WaveNet on Mel Spectrogram Predictions.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
