# AnimateDiff

---

model-name: AnimateDiff

backbone-name: stable-diffusion

module-type: mm

fine-tunable: True

model-version: 2.5

train-dataset: WebVid

author: MindSpore team

update-time: 2025-04-22

repo-link: <https://github.com/mindspore-lab/mindone/tree/v0.3.0/examples/animatediff>

user-id: MindSpore

used-for: inference

mindspore-version: 2.5

license: Apache2.0

summary: AnimateDiff is used for text-to-video generation

---

# AnimateDiff based on MindSpore

This repository is the MindSpore implementation of [AnimateDiff](https://arxiv.org/abs/2307.04725).

## Features

- ✔ Text-to-video generation with AnimdateDiff v2, supporting 16 frames @512x512 resolution on Ascend Atlas 800T A2 machines
- ✔ MotionLoRA inference
- ✔ Motion Module Training
- ✔ Motion LoRA Training
- ✔ AnimateDiff v3 Inference

## Requirements

| mindspore | ascend driver |  firmware   | cann toolkit/kernel |
| :-------: | :-----------: | :---------: | :-----------------: |
|   2.5.0   |    24.1.0     | 7.5.0.3.220 |     8.0.0.beta1     |

To install other dependent packages:

```bash
pip install -r requirements.txt
```

In case `decord` package is not available, try `pip install eva-decord`.
For EulerOS, instructions on ffmpeg and decord installation are as follows.

```shell
1. install ffmpeg 4, referring to https://ffmpeg.org/releases
    wget https://ffmpeg.org/releases/ffmpeg-4.0.1.tar.bz2 --no-check-certificate
    tar -xvf ffmpeg-4.0.1.tar.bz2
    mv ffmpeg-4.0.1 ffmpeg
    cd ffmpeg
    ./configure --enable-shared         # --enable-shared is needed for sharing libavcodec with decord
    make -j 64
    make install
2. install decord, referring to https://github.com/dmlc/decord?tab=readme-ov-file#install-from-source
    git clone --recursive https://github.com/dmlc/decord
    cd decord
    rm build && mkdir build && cd build
    cmake .. -DUSE_CUDA=0 -DCMAKE_BUILD_TYPE=Release
    make -j 64
    make install
    cd ../python
    python3 setup.py install --user
```

## Prepare Model Weights

Please download the following weights from to [huggingface](https://huggingface.co/guoyww/animatediff/tree/main/).

The full tree of expected checkpoints is shown below:

```text
models
├── domain_adapter_lora
│   └── v3_sd15_adapter.ckpt
├── dreambooth_lora
│   ├── realisticVisionV51_v51VAE.ckpt
│   └── toonyou_beta3.ckpt
├── motion_lora
│   └── v2_lora_ZoomIn.ckpt
├── motion_module
│   ├── mm_sd_v15.ckpt
│   ├── mm_sd_v15_v2.ckpt
│   └── v3_sd15_mm.ckpt
├── sparsectrl_encoder
│   ├── v3_sd15_sparsectrl_rgb.ckpt
│   └── v3_sd15_sparsectrl_scribble.ckpt
└── stable_diffusion
    └── sd_v1.5-d0ab7146.ckpt
```

Then, put all the weights under `animatediff/models/torch_ckpts/` and convert them by running the following command.

```shell
sh scripts/convert_weights.sh
```

## Inference

### Inference (AnimateDiff v3 and SparseCtrl)

```shell
# download demo images
bash scripts/download_demo_images.sh

# under general T2V setting
python text_to_video.py --config configs/prompts/v3/v3-1-T2V.yaml

# image animation (on RealisticVision)
python text_to_video.py --config configs/prompts/v3/v3-2-animation-RealisticVision.yaml

# sketch-to-animation and storyboarding (on RealisticVision)
python text_to_video.py --config configs/prompts/v3/v3-3-sketch-RealisticVision.yaml
```

Results:

<table class="center">
    <tr style="line-height: 0">
    <td width=25% style="border: none; text-align: center">Input (by RealisticVision)</td>
    <td width=25% style="border: none; text-align: center">Animation</td>
    <td width=25% style="border: none; text-align: center">Input</td>
    <td width=25% style="border: none; text-align: center">Animation</td>
    </tr>
    <tr>
    <td width=25% style="border: none"><img src="https://raw.githubusercontent.com/wtomin/mindone-assets/main/animatediff/__assets__/demos/image/RealisticVision_firework.png" style="width:100%"></td>
    <td width=25% style="border: none"><img src="https://raw.githubusercontent.com/wtomin/mindone-assets/main/animatediff/v3/0-closeup-face-photo-of-man-in-black-clothes%2C-night-city.gif" style="width:100%"></td>
    <td width=25% style="border: none"><img src="https://raw.githubusercontent.com/wtomin/mindone-assets/main/animatediff/__assets__/demos/image/RealisticVision_sunset.png" style="width:100%"></td>
    <td width=25% style="border: none"><img src="https://raw.githubusercontent.com/wtomin/mindone-assets/main/animatediff/v3/0-masterpiece%2C-bestquality%2C-highlydetailed%2C-ultradetailed%2C-sunset%2C-orange-sky%2C-warm-lighting%2C-fishing.gif" style="width:100%"></td>
    </tr>
</table>

<table class="center">
    <tr style="line-height: 0">
    <td width=25% style="border: none; text-align: center">Input Scribble</td>
    <td width=25% style="border: none; text-align: center">Output</td>
    <td width=25% style="border: none; text-align: center">Input Scribbles</td>
    <td width=25% style="border: none; text-align: center">Output</td>
    </tr>
    <tr>
      <td width=25% style="border: none"><img src="https://raw.githubusercontent.com/wtomin/mindone-assets/main/animatediff/__assets__/demos/scribble/scribble_1.png" style="width:100%"></td>
      <td width=25% style="border: none"><img src="https://raw.githubusercontent.com/wtomin/mindone-assets/main/animatediff/v3/0-a-back-view-of-a-boy%2C-standing-on-the-ground%2C.gif" style="width:100%"></td>
      <td width=25% style="border: none"><img src="https://raw.githubusercontent.com/wtomin/mindone-assets/main/animatediff/__assets__/demos/scribble/scribble_2_readme.png" style="width:100%"></td>
      <td width=25% style="border: none"><img src="https://raw.githubusercontent.com/wtomin/mindone-assets/main/animatediff/v3/0-an-aerial-view-of-a-modern-city%2C-sunlight%2C-day-time%2C.gif" style="width:100%"></td>
    </tr>
</table>

### Inference (AnimateDiff v2)

#### Text-to-Video

The script uses DDIM sampling by default:

```shell
python text_to_video.py --config configs/prompts/v2/1-ToonYou.yaml --L 16 --H 512 --W 512
```

Results:

<p float="left">
<img src=https://github.com/SamitHuang/mindone/assets/8156835/9d6ef65f-223d-407c-bc85-a852d3594934 width="25%" />
<img src=https://github.com/SamitHuang/mindone/assets/8156835/40dbe614-ccc6-4567-ab53-099cb8d61ebc width="25%" />
<img src=https://github.com/SamitHuang/mindone/assets/8156835/fb9e2069-041a-4e81-b88e-ccdcfa8afd32 width="25%" />
</p>

#### Motion LoRA

The script uses DDIM sampling by default:

```shell
python text_to_video.py --config configs/prompts/v2/1-ToonYou-MotionLoRA.yaml --L 16 --H 512 --W 512
```

Results using Zoom-In motion lora:

<p float="left">
<img src=https://github.com/SamitHuang/mindone/assets/8156835/9357b2e4-0479-4afa-a28b-7a121aba865e width="25%" />
<img src=https://github.com/SamitHuang/mindone/assets/8156835/f8ff1d2a-20d8-447d-89b2-fd94430db7a4 width="25%" />
<img src=https://github.com/SamitHuang/mindone/assets/8156835/d4d947a3-4d10-4c7e-b134-a725269037c3 width="25%" />
</p>

## Training (AnimateDiff v2)

### Image Finetuning

```shell
python train.py --config configs/training/image_finetune.yaml
```

Infer with the trained model by running:

```shell
python text_to_video.py --config configs/prompts/v2/base_video.yaml \
    --pretrained_model_path {path to saved checkpoint} \
    --prompt  {text prompt}  \
```

### Motion Module Training

```shell
python train.py --config configs/training/mmv2_train.yaml
```

You may change the arguments including data path, output directory, lr, etc in the yaml config file. You can also change by command line arguments referring to `args_train.py` or `python train.py --help`

Min-SNR weighting can improve diffusion training convergence. Enable it by appending `--snr_gamma=5.0` to the training command.

Infer with the trained model by running:

```shell
python text_to_video.py --config configs/prompts/v2/base_video.yaml \
    --motion_module_path {path to saved checkpoint} \
    --prompt  {text prompt}  \
```

You can also create a new config yaml to specify the prompts to test and the motion module path based on `configs/prompt/v2/base_video.yaml`.

Here are some generation results after MM training on 512x512 resolution and 16-frame data.

<table class="center">
    <tr style="line-height: 0">
    <td width=25% style="border: none; text-align: center">Disco light leaks disco ball light reflections shaped rectangular and line with motion blur effect</td>
    <td width=25% style="border: none; text-align: center">Cloudy moscow kremlin time lapse</td>
    <td width=25% style="border: none; text-align: center">Sharp knife to cut delicious smoked fish</td>
    <td width=25% style="border: none; text-align: center">A baker turns freshly baked loaves of sourdough bread</td>
    </tr>
    <tr>
      <td width=25% style="border: none"><img src="https://github.com/SamitHuang/mindone/assets/8156835/22fe1fcf-9dbd-4db4-8082-bcec5ce4cc7a" style="width:100%"></td>
      <td width=25% style="border: none"><img src="https://github.com/SamitHuang/mindone/assets/8156835/01856c0c-cfa9-4445-9c3d-7abc1af245e6" style="width:100%"></td>
      <td width=25% style="border: none"><img src="https://github.com/SamitHuang/mindone/assets/8156835/eb53baa6-1fb7-44f5-aced-bd7609fca9a2" style="width:100%"></td>
      <td width=25% style="border: none"><img src="https://github.com/SamitHuang/mindone/assets/8156835/135b552a-7331-478d-9590-f201b1145dff" style="width:100%"></td>
    </tr>
</table>

### Motion LoRA Training

```shell
python train.py --config configs/training/mmv2_lora.yaml
```

Infer with the trained model by running:

```shell
python text_to_video.py --config configs/prompts/v2/base_video.yaml \
    --motion_lora_path {path to saved checkpoint} \
    --prompt  {text prompt}  \
```

Here are some generation results after lora fine-tuning on 512x512 resolution and 16-frame data.

<table class="center">
    <tr style="line-height: 0">
    <td width=25% style="border: none; text-align: center">Disco light leaks disco ball light reflections shaped rectangular and line with motion blur effect</td>
    <td width=25% style="border: none; text-align: center">Cloudy moscow kremlin time lapse</td>
    <td width=25% style="border: none; text-align: center">Sharp knife to cut delicious smoked fish</td>
    <td width=25% style="border: none; text-align: center">A baker turns freshly baked loaves of sourdough bread</td>
    </tr>
    <tr>
      <td width=25% style="border: none"><img src="https://github.com/SamitHuang/mindone/assets/8156835/03d4d494-9ee4-473a-82c4-2d95fecf28f6" style="width:100%"></td>
      <td width=25% style="border: none"><img src="https://github.com/SamitHuang/mindone/assets/8156835/72075086-6f14-43ec-9a1b-3f27adc3ad4f" style="width:100%"></td>
      <td width=25% style="border: none"><img src="https://github.com/SamitHuang/mindone/assets/8156835/a4a5ee37-81df-4498-972b-ab454de77fc4" style="width:100%"></td>
      <td width=25% style="border: none"><img src="https://github.com/SamitHuang/mindone/assets/8156835/93b3ba6a-350d-4d35-8e44-d0445d8f3089" style="width:100%"></td>
    </tr>
</table>

## Performance (AnimateDiff v2)

Experiments are tested on Ascend Atlas 800T A2 machines with graph mode.

### Inference

- mindspore 2.5.0

|   model name   | cards | resolution | scheduler | steps | s/step | s/video |
| :------------: | :---: | :--------: | :-------: | :---: | :----: | :-----: |
| AnimateDiff v2 |   1   | 512x512x16 |   DDIM    |  30   |  0.64  |  19.2   |

### Training

- mindspore 2.5.0

|            method            | cards | batch size | resolution | flash attn | jit level | graph compile | s/step | img/s |
| :--------------------------: | ----- | :--------: | :--------: | :--------: | :-------: | :-----------: | :----: | :---: |
|         MM training          | 1     |     1      | 16x512x512 |     ON     |    O1     |    3~5mins    | 0.992  | 1.008 |
|         Motion Lora          | 1     |     1      | 16x512x512 |     ON     |    O1     |    3~5mins    | 1.304  | 0.767 |
| MM training w/ Embed. cached | 1     |     1      | 16x512x512 |     ON     |    O1     |    3~5mins    | 0.772  | 1.295 |
| Motion Lora w/ Embed. cached | 1     |     1      | 16x512x512 |     ON     |    O1     |    3~5mins    | 0.874  | 1.144 |

> MM training: Motion Module training.
> Embed. cached: The video embedding (VAE-encoder outputs) and text embedding are pre-computed and stored before diffusion training.
