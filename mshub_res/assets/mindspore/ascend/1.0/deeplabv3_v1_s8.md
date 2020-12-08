# DeepLabv3

---

model-name: DeepLab_v3_s8

backbone-name: Resnet101

module-type: cv-semantic_segmentation

fine-tunable: True

input-shape: [897, 897, 3]

model-version: 1.0

accuracy: 0.798

author: MindSpore team

update-time: 2020-09-04

repo-link: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/deeplabv3>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

license: Apache2.0

summary: DeepLabv3 used to image semantic segmentation

---

## Introduction

This MindSpore Hub model uses the implementation of DeepLabv3 from the MindSpore model zoo on Gitee at model_zoo/official/cv/deeplabv3.

All Parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
model = "mindspore/ascend/1.0/deeplabv3_v1"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, pretrained=False, num_classes=21)
#...
```

Refer to the readme description of modelzoo for specific usage: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/deeplabv3>

## Citation

1. Chen L C, Papandreou G, Schroff F, et al. Rethinking atrous convolution for semantic image segmentation[J]. arXiv preprint arXiv:1706.05587, 2017.
