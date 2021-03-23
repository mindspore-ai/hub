# IPT-SRx2

---

model-name: IPT-SRx2

backbone-name: IPT

module-type: cv-super-resolution

fine-tunable: True

input-shape: [48, 48, 3]

model-version: 1.0

train-dataset: Set14

accuracy: 34.54

author: Noah CVLab

update-time: 2021-03-05

repo-link: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/research/cv/IPT>

user-id: noah-cvlab

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-version: 1.1

mindspore-lite: False

asset:

- file-format: ckpt

  asset-link: <https://download.mindspore.cn/model_zoo/research/cv/IPT/IPT_sr2.ckpt>

  asset-sha256: e067e506e8bbdbd6d6330f64badb3a033116d0ed5cb7cd827cf30b3496dc2be6

license: Apache2.0

summary: IPT used to do x2 super-resolution of Set14 dataset of PSNR 34.54dB

---

## Introduction

This MindSpore Hub model uses the implementation of IPT from the MindSpore model zoo on Gitee at model_zoo/research/cv/IPT.

## Usage

```python
import mindspore_hub as mshub

from mindspore import context

from src.args import args

context.set_context(mode=context.PYNATIVE_MODE,
                    device_target="GPU",
                    device_id=0)

model = "noah-cvlab/gpu/1.1/ipt_v1.0_Set14_SR_x2"
network = mshub.load(model, args)

network.set_train(False)
```

## Citation

[1] Hanting Chen, Yunhe Wang, Tianyu Guo, Chang Xu, Yiping Deng, Zhenhua Liu, Siwei Ma, Chunjing Xu, Chao Xu, and Wen Gao. **"Pre-trained image processing transformer"**. <i>**CVPR 2021**.</i>