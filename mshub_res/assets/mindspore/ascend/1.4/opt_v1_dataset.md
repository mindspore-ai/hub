# OPT

---

model-name: OPT

backbone-name: BertModel

module-type: cross-modal Understanding and Generation

fine-tunable: True

input-shape: [90, 2048]

model-version: 1.0

pretrain-dataset: CC3M, COCO Captions, AIC. We translate English captions into Chinese.

retrieval-dataset: COCO Captions

caption-dataset: COCO Captions

accuracy:  0.00

author: casia iva team

update-time: 2021-12-2

repo-link:  

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

asset:  

-
    file-format: ckpt  
    asset-link:
    asset-sha256:

license: Apache2.0

summary: OPT used for Cross-Modal Understanding and Generation.

---

## Introduction

This MindSpore Hub model uses the implementation of OPT from the MindSpore model zoo on Gitee at model_zoo/.

This model has been pretrained on cc3m, coco and aic using the code published on Gitee and finetune.

All Parameters in the module are trainable.

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

model = "mindspore/ascend/1.0/"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Liu J, Zhu X, Liu F, et al. OPT: Omni-Perception Pre-Trainer for Cross-Modal Understanding and Generation[J]. arXiv preprint arXiv:2107.00249, 2021.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.