# VEnhancer

---

model-name: VEnhancer

backbone-name: diffusion

module-type: mm

fine-tunable: True

model-version: 2.5

train-dataset: N/A

author: MindSpore team

update-time: 2025-04-22

repo-link: <https://github.com/mindspore-lab/mindone/tree/v0.3.0/examples/venhancer>

user-id: MindSpore

used-for: inference

mindspore-version: 2.5

license: Apache2.0

summary: VEnhancer is a generative space-time enhancement framework for video generation

---

# VEnhancer based on MindSpore

This repository is the MindSpore implementation of [VEnhancer](https://arxiv.org/abs/2407.07667)[<a href="#references">1</a>].

VEnhancer, a generative space-time enhancement framework that improves the existing text-to-video results by adding more details in spatial domain and synthetic detailed motion in temporal domain. Given a generated low-quality video, VEnhancer can increase its spatial and temporal resolution simultaneously with arbitrary up-sampling space and time scales through a unified video diffusion model. Furthermore, VEnhancer effectively removes generated spatial artifacts and temporal flickering of generated videos.

<p align="center">
  <img src="https://github.com/user-attachments/assets/bfe97a4a-ba0e-482a-80c4-ecccf86362f6" width=900 />
</p>
<p align="center">
  <em> Figure 1. The Model Structure of VEnhancer. [<a href="#references">1</a>] </em>
</p>

## Requirements

| mindspore | ascend driver |  firmware   | cann toolkit/kernel |
| :-------: | :-----------: | :---------: | :-----------------: |
|   2.5.0   |   24.1.RC3    | 7.3.0.1.231 |    8.0.RC3.beta1    |

```shell
pip install -r requirements.txt
conda install ffmpeg
```

## Demo

The following videos are generated based on MindSpore and Ascend Atlas 800T A2 machines.

|                                                  Input                                                  |                                                             +VEnhancer                                                              |
| :-----------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------: |
| <img src="https://github.com/user-attachments/assets/77a8f492-b5d4-4f4c-910f-e89f22a9c41d" width="380"> | <img src="https://gitee.com/liuchuting/hub/raw/source/mshub_res/assets/mindspore/2.5/source/output_astronaut.gif" width="380"> |

## Inference

### Prepare model weights

We provide weight conversion script `tools/convert_weight.py` to convert the original Pytorch model weights to MindSpore model weights. Pytorch model weights can be accessed via links below.

|           model name            |                                          Description                                          |                                   pytorch checkpoint                                    |
| :-----------------------------: | :-------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------: |
|       VEnhancer_paper.pt        |    very creative, strong refinement, but sometimes over-smooths edges and texture details.    | [download link](https://huggingface.co/jwhejwhe/VEnhancer/blob/main/venhancer_paper.pt) |
|         VEnhancer_v2.pt         | less creative, but can generate better texture details, and has better identity preservation. |  [download link](https://huggingface.co/jwhejwhe/VEnhancer/blob/main/venhancer_v2.pt)   |
| CLIP-ViT-H-14-laion2B-s32B-b79K |                                               /                                               | [download link](https://huggingface.co/laion/CLIP-ViT-H-14-laion2B-s32B-b79K/tree/main) |

The text files in `tools/` mark the model parameters mapping between Pytorch and MindSpore version. Set `--model_name` as one of ["unet", "clip"] according to the model you want to convert, and then run the following command to convert weight.

```shell
cd tools
python convert_weight.py \
    --model_name "clip" \
    --src /path/to/pt/open_clip_pytorch_model.bin \
    --target ../models/open_clip.ckpt
```

**Note** Please covert `CLIP-ViT-H-14-laion2B-s32B-b79K` from pytorch to mindspore, and name it `open_clip.ckpt` and place it as follow,

```text
models
   ├── open_clip.ckpt
   ├── VEnhancer_paper.pt
```

### dataset

You can download prompts and input videos form this [URL](https://github.com/Vchitect/VEnhancer/tree/main/prompts).

### Run inference

```shell
bash scripts/run_infer.sh
```

### Performance

Experiments are tested on Ascend Atlas 800T A2 machines with pynative mode.

- mindspore 2.5.0

| model name | cards | batch size |  resolution  | sampler | steps | precision | jit level | graph compile | s/step | s/video |
| :--------: | :---: | :--------: | :----------: | :-----: | :---: | :-------: | :-------: | :-----------: | :----: | :-----: |
| VEnhancer  |   1   |     1      | 31x1214x1942 |  heun   |  15   |   fp16    |     /     |       /       | 51.69  |   926   |

## References

[1] He J, Xue T, Liu D, et al. VEnhancer: Generative Space-Time Enhancement for Video Generation[J]. arXiv preprint arXiv:2407.07667,2024.
