# DeepLabv3

---

model-name: DeepLab_v3_s8

backbone-name: Resnet101

module-type: cv-semantic_segmentation

fine-tunable: True

input-shape: [897, 897, 3]

model-version: 1.1

train-dataset: voc2012

accuracy: 0.798

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/deeplabv3>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

- file-format: ckpt  
  asset-link: <https://download.mindspore.cn/model_zoo/r1.1/deeplabv3s8r2_ascend_v111_voc2012_offical_cv_bs16_s8acc78/deeplabv3s8r2_ascend_v111_voc2012_offical_cv_bs16_s8acc78.ckpt>
  asset-sha256: a6c45f9be25ba1f8c98c754eeab23704a03576b0d9ba7e5913f37a1409b0bcea

license: Apache2.0

summary: DeepLabv3 used to image semantic segmentation

---

## Introduction

This MindSpore Hub model uses the implementation of DeepLabv3 from the MindSpore model zoo on Gitee at [model_zoo/official/cv/deeplabv3](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/deeplabv3/README.md).

All Parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
model = "mindspore/ascend/1.1/DeepLab_v3_s8_v1.1_voc2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, pretrained=False, num_classes=21)
#...
```

Refer to the readme description of modelzoo for specific usage: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/deeplabv3>

## Citation

1. Chen L C, Papandreou G, Schroff F, et al. Rethinking atrous convolution for semantic image segmentation[J]. arXiv preprint arXiv:1706.05587, 2017.
