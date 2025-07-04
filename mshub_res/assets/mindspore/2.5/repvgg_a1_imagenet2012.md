# repvgg_a1

---

model-name: repvgg_a1

backbone-name: repvgg

module-type: cv

fine-tunable: True

model-version: 2.5

train-dataset: ImageNet2012

evaluation: top1acc73.68 | top5acc91.51

author: MindSpore team

update-time: 2025-03-10

repo-link: <https://github.com/mindspore-lab/mindcv/tree/v0.5.0/configs/repvgg>

user-id: MindSpore

used-for: inference

mindspore-version: 2.5

asset:

- file-format: ckpt
  asset-link: <https://download-mindspore.osinfra.cn/toolkits/mindcv/repvgg/repvgg_a1-a40aa623-910v2.ckpt>
  asset-sha256: a40aa623

license: Apache2.0

summary: repvgg is used for cv

---

# RepVGG

<!--- Guideline: please use url linked to the paper abstract in ArXiv instead of PDF for fast loading.  -->

> [RepVGG: Making VGG-style ConvNets Great Again](https://arxiv.org/abs/2101.03697)

## Requirements

| mindspore | ascend driver |  firmware   | cann toolkit/kernel |
| :-------: | :-----------: | :---------: | :-----------------: |
|   2.5.0   |    24.1.0     | 7.5.0.3.220 |     8.0.0.beta1     |

## Introduction

<!--- Guideline: Introduce the model and architectures. Please cite if you use/adopt paper explanation from others. -->
<!--- Guideline: If an architecture table/figure is available in the paper, please put one here and cite for intuitive illustration. -->

The key idea of Repvgg is that by using re-parameterization, the model architecture could be trained in multi-branch but
validated in single branch.
Figure 1 shows the basic model architecture of Repvgg. By utilizing different values for a and b, we could get various
repvgg models.
Repvgg could achieve better model performance with smaller model parameters on ImageNet-1K dataset compared with
previous methods.[[1](#references)]

<p align="center">
  <img src="https://user-images.githubusercontent.com/77485245/226785860-e109b0ea-eb6b-4464-91a9-8898b3e3e056.png" width=400 />
</p>
<p align="center">
  <em>Figure 1. Architecture of Repvgg [<a href="#references">1</a>] </em>
</p>

## Performance

Our reproduced model performance on ImageNet-1K is reported as follows.

Experiments are tested on Ascend Atlas 800T A2 machines with mindspore 2.5.0 graph mode.

| model name | params(M) | cards | batch size | resolution | jit level | graph compile | ms/step | img/s    | acc@top1 | acc@top5 | recipe                                                                                         | weight                                                                                                |
| ---------- | --------- | ----- | ---------- | ---------- | --------- | ------------- | ------- | -------- | -------- | -------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| repvgg_a0  | 9.13      | 8     | 32         | 224x224    | O2        | 76s           | 24.12   | 10613.60 | 72.29    | 90.78    | [yaml](https://github.com/mindspore-lab/mindcv/blob/main/configs/repvgg/repvgg_a0_ascend.yaml) | [weights](https://download-mindspore.osinfra.cn/toolkits/mindcv/repvgg/repvgg_a0-b67a9f15-910v2.ckpt) |
| repvgg_a1  | 14.12     | 8     | 32         | 224x224    | O2        | 81s           | 28.29   | 9096.13  | 73.68    | 91.51    | [yaml](https://github.com/mindspore-lab/mindcv/blob/main/configs/repvgg/repvgg_a1_ascend.yaml) | [weights](https://download-mindspore.osinfra.cn/toolkits/mindcv/repvgg/repvgg_a1-a40aa623-910v2.ckpt) |

### Notes

- top-1 and top-5: Accuracy reported on the validation set of ImageNet-1K.

## Quick Start

### Preparation

#### Installation

Please refer to the [installation instruction](https://mindspore-lab.github.io/mindcv/installation/) in MindCV.

#### Dataset Preparation

Please download the [ImageNet-1K](https://www.image-net.org/challenges/LSVRC/2012/index.php) dataset for model training
and validation.

### Training

<!--- Guideline: Please avoid using shell scripts in the command line. Python scripts preferred. -->

- Distributed Training

  It is easy to reproduce the reported results with the pre-defined training recipe. For distributed training on multiple
  Ascend 910 devices, please run

  ```shell
  # distributed training on multiple NPU devices
  msrun --bind_core=True --worker_num 8 python train.py --config configs/repvgg/repvgg_a1_ascend.yaml --data_dir /path/to/imagenet
  ```

  For detailed illustration of all hyper-parameters, please refer
  to [config.py](https://github.com/mindspore-lab/mindcv/blob/main/config.py).

  **Note:** As the global batch size (batch_size x num_devices) is an important hyper-parameter, it is recommended to
  keep the global batch size unchanged for reproduction or adjust the learning rate linearly to a new global batch size.

- Standalone Training

  If you want to train or finetune the model on a smaller dataset without distributed training, please run:

  ```shell
  # standalone training on single NPU device
  python train.py --config configs/repvgg/repvgg_a1_ascend.yaml --data_dir /path/to/dataset --distribute False
  ```

### Validation

To validate the accuracy of the trained model, you can use `validate.py` and parse the checkpoint path
with `--ckpt_path`.

```shell
python validate.py -c configs/repvgg/repvgg_a1_ascend.yaml --data_dir /path/to/imagenet --ckpt_path /path/to/ckpt
```

## References

<!--- Guideline: Citation format GB/T 7714 is suggested. -->

[1] Ding X, Zhang X, Ma N, et al. Repvgg: Making vgg-style convnets great again[C]//Proceedings of the IEEE/CVF
conference on computer vision and pattern recognition. 2021: 13733-13742.
