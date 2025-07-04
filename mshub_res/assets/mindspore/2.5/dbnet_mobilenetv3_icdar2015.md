# dbnet_mobilenetv3

---

model-name: dbnet_mobilenetv3

backbone-name: mobilenetv3

module-type: cv

fine-tunable: True

model-version: 2.5

train-dataset: ICDAR2015

evaluation: Recall76.27 | Precision76.06 | F-score76.17

author: MindSpore team

update-time: 2025-03-10

repo-link: <https://github.com/mindspore-lab/mindocr/tree/v0.5.0/configs/det/dbnet>

user-id: MindSpore

used-for: inference

mindspore-version: 2.5

asset:

- file-format: ckpt
  asset-link: <https://download-mindspore.osinfra.cn/toolkits/mindocr/dbnet/dbnet_mobilenetv3-7e89e1df-910v2.ckpt>
  asset-sha256: 7e89e1df

license: Apache2.0

summary: dbnet_mobilenetv3 is used for cv

---

# DBNet and DBNet++

<!--- Guideline: use url linked to abstract in ArXiv instead of PDF for fast loading.  -->

> DBNet: [Real-time Scene Text Detection with Differentiable Binarization](https://arxiv.org/abs/1911.08947)
>
> DBNet++: [Real-Time Scene Text Detection with Differentiable Binarization and Adaptive Scale Fusion](https://arxiv.org/abs/2202.10304)

## Introduction

### DBNet

DBNet is a segmentation-based scene text detection method. Segmentation-based methods are gaining popularity for scene
text detection purposes as they can more accurately describe scene text of various shapes, such as curved text.
The drawback of current segmentation-based SOTA methods is the post-processing of binarization (conversion of
probability maps into text bounding boxes) which often requires a manually set threshold (reduces prediction accuracy)
and complex algorithms for grouping pixels (resulting in a considerable time cost during inference).
To eliminate the problem described above, DBNet integrates an adaptive threshold called Differentiable Binarization(DB)
into the architecture. DB simplifies post-processing and enhances the performance of text detection.Moreover, it can be
removed in the inference stage without sacrificing performance.[[1](#references)]

<p align="center"><img alt="Figure 1. Overall DBNet architecture" src="https://user-images.githubusercontent.com/16683750/225589619-d50c506c-e903-4f59-a316-8b62586c73a9.png" width="800"/></p>
<p align="center"><em>Figure 1. Overall DBNet architecture</em></p>

The overall architecture of DBNet is presented in _Figure 1._ It consists of multiple stages:

1. Feature extraction from a backbone at different scales. ResNet-50 is used as a backbone, and features are extracted
   from stages 2, 3, 4, and 5.
2. The extracted features are upscaled and summed up with the previous stage features in a cascade fashion.
3. The resulting features are upscaled once again to match the size of the largest feature map (from the stage 2) and
   concatenated along the channel axis.
4. Then, the final feature map (shown in dark blue) is used to predict both the probability and threshold maps by
   applying 3×3 convolutional operator and two de-convolutional operators with stride 2.
5. The probability and threshold maps are merged into one approximate binary map by the Differentiable binarization
   module. The approximate binary map is used to generate text bounding boxes.

### DBNet++

DBNet++ is an extension of DBNet and thus replicates its architecture. The only difference is that instead of
concatenating extracted and scaled features from the backbone as DBNet did, DBNet++ uses an adaptive way to fuse those
features called Adaptive Scale Fusion (ASF) module (Figure 2). It improves the scale robustness of the network by
fusing features of different scales adaptively. By using ASF, DBNet++’s ability to detect text instances of diverse
scales is distinctly strengthened.[[2](#references)]

<p align="center"><img alt="Figure 2. Overall DBNet++ architecture" src="https://user-images.githubusercontent.com/16683750/236786997-13823b9c-ecaa-4bc5-8037-71299b3baffe.png" width="800"/></p>
<p align="center"><em>Figure 2. Overall DBNet++ architecture</em></p>

<p align="center"><img alt="Figure 3. Detailed architecture of the Adaptive Scale Fusion module" src="https://user-images.githubusercontent.com/16683750/236787093-c0c78d8f-e4f4-4c5e-8259-7120a14b0e31.png" width="700"/></p>
<p align="center"><em>Figure 3. Detailed architecture of the Adaptive Scale Fusion module</em></p>

ASF consists of two attention modules – stage-wise attention and spatial attention, where the latter is integrated in
the former as described in the Figure 3. The stage-wise attention module learns the weights of the feature maps of
different scales. While the spatial attention module learns the attention across the spatial dimensions. The
combination of these two modules leads to scale-robust feature fusion.
DBNet++ performs better in detecting text instances of diverse scales, especially for large-scale text instances where
DBNet may generate inaccurate or discrete bounding boxes.

## Requirements

| mindspore | ascend driver |  firmware   | cann toolkit/kernel |
| :-------: | :-----------: | :---------: | :-----------------: |
|   2.5.0   |    24.1.0     | 7.5.0.3.220 |     8.0.0.beta1     |

## Quick Start

### Installation

Please refer to the [installation instruction](https://github.com/mindspore-lab/mindocr#installation) in MindOCR.

### Dataset preparation

#### ICDAR2015 dataset

Please download [ICDAR2015](https://rrc.cvc.uab.es/?ch=4&com=downloads) dataset, and convert the labels to the desired format referring to [dataset_converters](../../../tools/dataset_converters/README.md).

The prepared dataset file structure should be:

```text
.
├── test
│   ├── images
│   │   ├── img_1.jpg
│   │   ├── img_2.jpg
│   │   └── ...
│   └── test_det_gt.txt
└── train
    ├── images
    │   ├── img_1.jpg
    │   ├── img_2.jpg
    │   └── ....jpg
    └── train_det_gt.txt
```

#### MSRA-TD500 dataset

Please download MSRA-TD500 dataset，and convert the labels to the desired format referring to [dataset_converters](../../../tools/dataset_converters/README.md).

The prepared dataset file structure should be:

```txt
MSRA-TD500
 ├── test
 │   ├── IMG_0059.gt
 │   ├── IMG_0059.JPG
 │   ├── IMG_0080.gt
 │   ├── IMG_0080.JPG
 │   ├── ...
 │   ├── train_det_gt.txt
 ├── train
 │   ├── IMG_0030.gt
 │   ├── IMG_0030.JPG
 │   ├── IMG_0063.gt
 │   ├── IMG_0063.JPG
 │   ├── ...
 │   ├── test_det_gt.txt
```

#### SCUT-CTW1500 dataset

Please download [SCUT-CTW1500](https://github.com/Yuliang-Liu/Curve-Text-Detector) dataset，and convert the labels to the desired format referring to [dataset_converters](https://github.com/mindspore-lab/mindocr/blob/main/tools/dataset_converters/README.md).

The prepared dataset file structure should be:

```txt
ctw1500
 ├── test_images
 │   ├── 1001.jpg
 │   ├── 1002.jpg
 │   ├── ...
 ├── train_images
 │   ├── 0001.jpg
 │   ├── 0002.jpg
 │   ├── ...
 ├── test_det_gt.txt
 ├── train_det_gt.txt
```

#### Total-Text dataset

Please download [Total-Text](https://github.com/cs-chan/Total-Text-Dataset/tree/master/Dataset) dataset，and convert the labels to the desired format referring to [dataset_converters](https://github.com/mindspore-lab/mindocr/blob/main/tools/dataset_converters/README.md).

The prepared dataset file structure should be:

```txt
totaltext
 ├── Images
 │   ├── Train
 │   │   ├── img1001.jpg
 │   │   ├── img1002.jpg
 │   │   ├── ...
 │   ├── Test
 │   │   ├── img1.jpg
 │   │   ├── img2.jpg
 │   │   ├── ...
 ├── test_det_gt.txt
 ├── train_det_gt.txt
```

#### MLT2017 dataset

The MLT2017 dataset is a multilingual text detection and recognition dataset that includes nine languages: Chinese, Japanese, Korean, English, French, Arabic, Italian, German, and Hindi. Please download [MLT2017](https://rrc.cvc.uab.es/?ch=8&com=downloads) and extract the dataset. Then convert the .gif format images in the data to .jpg or .png format, and convert the labels to the desired format referring to [dataset_converters](https://github.com/mindspore-lab/mindocr/blob/main/tools/dataset_converters/README.md).

The prepared dataset file structure should be:

```txt
MLT_2017
 ├── train
 │   ├── img_1.png
 │   ├── img_2.png
 │   ├── img_3.jpg
 │   ├── img_4.jpg
 │   ├── ...
 ├── validation
 │   ├── img_1.jpg
 │   ├── img_2.jpg
 │   ├── ...
 ├── train_det_gt.txt
 ├── validation_det_gt.txt
```

> If users want to use their own dataset for training, please convert the labels to the desired format referring to [dataset_converters](https://github.com/mindspore-lab/mindocr/blob/main/tools/dataset_converters/README.md). Then configure the yaml file, and use a single or multiple devices to run train.py for training. For detailed information, please refer to the following tutorials.

#### SynthText dataset

Please download [SynthText](https://academictorrents.com/details/2dba9518166cbd141534cbf381aa3e99a087e83c) dataset and process it as described in [dataset_converters](../../../tools/dataset_converters/README.md)

```text
.
├── SynthText
│   ├── 1
│   │   ├── img_1.jpg
│   │   ├── img_2.jpg
│   │   └── ...
│   ├── 2
│   │   ├── img_1.jpg
│   │   ├── img_2.jpg
│   │   └── ...
│   ├── ...
│   ├── 200
│   │   ├── img_1.jpg
│   │   ├── img_2.jpg
│   │   └── ...
│   └── gt.mat

```

> :warning: Additionally, It is strongly recommended to pre-process the `SynthText` dataset before using it as it contains some faulty data:
>
> ```shell
> python tools/dataset_converters/convert.py --dataset_name=synthtext --task=det --label_dir=/path-to-data-dir/SynthText/gt.mat --output_path=/path-to-data-dir/SynthText/gt_processed.mat
> ```
>
> This operation will generate a filtered output in the same format as the original `SynthText`.

### Update yaml config file

Update `configs/det/dbnet/db_r50_icdar15.yaml` configuration file with data paths,
specifically the following parts. The `dataset_root` will be concatenated with `data_dir` and `label_file` respectively to be the complete dataset directory and label file path.

```yaml
---
train:
  ckpt_save_dir: "./tmp_det"
  dataset_sink_mode: False
  dataset:
    type: DetDataset
    dataset_root: dir/to/dataset          <--- Update
    data_dir: train/images                <--- Update
    label_file: train/train_det_gt.txt    <--- Update
---
eval:
  dataset_sink_mode: False
  dataset:
    type: DetDataset
    dataset_root: dir/to/dataset          <--- Update
    data_dir: test/images                 <--- Update
    label_file: test/test_det_gt.txt      <--- Update
```

> Optionally, change `num_workers` according to the cores of CPU.

DBNet consists of 3 parts: `backbone`, `neck`, and `head`. Specifically:

```yaml
model:
  type: det
  transform: null
  backbone:
    name: det_resnet50 # Only ResNet50 is supported at the moment
    pretrained: True # Whether to use weights pretrained on ImageNet
  neck:
    name: DBFPN # FPN part of the DBNet
    out_channels: 256
    bias: False
    use_asf: False # Adaptive Scale Fusion module from DBNet++ (use it for DBNet++ only)
  head:
    name: DBHead
    k: 50 # amplifying factor for Differentiable Binarization
    bias: False
    adaptive: True # True for training, False for inference
```

### Training

- Standalone training

  Please set `distribute` in yaml config file to be False.

  ```shell
  python tools/train.py -c=configs/det/dbnet/db_r50_icdar15.yaml
  ```

- Distributed training

  Please set `distribute` in yaml config file to be True.

  ```shell
  # n is the number of NPUs
  mpirun --allow-run-as-root -n 2 python tools/train.py --config configs/det/dbnet/db_r50_icdar15.yaml
  ```

The training result (including checkpoints, per-epoch performance and curves) will be saved in the directory parsed by the arg `ckpt_save_dir` in yaml config file. The default directory is `./tmp_det`.

### Evaluation

To evaluate the accuracy of the trained model, you can use `eval.py`. Please set the checkpoint path to the arg `ckpt_load_path` in the `eval` section of yaml config file, set `distribute` to be False, and then run:

```shell
python tools/eval.py -c=configs/det/dbnet/db_r50_icdar15.yaml
```

### Performance

DBNet and DBNet++ were trained on the ICDAR2015, MSRA-TD500, SCUT-CTW1500, Total-Text, and MLT2017 datasets. In addition, we conducted pre-training on the ImageNet or SynthText dataset and provided a URL to download pretrained weights. All training results are as follows:

#### ICDAR2015

| **model name** | **backbone** | **pretrained** | **cards** | **batch size** | **jit level** | **graph compile** | **ms/step** | **img/s** | **recall** | **precision** | **f-score** |               **recipe**               |                                                                                                       **weight**                                                                                                        |
| :------------: | :----------: | :------------: | :-------: | :------------: | :-----------: | :---------------: | :---------: | :-------: | :--------: | :-----------: | :---------: | :------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|     DBNet      | MobileNetV3  |    ImageNet    |     1     |       10       |      O2       |     403.87 s      |    65.69    |  152.23   |   74.68%   |    79.38%     |   76.95%    |  [yaml](db_mobilenetv3_icdar15.yaml)   | [ckpt](https://download-mindspore.osinfra.cn/toolkits/mindocr/dbnet/dbnet_mobilenetv3-e72f9b8b-910v2.ckpt) \| [mindir](https://download.mindspore.cn/toolkits/mindocr/dbnet/dbnet_mobilenetv3-62c44539-f14c6a13.mindir) |
|     DBNet      | MobileNetV3  |    ImageNet    |     8     |       8        |      O2       |     405.35 s      |    54.46    |  1175.12  |   76.27%   |    76.06%     |   76.17%    | [yaml](db_mobilenetv3_icdar15_8p.yaml) |                                                       [ckpt](https://download-mindspore.osinfra.cn/toolkits/mindocr/dbnet/dbnet_mobilenetv3-7e89e1df-910v2.ckpt)                                                        |
|     DBNet      |  ResNet-50   |    ImageNet    |     1     |       10       |      O2       |     147.81 s      |   155.62    |   64.25   |   84.50%   |    85.36%     |   84.93%    |      [yaml](db_r50_icdar15.yaml)       |    [ckpt](https://download-mindspore.osinfra.cn/toolkits/mindocr/dbnet/dbnet_resnet50-48153c3b-910v2.ckpt) \| [mindir](https://download.mindspore.cn/toolkits/mindocr/dbnet/dbnet_resnet50-c3a4aa24-fbf95c82.mindir)    |
|     DBNet      |  ResNet-50   |    ImageNet    |     8     |       10       |      O2       |     151.23 s      |   159.22    |   502.4   |   81.15%   |    87.63%     |   84.26%    |     [yaml](db_r50_icdar15_8p.yaml)     |                                                         [ckpt](https://download-mindspore.osinfra.cn/toolkits/mindocr/dbnet/dbnet_resnet50-e10bad35-910v2.ckpt)                                                         |
|    DBNet++     |  ResNet-50   |   SynthText    |     1     |       32       |      O2       |     191.93 s      |   549.24    |   58.26   |   86.81%   |    86.85%     |   86.86%    |     [yaml](dbpp_r50_icdar15.yaml)      |     [ckpt](https://download.mindspore.cn/toolkits/mindocr/dbnet/dbnetpp_resnet50_910-35dc71f2.ckpt) \| [mindir](https://download.mindspore.cn/toolkits/mindocr/dbnet/dbnetpp_resnet50_910-35dc71f2-e61a9c37.mindir)     |

### Notes

- Note that the training time of DBNet is highly affected by data processing and varies on different machines.
- The input_shape for exported DBNet MindIR and DBNet++ MindIR in the links are `(1,3,736,1280)` and `(1,3,1152,2048)`, respectively.

## References

<!--- Guideline: Citation format GB/T 7714 is suggested. -->

[1] Minghui Liao, Zhaoyi Wan, Cong Yao, Kai Chen, Xiang Bai. Real-time Scene Text Detection with Differentiable
Binarization. arXiv:1911.08947, 2019

[2] Minghui Liao, Zhisheng Zou, Zhaoyi Wan, Cong Yao, Xiang Bai. Real-Time Scene Text Detection with Differentiable
Binarization and Adaptive Scale Fusion. arXiv:2202.10304, 2022
