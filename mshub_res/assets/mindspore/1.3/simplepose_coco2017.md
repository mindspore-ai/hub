# simple_pose

---

model-name: simple_pose

backbone-name: simple_pose

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: coco2017

evaluation: acc70

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/official/cv/simple_pose>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/simplepose_ascend_v130_coco2017_official_cv_acc70.ckpt>
    asset-sha256: 206c944b9a756c17475c97864469cfb3c5e56b8737ecf6dccaf544b9fc75f0df

license: Apache2.0

summary: simple_pose is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of simple_pose from the MindSpore model zoo on Gitee at official/cv/simple_pose.

simple_pose is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/simple_pose](https://gitee.com/mindspore/models/blob/r1.3/official/cv/simple_pose/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.3/simplepose_coco2017"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

B. Xiao, H. Wu, and Y. Wei, “Simple baselines for human pose estimation and tracking,” in Proc. Eur. Conf. Comput. Vis., 2018, pp. 472–487.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
