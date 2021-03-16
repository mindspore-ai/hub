# IPT

---

model-name: IPT

backbone-name: IPT

module-type: cv-super-resolution

fine-tunable: True

input-shape: [48, 48, 3]

model-version: 1.0

train-dataset: Set14

accuracy: 30.96

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

  asset-link: <https://download.mindspore.cn/model_zoo/research/cv/IPT/IPT_sr3.ckpt>

  asset-sha256: 2f81d98f91d7857d96aa9cb4dbbf9a614b635af5d5a50d32ebc9572918137859

license: Apache2.0

summary: IPT used to do x3 super-resolution of Set14 dataset of PNSR 30.96dB

---

## Usage

```python
import mindspore_hub as mshub

from mindspore import context

from src.args import args

context.set_context(mode=context.PYNATIVE_MODE,
                    device_target="GPU",
                    device_id=0)

model = "noah-cvlab/gpu/1.0/IPT_sr3"
network = mshub.load(model, args)

network.set_train(False)
```

## Citation

[1] Hanting Chen, Yunhe Wang, Tianyu Guo, Chang Xu, Yiping Deng, Zhenhua Liu, Siwei Ma, Chunjing Xu, Chao Xu, and Wen Gao. **"Pre-trained image processing transformer"**. <i>**CVPR 2021**.</i>