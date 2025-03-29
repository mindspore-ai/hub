# yolov5n

---

model-name: yolov5n

backbone-name: yolov5

module-type: cv

fine-tunable: True

model-version: 2.5

train-dataset: COCO2017

evaluation: mAP27.4

author: MindSpore team

update-time: 2025-03-10

repo-link: <https://github.com/mindspore-lab/mindyolo/tree/v0.5.0/configs/yolov5>

user-id: MindSpore

used-for: inference

mindspore-version: 2.5

asset:

- file-format: ckpt
  asset-link: <https://download-mindspore.osinfra.cn/toolkits/mindyolo/yolov5/yolov5n_300e_mAP273-bedf9a93-910v2.ckpt>
  asset-sha256: bedf9a93

license: Apache2.0

summary: yolov5 is used for cv

---

# YOLOv5

## Abstract

YOLOv5 is a family of object detection architectures and models pretrained on the COCO dataset, representing Ultralytics open-source research into future vision AI methods, incorporating lessons learned and best practices evolved over thousands of hours of research and development.

<div align=center>
<img src="https://raw.githubusercontent.com/zhanghuiyao/pics/main/mindyolo20230407113509.png"/>
</div>

## Requirements

| mindspore | ascend driver |  firmware   | cann toolkit/kernel |
| :-------: | :-----------: | :---------: | :-----------------: |
|   2.5.0   |    24.1.0     | 7.5.0.3.220 |     8.0.0.beta1     |

## Quick Start

Please refer to the [GETTING_STARTED](https://github.com/mindspore-lab/mindyolo/blob/master/GETTING_STARTED.md) in MindYOLO for details.

### Training

<details open>
<summary><b>View More</b></summary>

#### - Distributed Training

It is easy to reproduce the reported results with the pre-defined training recipe. For distributed training on multiple Ascend 910 devices, please run

```shell
# distributed training on multiple Ascend devices
msrun --worker_num=8 --local_worker_num=8 --bind_core=True --log_dir=./yolov5_log  python train.py --config ./configs/yolov5/yolov5n.yaml --device_target Ascend --is_parallel True
```

**Note:** For more information about msrun configuration, please refer to [here](https://www.mindspore.cn/docs/zh-CN/r2.5.0/model_train/parallel/msrun_launcher.html)

For detailed illustration of all hyper-parameters, please refer to [config.py](https://github.com/mindspore-lab/mindyolo/blob/master/mindyolo/utils/config.py).

**Note:** As the global batch size (batch_size x num_devices) is an important hyper-parameter, it is recommended to keep the global batch size unchanged for reproduction or adjust the learning rate linearly to a new global batch size.

#### - Standalone Training

If you want to train or finetune the model on a smaller dataset without distributed training, please run:

```shell
# standalone training on a CPU/Ascend device
python train.py --config ./configs/yolov5/yolov5n.yaml --device_target Ascend
```

  </details>

### Validation and Test

To validate the accuracy of the trained model, you can use `test.py` and parse the checkpoint path with `--weight`.

```shell
python test.py --config ./configs/yolov5/yolov5n.yaml --device_target Ascend --weight /PATH/TO/WEIGHT.ckpt
```

To validate the accuracy of the trained model for resolution of 1280, you can use `test.py` and parse the checkpoint path with `--weight` and parse the image sizes with `--img_size`.

```shell
python test.py --config ./configs/yolov5/yolov5n6.yaml --device_target Ascend --weight /PATH/TO/WEIGHT.ckpt --img_size 1280
```

## Performance

Experiments are tested on Ascend 910\* with mindspore 2.5.0 graph mode.

| model name | scale | cards | batch size | resolution | jit level | graph compile | ms/step | img/s  |  map  |         recipe          |                                                      weight                                                       |
| :--------: | :---: | :---: | :--------: | :--------: | :-------: | :-----------: | :-----: | :----: | :---: | :---------------------: | :---------------------------------------------------------------------------------------------------------------: |
|   YOLOv5   |   N   |   8   |     32     |  640x640   |    O2     |    377.81s    | 520.79  | 491.56 | 27.4% | [yaml](./yolov5n.yaml)  | [weights](https://download-mindspore.osinfra.cn/toolkits/mindyolo/yolov5/yolov5n_300e_mAP273-bedf9a93-910v2.ckpt) |
|   YOLOv5   |   S   |   8   |     32     |  640x640   |    O2     |    378.18s    | 526.49  | 486.30 | 37.6% | [yaml](./yolov5s.yaml)  | [weights](https://download-mindspore.osinfra.cn/toolkits/mindyolo/yolov5/yolov5s_300e_mAP376-df4a45b6-910v2.ckpt) |
|   YOLOv5   |  N6   |   8   |     32     | 1280x1280  |    O2     |    494.36s    | 1543.35 | 165.87 | 35.7% | [yaml](./yolov5n6.yaml) |   [weights](https://download-mindspore.osinfra.cn/toolkits/mindyolo/yolov5/yolov5n6_300e_mAP357-49d91077.ckpt)    |
|   YOLOv5   |  S6   |   8   |     32     | 1280x1280  |    O2     |    524.91s    | 1514.98 | 168.98 | 44.4% | [yaml](./yolov5s6.yaml) |   [weights](https://download-mindspore.osinfra.cn/toolkits/mindyolo/yolov5/yolov5s6_300e_mAP444-aeaffe77.ckpt)    |
|   YOLOv5   |  M6   |   8   |     32     | 1280x1280  |    O2     |    572.32s    | 1769.17 | 144.70 | 51.1% | [yaml](./yolov5m6.yaml) |   [weights](https://download-mindspore.osinfra.cn/toolkits/mindyolo/yolov5/yolov5m6_300e_mAP511-025d9536.ckpt)    |
|   YOLOv5   |  L6   |   8   |     16     | 1280x1280  |    O2     |    800.34s    | 894.65  | 143.07 | 53.6% | [yaml](./yolov5l6.yaml) |   [weights](https://download-mindspore.osinfra.cn/toolkits/mindyolo/yolov5/yolov5l6_300e_mAP536-617a1cc1.ckpt)    |
|   YOLOv5   |  X6   |   8   |     8      | 1280x1280  |    O2     |    995.73s    | 864.43  | 74.04  | 54.5% | [yaml](./yolov5x6.yaml) |   [weights](https://download-mindspore.osinfra.cn/toolkits/mindyolo/yolov5/yolov5x6_300e_mAP545-81ebdca9.ckpt)    |

<br>

### Notes

- map: Accuracy reported on the validation set.
- We refer to the official [YOLOV5](https://github.com/ultralytics/yolov5) to reproduce the P5 series model, and the differences are as follows:
  The single-device batch size is 32. This is different from the official codes.

## References

<!--- Guideline: Citation format should follow GB/T 7714. -->

[1] Jocher Glenn. YOLOv5 release v6.1. <https://github.com/ultralytics/yolov5/releases/tag/v6.1>, 2022.
