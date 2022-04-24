# ddpg

---

model-name: ddpg

backbone-name: ddpg

module-type: rl

fine-tunable: True

model-version: 1.5

train-dataset: none

evaluation: avgReward-9.11

author: MindSpore team

update-time: 2022-04-24

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/research/rl/ddpg>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/ddpg_actortarget_ascend_v150_none_research_rl_avgReward-9.11.ckpt>
    asset-sha256: 1b56c1d5f5abe913d41ec0af3f7f129eb703756d549f98189225fff9a3afaf92

license: Apache2.0

summary: ddpg is used for rl

---

## Introduction

This MindSpore Hub model uses the implementation of ddpg from the MindSpore model zoo on Gitee at research/rl/ddpg.

ddpg is a rl network. More details please refer to the MindSpore model zoo on Gitee at [research/rl/ddpg](https://gitee.com/mindspore/models/blob/r1.5/research/rl/ddpg/README_CN.md).

All parameters in the module are trainable.

## Citation

Timothy P. Lillicrap,Jonathan J. Hunt,Alexander Pritzel,Nicolas Heess,Tom Erez,Yuval Tassa,David Silver,Daan Wierstra. Continuous control with deep reinforcement learning.[J]. CoRR,2015,abs/1509.02971

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
