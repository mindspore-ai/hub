# yolov8s

---

model-name: yolov8s

backbone-name: yolov8

module-type: cv

fine-tunable: True

model-version: 2.5

train-dataset: COCO2017

evaluation: mAP44.7

author: MindSpore team

update-time: 2025-03-10

repo-link: <https://github.com/mindspore-lab/mindyolo/tree/v0.5.0/configs/yolov8>

user-id: MindSpore

used-for: inference

mindspore-version: 2.5

asset:

- file-format: ckpt
  asset-link: <https://download-mindspore.osinfra.cn/toolkits/mindyolo/yolov8/yolov8-s_500e_mAP446-fae4983f-910v2.ckpt>
  asset-sha256: fae4983f

license: Apache2.0

summary: yolov8 is used for cv

---

# YOLOv8

## Abstract

Ultralytics YOLOv8, developed by Ultralytics, is a cutting-edge, state-of-the-art (SOTA) model that builds upon the success of previous YOLO versions and introduces new features and improvements to further boost performance and flexibility. YOLOv8 is designed to be fast, accurate, and easy to use, making it an excellent choice for a wide range of object detection, image segmentation and image classification tasks.

<div align=center>
<img src="https://raw.githubusercontent.com/zhanghuiyao/pics/main/mindyolomindyolo-yolov8-comparison-plots.png"/>
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
msrun --worker_num=8 --local_worker_num=8 --bind_core=True --log_dir=./yolov8_log python train.py --config ./configs/yolov8/yolov8n.yaml --device_target Ascend --is_parallel True
```

**Note:** For more information about msrun configuration, please refer to [here](https://www.mindspore.cn/docs/zh-CN/r2.5.0/model_train/parallel/msrun_launcher.html)

For detailed illustration of all hyper-parameters, please refer to [config.py](https://github.com/mindspore-lab/mindyolo/blob/master/mindyolo/utils/config.py).

**Note:** As the global batch size (batch_size x num_devices) is an important hyper-parameter, it is recommended to keep the global batch size unchanged for reproduction or adjust the learning rate linearly to a new global batch size.

#### - Standalone Training

If you want to train or finetune the model on a smaller dataset without distributed training, please run:

```shell
# standalone training on a CPU/Ascend device
python train.py --config ./configs/yolov8/yolov8n.yaml --device_target Ascend
```

  </details>

### Validation and Test

To validate the accuracy of the trained model, you can use `test.py` and parse the checkpoint path with `--weight`.

```shell
python test.py --config ./configs/yolov8/yolov8n.yaml --device_target Ascend --weight /PATH/TO/WEIGHT.ckpt
```

## Performance

### Detection

Experiments are tested on Ascend 910\* with mindspore 2.5.0 graph mode.

| model name | scale | cards | batch size | resolution | jit level | graph compile | ms/step | img/s  |  map  |         recipe         |                                                       weight                                                       |
| :--------: | :---: | :---: | :--------: | :--------: | :-------: | :-----------: | :-----: | :----: | :---: | :--------------------: | :----------------------------------------------------------------------------------------------------------------: |
|   YOLOv8   |   N   |   8   |     16     |  640x640   |    O2     |    145.89s    | 252.79  | 506.35 | 37.3% | [yaml](./yolov8n.yaml) | [weights](https://download-mindspore.osinfra.cn/toolkits/mindyolo/yolov8/yolov8-n_500e_mAP372-0e737186-910v2.ckpt) |
|   YOLOv8   |   S   |   8   |     16     |  640x640   |    O2     |    172.22s    | 251.30  | 509.35 | 44.7% | [yaml](./yolov8s.yaml) | [weights](https://download-mindspore.osinfra.cn/toolkits/mindyolo/yolov8/yolov8-s_500e_mAP446-fae4983f-910v2.ckpt) |

### Segmentation

Experiments are tested on Ascend 910 with mindspore 2.5.0 graph mode.

_coming soon_

### Notes

- map: Accuracy reported on the validation set.
- We refer to the official [YOLOV8](https://github.com/ultralytics/ultralytics) to reproduce the P5 series model.

## References

<!--- Guideline: Citation format should follow GB/T 7714. -->

[1] Jocher Glenn. Ultralytics YOLOv8. <https://github.com/ultralytics/ultralytics>, 2023.
