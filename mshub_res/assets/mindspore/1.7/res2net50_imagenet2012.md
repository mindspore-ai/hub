# res2net50

---

model-name: res2net50

backbone-name: res2net

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: imagenet2012

evaluation: top1acc78 | top5acc94

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/research/cv/res2net>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/res2net50_ascend_v170_imagenet2012_research_cv_top1acc78_top5acc94.ckpt>
    asset-sha256: 38aef446135e0e4afd02b64f4dd2ff208830c735c4332402a7c4ce741bb7fb0d

license: Apache2.0

summary: res2net is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of res2net from the MindSpore model zoo on Gitee at research/cv/res2net.

res2net is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/res2net](https://gitee.com/mindspore/models/blob/r1.7/research/cv/res2net/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.7/res2net50_imagenet2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Gao, Shang-Hua and Cheng, Ming-Ming and Zhao, Kai and Zhang, Xin-Yu and Yang, Ming-Hsuan and Torr, Philip. "Res2Net: A New Multi-scale Backbone Architecture"，TPAMI21

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
