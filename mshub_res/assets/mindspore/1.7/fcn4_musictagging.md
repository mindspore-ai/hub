# fcn-4

---

model-name: fcn-4

backbone-name: fcn-4

module-type: audio

fine-tunable: True

model-version: 1.7

train-dataset: musictagging

evaluation: acc90.89

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/research/audio/fcn-4>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/fcn4_ascend_v170_musictagging_research_audio_acc90.89.ckpt>
    asset-sha256: bdb7116d2dc25ae80381a882b9d8a75f857e53a920561015e3a9245cf469d284

license: Apache2.0

summary: fcn-4 is used for audio

---

## Introduction

This MindSpore Hub model uses the implementation of fcn-4 from the MindSpore model zoo on Gitee at research/audio/fcn-4.

fcn-4 is a audio network. More details please refer to the MindSpore model zoo on Gitee at [research/audio/fcn-4](https://gitee.com/mindspore/models/blob/r1.7/research/audio/fcn-4/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.7/fcn4_musictagging"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

"Keunwoo Choi, George Fazekas, and Mark Sandler, “Automatic tagging using deep convolutional neural networks,” in International Society of Music Information Retrieval Conference. ISMIR, 2016."

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
