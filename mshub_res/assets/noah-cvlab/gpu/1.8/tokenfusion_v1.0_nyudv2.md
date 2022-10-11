# TokenFusion

---

model-name: TokenFusion

backbone-name: TokenFusion

module-type: cv-segmentation

fine-tunable: True

input-shape: [[640, 480, 3], [640, 480, 3]]

model-version: 1.0

train-dataset: NYUDv2

accuracy: 54.8

author: Noah's Ark Lab

update-time: 2022-08-13

repo-link: https://gitee.com/mindspore/models/tree/master/research/cv/TokenFusion

user-id: Noah's Ark Lab

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-version: 1.8

asset:

- file-format: ckpt

  asset-link: https://download.mindspore.cn/models/r1.8/tokenfusion_ascend_v180_nyudv2_research_cv_acc54.8.ckpt

  asset-sha256: aca709e5907ec3fca31fc003ca6b1d1e4d073a06e2a029ec84d9c5e13921bb2b

license: Apache2.0
summary: TokenFusion model for RGB-D semantic segmentation

---

## Introduction

This MindSpore Hub model uses the implementation of TokenFusion from the MindSpore model zoo on Gitee at models/tree/master/research/cv/TokenFusion.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context
from src.args import args

context.set_context(mode=context.PYNATIVE_MODE,
                    device_target="GPU",
                    device_id=0)

model = "mindspore/gpu/1.3/tokenfusion_v1.0_nyudv2"
network = mshub.load(model, args)
network.set_train(False)
```

## Citation

1. Yikai Wang, Xinghao Chen, Lele Cao, Wenbing Huang, Fuchun Sun, Yunhe Wang, [**Multimodal Token Fusion for Vision Transformers**](https://openaccess.thecvf.com/content/CVPR2022/papers/Wang_Multimodal_Token_Fusion_for_Vision_Transformers_CVPR_2022_paper.pdf), In **CVPR 2022**.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.