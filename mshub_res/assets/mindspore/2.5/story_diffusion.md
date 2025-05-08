# StoryDiffusion

---

model-name: StoryDiffusion

backbone-name: stable-diffusion

module-type: mm

fine-tunable: True

model-version: 2.5

train-dataset: N/A

author: MindSpore team

update-time: 2025-04-22

repo-link: <https://github.com/mindspore-lab/mindone/tree/v0.3.0/examples/story_diffusion>

user-id: MindSpore

used-for: inference

mindspore-version: 2.5

license: Apache2.0

summary: StoryDiffusion is a model for consistent long-range image and video generation

---

# StoryDiffusion: Consistent Self-Attention for Long-Range Image and Video Generation

This is an efficient MindSpore implementation of [StoryDiffusion](https://github.com/HVision-NKU/StoryDiffusion/tree/main)

## Introduction

StoryDiffusion can generate consistent images and videos given a set of text prompts. The major contributions are two-fold:

1. Consistent self-attention, a training-free and pluggable module with all SD1.5 and SDXL-based image diffusion models. Given at least 3 text prompts, it can generate images with consistent subjects and good text-vision alignment.
2. Motion predictor for long-range video generation, which can predict motion between condition images.

The current implementation only supports text-to-image generation with consistent self-attention.

## TODOs

- ✔ Comic Generation Inference script
- ✔ Gradio demo of comic generation
- ✖ Motion predictor with condition images

## 📦 Requirements

<div align="center">

| mindspore | ascend driver |  firmware   | cann toolkit/kernel |
| :-------: | :-----------: | :---------: | :-----------------: |
|   2.5.0   |   24.1.RC2    | 7.5.0.2.220 |    8.0.RC3.beta1    |

</div>

## Installation

1. Use python>=3.9 [[install]](https://www.python.org/downloads/)

2. Please install MindSpore 2.5.0 according to the [MindSpore official website](https://www.mindspore.cn/install/) and install [CANN 8.0.RC3.beta1](https://www.hiascend.com/developer/download/community/result?module=cann&cann=8.0.RC3.beta1) as recommended by the official installation website.

3. Install requirements

```bash
pip install -r requirements.txt
```

## Usage

### Comic Generation

Please run the following inference script to generate consistent images:

```shell
python run.py --general_prompt "a man with a black suit" --sd_model_name "RealVision" --style_name "Comic book" --output_dir "outputs"
```

This will generate some images under the folder named "outputs". These images are conditioned on a set of text prompts, like:

```text
a man with a black suit wake up in the bed,
a man with a black suit have breakfast,
...
```

Example images are shown below:

<p align="center">
  <img src="https://github.com/wtomin/mindone-assets/blob/main/story_diffusion/0-Comic%20book-RealVision_update.png?raw=true" width=550 />
</p>

<p align="center">
  <img src="https://github.com/wtomin/mindone-assets/blob/main/story_diffusion/1-Comic%20book-RealVision_update.png?raw=true" width=550 />
</p>

Now this inference script support the following SD-XL models:

```python
models_dict = {
    "Juggernaut": "RunDiffusion/Juggernaut-XL-v8",
    "RealVision": "SG161222/RealVisXL_V4.0",
    "SDXL": "stabilityai/stable-diffusion-xl-base-1.0",
    "Unstable": "stablediffusionapi/sdxl-unstable-diffusers-y",
}
```

The default cache directory is `./cache_dir`. If you have the model files downloaded and stored under `./cache_dir`, you can run the inference script append with `--local_files_only` to skip the downloading process.

### Local Gradio Demo

You can also start a local gradio demo by running:

```bash
python gradio_app_sdxl_specific_id_low_vram.py
```
