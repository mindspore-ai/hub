# TNT

---

model-name: TNT

backbone-name: TNT

module-type: cv-classification

fine-tunable: True

input-shape: [384, 384, 3]

model-version: 1.0

train-dataset: Oxford-IIIT Pet

accuracy: 95.0

author: Noah's Ark Lab

update-time: 2021-03-24

repo-link: <https://gitee.com/mindspore/models/tree/master/research/cv/TNT>

user-id: noah-cvlab

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-version: 1.1

mindspore-lite: False

asset:

- file-format: ckpt

  asset-link: <https://download.mindspore.cn/model_zoo/research/cv/TNT/tnt_b_pets.ckpt>

  asset-sha256: 73d333605ccf10c93243af1e64318498792dc175c2b7ba96f844b512f0ae6f75

license: Apache2.0

summary: Transformer in Transformer (TNT) model for visual recognition

---

## Introduction

This MindSpore Hub model uses the implementation of TNT from the MindSpore model zoo on Gitee at model_zoo/research/cv/TNT.

## Usage

```python
import mindspore_hub as mshub

from mindspore import context

from src.args import args

context.set_context(mode=context.PYNATIVE_MODE,
                    device_target="GPU",
                    device_id=0)

model = "noah-cvlab/gpu/1.1/tnt_v1.0_oxford_pets"
network = mshub.load(model, args)

network.set_train(False)
```

## Citation

[1] Kai Han, An Xiao, Enhua Wu, Jianyuan Guo, Chunjing Xu, Yunhe Wang. Transformer in Transformer. preprint 2021.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.