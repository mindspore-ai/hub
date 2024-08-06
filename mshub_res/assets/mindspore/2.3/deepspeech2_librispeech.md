# deepspeech2

---

model-name: deepspeech2

backbone-name: deepspeech2

module-type: audio

fine-tunable: True

model-version: 2.3

train-dataset:  librispeech

evaluation: CER3.461 | WER10.24

author: MindSpore team

update-time: 2024-8-1

repo-link: <https://github.com/mindspore-lab/mindaudio/tree/v0.4.0/examples/deepspeech2>

user-id: MindSpore

used-for: inference

mindspore-version: 2.3

asset:

-
    file-format: ckpt
    asset-link: <https://download-mindspore.osinfra.cn/toolkits/mindaudio/deepspeech2/deepspeech2_70_402-531d2b5c-910v2.ckpt>
    asset-sha256: 531d2b5c

license: Apache2.0

summary: deepspeech2 is used for audio

---

## Introduction

This MindSpore Hub model uses the implementation of deepspeech2 from the MindSpore.

deepspeech2 is an audio network. More details please refer to the MindSpore-Lab on GitHub at [deepspeech2](https://github.com/mindspore-lab/mindaudio/blob/v0.4.0/examples/deepspeech2/readme.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/2.3/deepspeech2_librispeech"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](https://arxiv.org/pdf/1512.02595.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
