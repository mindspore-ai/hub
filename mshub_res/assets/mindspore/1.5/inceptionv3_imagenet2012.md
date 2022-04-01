# inceptionv3

---

model-name: inceptionv3

backbone-name: inceptionv3

module-type: cv

fine-tunable: True

model-version: 1.5

train-dataset: imagenet2012

evaluation: top1acc78.69 | top5acc94.3

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/official/cv/inceptionv3>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/inceptionv3_ascend_v150_imagenet2012_official_cv_top1acc78.69_top5acc94.3.ckpt>
    asset-sha256: c3b6bd7fb0394255d8d96fde238face46e79b6a3a130c9a71135a1d8552536b4

license: Apache2.0

summary: inceptionv3 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of inceptionv3 from the MindSpore model zoo on Gitee at official/cv/inceptionv3.

inceptionv3 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/inceptionv3](https://gitee.com/mindspore/models/blob/r1.5/official/cv/inceptionv3/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.5/inceptionv3_imagenet2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Min Sun, Ali Farhadi, Steve Seitz. Ranking Domain-Specific Highlights by Analyzing Edited Videos[J]. 2014.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
