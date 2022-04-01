# emotect

---

model-name: emotect

backbone-name: emotect

module-type: nlp

fine-tunable: True

model-version: 1.5

train-dataset: baidu

evaluation: acc90.44

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/official/nlp/emotect>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/emotect_ascend_v150_baidu_official_nlp_acc90.44.ckpt>
    asset-sha256: 5b0ddb04f17f27d706007353d15faf93b627dcaf0ce7fcfcf1b61d4f2ddc228b

license: Apache2.0

summary: emotect is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of emotect from the MindSpore model zoo on Gitee at official/nlp/emotect.

emotect is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [official/nlp/emotect](https://gitee.com/mindspore/models/blob/r1.5/official/nlp/emotect/README_CN.md).

All parameters in the module are trainable.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
