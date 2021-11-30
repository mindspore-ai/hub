# FCN-4

---

model-name: fcn4

backbone-name: fcn4

module-type: audio

fine-tunable: True

input-shape: [[1, 128], [1, 128], [1, 128]]

model-version: 1.1

train-dataset: MagnaTagATune

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/research/audio/fcn-4>

user-id: MindSpore

used-for: inference/transfer-learning

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

  -
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/fcn4_ascend_v111_musictag_research_audio_bs32_acc90/fcn4_ascend_v111_musictag_research_audio_bs32_acc90.ckpt>
    asset-sha256: 52f8bbab81c969835f1d85c6f310b6bce916f7133e1e5d27b67cbdee6229b643

license: Apache2.0

summary: FCN-4 is a convolutional neural network architecture, its name FCN-4 comes from the fact that it has 4 layers. Its layers consists of Convolutional layers, Max Pooling layers, Activation layers, Fully connected layers.

---

## Introduction

This MindSpore Hub model uses the implementation of fcn-4 from the MindSpore model zoo on Gitee at model_zoo/research/audio/fcn-4.

fcn-4 is a audio network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/audio/fcn-4](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/research/audio/fcn-4/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/fcn4_v1.1"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, in_classes=[1, 128, 384, 768, 2048],
                            kernel_size=[3, 3, 3, 3, 3],
                            padding=[0] * 5,
                            maxpool=[(2, 4), (4, 5), (3, 8), (4, 8)],
                            has_bias=True)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

Paper: "Keunwoo Choi, George Fazekas, and Mark Sandler, “Automatic tagging using deep convolutional neural networks,” in International Society of Music Information Retrieval Conference. ISMIR, 2016."

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.