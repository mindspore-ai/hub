# wide_and_deep_multitable

---

model-name: wide_and_deep_multitable

backbone-name: wide_and_deep_multitable

module-type: recommend

fine-tunable: True

model-version: 1.9

train-dataset: outbrain

evaluation: acc80.97

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/recommend/wide_and_deep_multitable>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/wideanddeepmultitable_ascend_v190_outbrain_official_recommend_acc80.97.ckpt>
    asset-sha256: dfbee3851427816f19ced062e7318c0080bafd5e68db4772c718047dceea0b10

license: Apache2.0

summary: wide_and_deep_multitable is used for recommend

---

## Introduction

This MindSpore Hub model uses the implementation of wide_and_deep_multitable from the MindSpore model zoo on Gitee at official/recommend/wide_and_deep_multitable.

wide_and_deep_multitable is a recommend network. More details please refer to the MindSpore model zoo on Gitee at [official/recommend/wide_and_deep_multitable](https://gitee.com/mindspore/models/blob/r1.9/official/recommend/wide_and_deep_multitable/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.9/wideanddeepmultitable_outbrain"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[Wide & Deep Learning for Recommender System](https://arxiv.org/pdf/1606.07792.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
