# AutoEncoders

---

model-name: AutoEncoders

backbone-name: vae

module-type: mm

fine-tunable: True

model-version: 2.5

train-dataset: CelebA-HQ

evaluation: PSNR32.58 | SSIM0.91

author: MindSpore team

update-time: 2025-04-22

repo-link: <https://github.com/mindspore-lab/mindone/tree/v0.3.0/examples/autoencoders>

user-id: MindSpore

used-for: inference

mindspore-version: 2.5

license: Apache2.0

summary: AutoEncoders is used for image reconstruction and generation

---

# AutoEncoders based on MindSpore

This repository contains SoTA image and video autoencoders and their training and inference pipelines implemented with MindSpore.

## Features

- VAE (Image Variational AutoEncoder)
    - ✔ KL-reg with GAN loss (SD VAE)
    - ✔ VQ-reg with GAN loss (VQ-GAN)

## Requirements

| mindspore | ascend driver |  firmware   | cann toolkit/kernel |
| :-------: | :-----------: | :---------: | :-----------------: |
|   2.5.0   |   24.1.RC3    | 7.3.0.1.231 |    8.0.RC3.beta1    |

```shell
pip install -r requirements.txt
```

## Variational Autoencoder (VAE)

### Training

Please download the [lpips_vgg-426bf45c.ckpt](https://download-mindspore.osinfra.cn/toolkits/mindone/autoencoders/lpips_vgg-426bf45c.ckpt) checkpoint and put it under `models/`.

To train a VAE, please run

```shell
python train.py --config configs/training/your_train_receipe.yaml
```

For example, to train VAE-kl-f8 model on CelebA-HQ dataset, you can run

```shell
python train.py --config configs/training/vae_celeba.yaml
```

after setting the `data_path` argument to the dataset path.

Note that you can either set arguments by editing the yaml file, or parsing by CLI (e.g. appending `--data_path=datasets/celeba_hq/train` to the training command). The CLI arguments will overwrite the corresponding values in the base yaml config.

#### Key arguments

- `model_config`: path to a yaml config file defining the autoencoder architecture and loss. Default: "configs/autoencoder_kl_f8.yaml"
- `use_discriminator`: If True (please also set `mode:1` for VAE-vq), GAN adversarial training will be applied after `disc_start` steps (defined in model config). Default: False

<!--
Note that `calculate_adaptive_weight` is not used currently compared to torch GAN.
-->

For more arguments, please run `python train.py -h` to check.

### Evaluation

```shell
python infer.py \
    --model_config configs/autoencoder_kl_f8.yaml \
    --ckpt_path path/to/checkpoint \
    --data_path path/to/test_data \
    --size 256 \
```

After running it will save the reconstruction results in `samples/vae_recons` and report the PSNR and SSIM evaluation metrics by default.

For detailed arguments, please run `python infer.py -h`.

### Performance

We split the CelebA-HQ dataset into 24,000 images for training and 6,000 images for testing. Experiments are tested on Ascend Atlas 800T A2 machines with graph mode.

- mindspore 2.5.0

| model name | cards | batch size | resolution | precision | discriminator | jit_level | graph compile | s/step | img/s | PSNR↑ | SSIM↑ |
| :--------- | :---- | :--------- | :--------- | :-------- | :------------ | --------: | :-----------: | :----: | :---: | :---: | :---: |
| VAE-kl     | 1     | 12         | 256x256    | fp32      | OFF           |        O1 |     1 min     |  0.57  | 21.05 | 32.58 | 0.91  |
| VAE-vq     | 1     | 8          | 256x256    | fp32      | OFF           |        O1 |     1 min     |  0.36  | 22.22 | 29.66 | 0.87  |

Here are some reconstruction results (left is ground-truth, right is the reconstructed)

<p float="center">
<img src=https://github.com/SamitHuang/mindone/assets/8156835/ec7ceee8-13e0-4358-8a8a-8b5a3a3daa57 width="30%" />
<img src=https://github.com/SamitHuang/mindone/assets/8156835/595eb459-96e1-442d-9152-39e0d431ff04 width="30%" />
<img src=https://github.com/SamitHuang/mindone/assets/8156835/aecc813a-71e2-4a30-971a-061f82b63e7c width="30%" />
</p>
