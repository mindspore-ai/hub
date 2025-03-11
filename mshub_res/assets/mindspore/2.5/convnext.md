# convnext_tiny

---

model-name: convnext_tiny

backbone-name: convnext

module-type: cv

fine-tunable: True

model-version: 2.5

train-dataset: ImageNet2012

evaluation: top1acc81.28 | top5acc95.61

author: MindSpore team

update-time: 2025-3-10

repo-link: <https://github.com/mindspore-lab/mindcv/tree/v0.4.0/configs/convnext>

user-id: MindSpore

used-for: inference

mindspore-version: 2.5

asset:

- file-format: ckpt
  asset-link: <https://download-mindspore.osinfra.cn/toolkits/mindcv/convnext/convnext_tiny-db11dc82-910v2.ckpt>
  asset-sha256: db11dc82

license: Apache2.0

summary: convnext is used for cv

---

# convnext_tiny

> [A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545)

## Introduction

In this work, the authors reexamine the design spaces and test the limits of what a pure ConvNet can achieve.
The authors gradually "modernize" a standard ResNet toward the design of a vision Transformer, and discover several key
components that contribute to the performance difference along the way. The outcome of this exploration is a family of
pure ConvNet models dubbed ConvNeXt. Constructed entirely from standard ConvNet modules, ConvNeXts compete favorably
with Transformers in terms of accuracy and scalability, achieving 87.8% ImageNet top-1 accuracy, while maintaining the
simplicity and efficiency of standard ConvNets.[[1](#references)]

<p align="center">
  <img src="https://user-images.githubusercontent.com/53842165/223907142-3bf6acfb-080a-49f5-b021-233e003318c3.png" width=250 />
</p>
<p align="center">
  <em>Figure 1. Architecture of ConvNeXt [<a href="#references">1</a>] </em>
</p>

## Results

Our reproduced model performance on ImageNet-1K is reported as follows.

<div align="center">

| Model          | Context   | Top-1 (%) | Top-5 (%) | Params (M) | Recipe                                                                                                | Download                                                                                               |
| -------------- | --------- | --------- | --------- | ---------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| convnext_tiny  | D910x64-G | 81.91     | 95.79     | 28.59      | [yaml](https://github.com/mindspore-lab/mindcv/blob/main/configs/convnext/convnext_tiny_ascend.yaml)  | [weights](https://download-mindspore.osinfra.cn/toolkits/mindcv/convnext/convnext_tiny-ae5ff8d7.ckpt)  |
| convnext_small | D910x64-G | 83.40     | 96.36     | 50.22      | [yaml](https://github.com/mindspore-lab/mindcv/blob/main/configs/convnext/convnext_small_ascend.yaml) | [weights](https://download-mindspore.osinfra.cn/toolkits/mindcv/convnext/convnext_small-e23008f3.ckpt) |
| convnext_base  | D910x64-G | 83.32     | 96.24     | 88.59      | [yaml](https://github.com/mindspore-lab/mindcv/blob/main/configs/convnext/convnext_base_ascend.yaml)  | [weights](https://download-mindspore.osinfra.cn/toolkits/mindcv/convnext/convnext_base-ee3544b8.ckpt)  |

</div>

### Notes

- Context: Training context denoted as {device}x{pieces}-{MS mode}, where mindspore mode can be G - graph mode or F - pynative mode with ms function. For example, D910x8-G is for training on 8 pieces of Ascend 910 NPU using graph mode.
- Top-1 and Top-5: Accuracy reported on the validation set of ImageNet-1K.

## Quick Start

### Preparation

#### Installation

Please refer to the [installation instruction](https://github.com/mindspore-ecosystem/mindcv#installation) in MindCV.

#### Dataset Preparation

Please download the [ImageNet-1K](https://www.image-net.org/challenges/LSVRC/2012/index.php) dataset for model training and validation.

### Training

- Distributed Training

It is easy to reproduce the reported results with the pre-defined training recipe. For distributed training on multiple Ascend 910 devices, please run

```shell
# distributed training on multiple GPU/Ascend devices
mpirun -n 8 python train.py --config configs/convnext/convnext_tiny_ascend.yaml --data_dir /path/to/imagenet
```

> If the script is executed by the root user, the `--allow-run-as-root` parameter must be added to `mpirun`.

Similarly, you can train the model on multiple GPU devices with the above `mpirun` command.

For detailed illustration of all hyper-parameters, please refer to [config.py](https://github.com/mindspore-lab/mindcv/blob/main/config.py).

**Note:** As the global batch size (batch_size x num_devices) is an important hyper-parameter, it is recommended to keep the global batch size unchanged for reproduction or adjust the learning rate linearly to a new global batch size.

- Standalone Training

If you want to train or finetune the model on a smaller dataset without distributed training, please run:

```shell
# standalone training on a CPU/GPU/Ascend device
python train.py --config configs/convnext/convnext_tiny_ascend.yaml --data_dir /path/to/dataset --distribute False
```

### Validation

To validate the accuracy of the trained model, you can use `validate.py` and parse the checkpoint path with `--ckpt_path`.

```shell
python validate.py -c configs/convnext/convnext_tiny_ascend.yaml --data_dir /path/to/imagenet --ckpt_path /path/to/ckpt
```

### Deployment

Please refer to the [deployment tutorial](https://mindspore-lab.github.io/mindcv/zh/tutorials/inference/) in MindCV.

## References

[1] Liu Z, Mao H, Wu C Y, et al. A convnet for the 2020s[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022: 11976-11986.
