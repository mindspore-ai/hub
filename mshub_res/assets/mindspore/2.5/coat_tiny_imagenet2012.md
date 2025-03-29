# coat_tiny

---

model-name: coat_tiny

backbone-name: coat

module-type: cv

fine-tunable: True

model-version: 2.5

train-dataset: ImageNet2012

evaluation: top1acc79.28 | top5acc94.45

author: MindSpore team

update-time: 2025-03-10

repo-link: <https://github.com/mindspore-lab/mindcv/tree/v0.5.0/configs/coat>

user-id: MindSpore

used-for: inference

mindspore-version: 2.5

asset:

- file-format: ckpt
  asset-link: <https://download-mindspore.osinfra.cn/toolkits/mindcv/coat/coat_tiny-dcca16b1-910v2.ckpt>
  asset-sha256: dcca16b1

license: Apache2.0

summary: coat is used for cv

---

# CoaT

> [Co-Scale Conv-Attentional Image Transformers](https://arxiv.org/abs/2104.06399v2)

## Requirements

| mindspore | ascend driver |  firmware   | cann toolkit/kernel |
| :-------: | :-----------: | :---------: | :-----------------: |
|   2.5.0   |    24.1.0     | 7.5.0.3.220 |     8.0.0.beta1     |

## Introduction

Co-Scale Conv-Attentional Image Transformer (CoaT) is a Transformer-based image classifier equipped with co-scale and conv-attentional mechanisms. First, the co-scale mechanism maintains the integrity of Transformers' encoder branches at individual scales, while allowing representations learned at different scales to effectively communicate with each other. Second, the conv-attentional mechanism is designed by realizing a relative position embedding formulation in the factorized attention module with an efficient convolution-like implementation. CoaT empowers image Transformers with enriched multi-scale and contextual modeling capabilities.

## Performance

Our reproduced model performance on ImageNet-1K is reported as follows.

Experiments are tested on ascend 910\* with mindspore 2.5.0 graph mode.

_coming soon_

### Notes

- top-1 and top-5: Accuracy reported on the validation set of ImageNet-1K.

## Quick Start

### Preparation

#### Installation

Please refer to the [installation instruction](https://mindspore-lab.github.io/mindcv/installation/) in MindCV.

#### Dataset Preparation

Please download the [ImageNet-1K](https://www.image-net.org/challenges/LSVRC/2012/index.php) dataset for model training and validation.

### Training

- Distributed Training

  It is easy to reproduce the reported results with the pre-defined training recipe. For distributed training on multiple Ascend 910 devices, please run

  ```shell
  # distributed training on multiple NPU devices
  msrun --bind_core=True --worker_num 8 python train.py --config configs/coat/coat_lite_tiny_ascend.yaml --data_dir /path/to/imagenet
  ```

  For detailed illustration of all hyper-parameters, please refer to [config.py](https://github.com/mindspore-lab/mindcv/blob/main/config.py).

  **Note:** As the global batch size (batch_size x num_devices) is an important hyper-parameter, it is recommended to keep the global batch size unchanged for reproduction or adjust the learning rate linearly to a new global batch size.

- Standalone Training

  If you want to train or finetune the model on a smaller dataset without distributed training, please run:

  ```shell
  # standalone training on single NPU device
  python train.py --config configs/coat/coat_lite_tiny_ascend.yaml --data_dir /path/to/dataset --distribute False
  ```

### Validation

To validate the accuracy of the trained model, you can use `validate.py` and parse the checkpoint path with `--ckpt_path`.

```shell
python validate.py -c configs/coat/coat_lite_tiny_ascend.yaml --data_dir /path/to/imagenet --ckpt_path /path/to/ckpt
```

## References

[1] Han D, Yun S, Heo B, et al. Rethinking channel dimensions for efficient model design[C]//Proceedings of the IEEE/CVF conference on Computer Vision and Pattern Recognition. 2021: 732-741.
