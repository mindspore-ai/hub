# IPT

---

model-name: IPT

backbone-name: IPT

module-type: cv-derain

fine-tunable: True

input-shape: [48, 48, 3]

model-version: 1.0

train-dataset: Rain100L

accuracy: 41.98

author: Noah CVLab

update-time: 2021-03-05

repo-link: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/research/cv/IPT>

user-id: noah-cvlab

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

mindspore-lite: False

asset:

- file-format: ckpt

  asset-link: <https://download.mindspore.cn/model_zoo/research/cv/IPT/IPT_derain.ckpt>

  asset-sha256: 4d4876ca02c4c4564d1484685601a947e9dd47379b9e4719b3e8f31e09b28685

license: Apache2.0

summary: IPT used to do derain of Rain100L dataset of PSNR 41.98dB

---

## Usage

```python
import mindspore_hub as mshub

from mindspore import context

from src.args import args

context.set_context(mode=context.GRAPH_MODE,
                    device_target="ASCEND",
                    device_id=0)

model = "noah-cvlab/ascend/1.1/ipt_v1.0_Rain100L_derain"
network = mshub.load(model, args)

network.set_train(False)
```

## Citation

[1] Hanting Chen, Yunhe Wang, Tianyu Guo, Chang Xu, Yiping Deng, Zhenhua Liu, Siwei Ma, Chunjing Xu, Chao Xu, and Wen Gao. **"Pre-trained image processing transformer"**. <i>**CVPR 2021**.</i>