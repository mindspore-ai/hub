# wave_mlp

---

model-name: wave_mlp

backbone-name: wave_mlp

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: imagenet2012

evaluation: top1acc80.7

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/wave_mlp>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/wavemlp_ascend_v190_imagenet2012_research_cv_top1acc80.7.ckpt>
    asset-sha256: 93f94387830ccd79382cf8aab493c918f8f3f479d7d8a3bb940ca2db7370661f

license: Apache2.0

summary: wave_mlp is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of wave_mlp from the MindSpore model zoo on Gitee at research/cv/wave_mlp.

wave_mlp is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/wave_mlp](https://gitee.com/mindspore/models/blob/r1.9/research/cv/wave_mlp/README.md).

All parameters in the module are trainable.

## Citation

Yehui Tang, Kai Han, Jianyuan Guo, Chang Xu, Yanxi Li, Chao Xu, Yunhe Wang. An Image Patch is a Wave: Phase-Aware Vision MLP. arxiv 2111.12294.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
