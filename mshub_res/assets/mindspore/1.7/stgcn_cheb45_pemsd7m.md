# stgcn

---

model-name: stgcn

backbone-name: stgcn

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: pemsd7m

evaluation: mae3.22 | mape8.37 | rmse6.09

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/research/cv/stgcn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/stgcn_cheb45_ascend_v170_pemsd7m_research_cv_mae3.22_mape8.37_rmse6.09.ckpt>
    asset-sha256: 75da728efa227e2c6333d5a529d190c8dfb14eea475c7e4dc780d08acd0d2645

license: Apache2.0

summary: stgcn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of stgcn from the MindSpore model zoo on Gitee at research/cv/stgcn.

stgcn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/stgcn](https://gitee.com/mindspore/models/blob/r1.7/research/cv/stgcn/README_CN.md).

All parameters in the module are trainable.

## Citation

Bing yu, Haoteng Yin, and Zhanxing Zhu. "Spatio-Temporal Graph Convolutional Networks: A Deep Learning Framework for Traffic Forecasting." Proceedings of the 27th International Joint Conference on Artificial Intelligence. 2017.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
