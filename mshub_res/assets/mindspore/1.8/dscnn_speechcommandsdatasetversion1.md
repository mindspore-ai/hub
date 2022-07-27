# dscnn

---

model-name: dscnn

backbone-name: dscnn

module-type: audio

fine-tunable: True

model-version: 1.8

train-dataset: speechcommandsdatasetversion1

evaluation: acc93.77

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/audio/dscnn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/dscnn_ascend_v180_speechcommandsdatasetversion1_research_audio_acc93.77.ckpt>
    asset-sha256: 5d18afdd3ffe3e9ec179392a66dc3d36cc1af63521e44bd60b70aed6a29c08a5

license: Apache2.0

summary: dscnn is used for audio

---

## Introduction

This MindSpore Hub model uses the implementation of dscnn from the MindSpore model zoo on Gitee at research/audio/dscnn.

dscnn is a audio network. More details please refer to the MindSpore model zoo on Gitee at [research/audio/dscnn](https://gitee.com/mindspore/models/blob/r1.8/research/audio/dscnn/README.md).

All parameters in the module are trainable.

## Citation

Zhang, Yundong, Naveen Suda, Liangzhen Lai, and Vikas Chandra. "Hello edge: Keyword spotting on microcontrollers." arXiv preprint arXiv:1711.07128 (2017).

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
