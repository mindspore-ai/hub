# CNN&CTC

---

model-name: cnnctc

backbone-name: resnet50

module-type: cv

fine-tunable: True

input-shape: [32, 100, 3]

model-version: 1.1

train-dataset: MJSynth

accuracy: 0.85

author: MindSpore team

update-time: 2021-4-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/cnnctc>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/cnnctc_ascend_v111_offical_cv_bs192_acc85/cnnctc_ascend_v111_offical_cv_bs192_acc85.ckpt>
    asset-sha256: c6a340120565c3b93ed7e63a9bc2a69428510000051338f4ae0f6b66ea4623dd

license: Apache2.0

summary: cnnctc used to test detection of MJSyncth and SynthText

---

## Introduction

This MindSpore Hub model uses the implementation of cnnctc from the MindSpore model zoo on Gitee at model_zoo/official/cv/cnnctc.

cnnctc is a audio network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/cnnctc](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/cnnctc/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/cnnctc_v1.1"

network = mshub.load(model)
network.set_train(False)

```

## Citation

Paper: J. Baek, G. Kim, J. Lee, S. Park, D. Han, S. Yun, S. J. Oh, and H. Lee, “What is wrong with scene text recognition model comparisons? dataset and model analysis,” ArXiv, vol. abs/1904.01906, 2019.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.