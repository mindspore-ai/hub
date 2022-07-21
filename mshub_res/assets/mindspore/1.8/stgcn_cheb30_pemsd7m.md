# stgcn

---

model-name: stgcn

backbone-name: stgcn

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: pemsd7m

evaluation: mae2.89 | mape7.35 | rmse5.43

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/stgcn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/stgcn_cheb30_ascend_v180_pemsd7m_research_cv_mae2.89_mape7.35_rmse5.43.ckpt>
    asset-sha256: 8ff99b5672b05a8df426d9a2c465cbcb2cdfffaf6234408ab917c4c1e946563d

license: Apache2.0

summary: stgcn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of stgcn from the MindSpore model zoo on Gitee at research/cv/stgcn.

stgcn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/stgcn](https://gitee.com/mindspore/models/blob/r1.8/research/cv/stgcn/README_CN.md).

All parameters in the module are trainable.

## Citation

Bing yu, Haoteng Yin, and Zhanxing Zhu. "Spatio-Temporal Graph Convolutional Networks: A Deep Learning Framework for Traffic Forecasting." Proceedings of the 27th International Joint Conference on Artificial Intelligence. 2017.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
