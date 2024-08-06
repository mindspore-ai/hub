# conformer

---

model-name: conformer

backbone-name: conformer

module-type: audio

fine-tunable: True

model-version: 2.3

train-dataset: AISHELL-1

evaluation: ctc greedy search CER5.62 | ctc prefix beam search CER5.62 | attention rescoring CER5.12

author: MindSpore team

update-time: 2024-8-1

repo-link: <https://github.com/mindspore-lab/mindaudio/tree/v0.4.0/examples/conformer>

user-id: MindSpore

used-for: inference

mindspore-version: 2.3

asset:

-
    file-format: ckpt
    asset-link: <https://download-mindspore.osinfra.cn/toolkits/mindaudio/conformer/conformer_avg_30-692d57b3-910v2.ckpt>
    asset-sha256: 692d57b3

license: Apache2.0

summary: conformer is used for audio

---

## Introduction

This MindSpore Hub model uses the implementation of conformer from the MindSpore.

conformer is an audio network. More details please refer to the MindSpore-Lab on GitHub at [conformer](https://github.com/mindspore-lab/mindaudio/blob/v0.4.0/examples/conformer/readme.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/2.3/conformer_aishell"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/pdf/2005.08100.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
