# deepfm

---

model-name: deepfm

backbone-name: deepfm

module-type: recommend

fine-tunable: True

input-shape: [[1000, 39], [1000, 39]]

model-version: 1.1

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/recommend/deepfm>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/deepfm_ascend_v111_criteio_offical_recommend_bs16000_acc80/deepfm_ascend_v111_criteio_offical_recommend_bs16000_acc80.ckpt>
    asset-sha256: 4b42ca5e470ff027a739d402f58422386887002dccd9abae70731ec10658b758

license: Apache2.0

summary: deepfm used in recommend system

---

## Introduction

This MindSpore Hub model uses the implementation of deepfm from the MindSpore model zoo on Gitee at model_zoo/official/recommend/deepfm.

deepfm is a recommend network. More details please refer to the MindSpore model zoo on Gitee [model_zoo/official/recommend/deepfm](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/recommend/deepfm/README.md).

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

model = "mindspore/ascend/1.1/deepfm_v1.1"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Huifeng Guo, Ruiming Tang, Yunming Ye, Zhenguo Li, Xiuqiang He. DeepFM: A Factorization-Machine based Neural Network for CTR Prediction.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.