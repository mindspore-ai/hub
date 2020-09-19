# GhostNet

---

model-name: GhostNet

backbone-name: GhostNet

module-type: CV-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.0

train-dataset: Oxford-IIIT Pet

accuracy: 0.824


author: Noah CVLab

update-time: 2020-09-08

repo-link: https://gitee.com/mindspore/mindspore/tree/master/model_zoo/research/cv/ghostnet

user-id: noah-cvlab

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-version: 1.0

asset:
  -
    file-format: ckpt
    asset-link: https://download.mindspore.cn/model_zoo/research/cv/ghostnet/ghostnet_1x_pets.ckpt
    asset-sha256: 722e13be6cd6186dddcd68d5c0a50776d9a8ad8e79db3870556f68d4d2f179e4

license: Apache2.0

summary: AlexNet used to classify 37 classes of Oxford-IIIT Pet

---


## Introduction

This MindSpore Hub model uses the implementation of GhostNet from the MindSpore model zoo on Gitee at model_zoo/official/cv/ghostnet.


### Performance

#### GhostNet on ImageNet2012
| Parameters                 |                                        |   |
| -------------------------- | -------------------------------------- |---------------------------------- |
| Model Version              | GhostNet                                             |GhostNet-600|
| uploaded Date              | 09/08/2020 (month/day/year)  ；                        | 09/08/2020 (month/day/year) |
| Dataset                    | ImageNet2012                                                    | ImageNet2012|
| Parameters (M)             | 5.2                                                   | 11.9 |
| FLOPs (M) | 142 | 591 |
| Accuracy (Top1) | 73.9 |80.2   |

#### GhostNet on Oxford-IIIT Pet

| Parameters                 |                                        |   |
| -------------------------- | -------------------------------------- |---------------------------------- |
| Model Version              | GhostNet                                             |GhostNet-600|
| uploaded Date              | 09/08/2020 (month/day/year)  ；                        | 09/08/2020 (month/day/year) |
| Dataset                    | Oxford-IIIT Pet                                                   | Oxford-IIIT Pet|
| Parameters (M)             | 3.9                                                    | 10.6 |
| FLOPs (M) | 140 | 590 |
| Accuracy (Top1) |            82.4              |86.9   |

#### Comparison with other methods on Oxford-IIIT Pet

| Model           | FLOPs (M) | Latency (ms)* | Accuracy (Top1) |
| --------------- | --------- | ------------- | --------------- |
| MobileNetV2-1x  | 300       | 28.2          | 78.5            |
| Ghost-1x w\o SE | 138       | 19.1          | 81.1            |
| Ghost-1x        | 140       | 25.3          | 82.4            |
| Ghost-600       | 590       | -             | 86.9            |

*The latency is measured on Huawei Kirin 990 chip under single-threaded mode with batch size 1.

## Usage

```python
import mindspore_hub as mshub

from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="GPU",
                    device_id=0)

model = "noah-cvlab/gpu/1.0/ghostnet_v1.0_oxford_pets"
network = mshub.load(model, num_classes=37)

network.set_train(False)
```

## Citation

1. Kai Han, Yunhe Wang, Qi Tian, Jianyuan Guo, Chunjing Xu, Chang Xu; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2020, pp. 1580-1589