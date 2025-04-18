# yolox_s

---

model-name: yolox_s

backbone-name: yolox

module-type: cv

fine-tunable: True

model-version: 2.5

train-dataset: COCO2017

evaluation: mAP41.0

author: MindSpore team

update-time: 2025-03-10

repo-link: <https://github.com/mindspore-lab/mindyolo/tree/v0.5.0/configs/yolox>

user-id: MindSpore

used-for: inference

mindspore-version: 2.5

asset:

- file-format: ckpt
  asset-link: <https://download-mindspore.osinfra.cn/toolkits/mindyolo/yolox/yolox-s_300e_map407-cebd0183-910v2.ckpt>
  asset-sha256: cebd0183

license: Apache2.0

summary: yolox is used for cv

---

# YOLOX

## Abstract

YOLOX is a new high-performance detector with some experienced improvements to YOLO series. We switch the YOLO detector to an anchor-free manner and conduct other advanced detection techniques, i.e., a decoupled head and the leading label assignment strategy SimOTA to achieve state-of-the-art results across a large scale range of models: For YOLO-Nano with only 0.91M parameters and 1.08G FLOPs, we get 25.3% AP on COCO, surpassing NanoDet by 1.8% AP; for YOLOv3, one of the most widely used detectors in industry, we boost it to 47.3% AP on COCO, outperforming the current best practice by 3.0% AP; for YOLOX-L with roughly the same amount of parameters as YOLOv4-CSP, YOLOv5-L, we achieve 50.0% AP on COCO at a speed of 68.9 FPS on Tesla V100, exceeding YOLOv5-L by 1.8% AP. Further, we won the 1st Place on Streaming Perception Challenge (Workshop on Autonomous Driving at CVPR 2021) using a single YOLOX-L model.

<div align=center>
<img src="https://raw.githubusercontent.com/zhanghuiyao/pics/main/mindyoloyolox_baseline.png"/>
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
msrun --worker_num=8 --local_worker_num=8 --bind_core=True --log_dir=./yolox_log python train.py --config ./configs/yolox/yolox-s.yaml --device_target Ascend --is_parallel True
```

**Note:** For more information about msrun configuration, please refer to [here](https://www.mindspore.cn/docs/zh-CN/r2.5.0/model_train/parallel/msrun_launcher.html)

For detailed illustration of all hyper-parameters, please refer to [config.py](https://github.com/mindspore-lab/mindyolo/blob/master/mindyolo/utils/config.py).

**Note:** As the global batch size (batch_size x num_devices) is an important hyper-parameter, it is recommended to keep the global batch size unchanged for reproduction.

#### - Standalone Training

If you want to train or finetune the model on a smaller dataset without distributed training, please firstly run:

```shell
# standalone 1st stage training on a CPU/Ascend device
python train.py --config ./configs/yolox/yolox-s.yaml --device_target Ascend
```

  </details>

### Validation and Test

To validate the accuracy of the trained model, you can use `test.py` and parse the checkpoint path with `--weight`.

```shell
python test.py --config ./configs/yolox/yolox-s.yaml --device_target Ascend --weight /PATH/TO/WEIGHT.ckpt
```

## Performance

Experiments are tested on Ascend Atlas 800T A2 machines with mindspore 2.5.0 graph mode.

| model name | scale | cards | batch size | resolution | jit level | graph compile | ms/step | img/s  |  map  |         recipe         |                                                      weight                                                      |
| :--------: | :---: | :---: | :--------: | :--------: | :-------: | :-----------: | :-----: | :----: | :---: | :--------------------: | :--------------------------------------------------------------------------------------------------------------: |
|   YOLOX    |   S   |   8   |     8      |  640x640   |    O2     |    299.01s    | 177.65  | 360.26 | 41.0% | [yaml](./yolox-s.yaml) | [weights](https://download-mindspore.osinfra.cn/toolkits/mindyolo/yolox/yolox-s_300e_map407-cebd0183-910v2.ckpt) |

<br>

### Notes

- map: Accuracy reported on the validation set.
- We refer to the official [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) to reproduce the results.

## References

<!--- Guideline: Citation format should follow GB/T 7714. -->

[1] Zheng Ge. YOLOX: Exceeding YOLO Series in 2021. <https://arxiv.org/abs/2107.08430>, 2021.
