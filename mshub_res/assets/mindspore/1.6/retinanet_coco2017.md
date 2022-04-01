# retinanet

---

model-name: retinanet

backbone-name: retinanet

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: coco2017

evaluation: acc35

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/official/cv/retinanet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/retinanet_ascend_v160_coco2017_official_cv_acc35.ckpt>
    asset-sha256: 2fda03174122089d884f7fde4115d51145a25d44cca6f9c02f0653a83d17cab6

license: Apache2.0

summary: retinanet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of retinanet from the MindSpore model zoo on Gitee at official/cv/retinanet.

retinanet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/retinanet](https://gitee.com/mindspore/models/blob/r1.6/official/cv/retinanet/README_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.6/retinanet_coco2017"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Lin T Y , Goyal P , Girshick R , et al. Focal Loss for Dense Object Detection[C]// 2017 IEEE International Conference on Computer Vision (ICCV). IEEE, 2017:2999-3007.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
