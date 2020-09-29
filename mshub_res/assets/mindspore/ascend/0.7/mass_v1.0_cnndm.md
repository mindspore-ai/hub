# MASS 

---

model-name: mass

backbone-name: MassModel

module-type: nlp

fine-tunable: True

input-shape: [[1, 128], [1, 128], [1, 128], [1, 128], [1, 128], [1, 128]]

model-version: 1.0


author: MindSpore team

update-time: 2020-09-21

repo-link: https://gitee.com/mindspore/mindspore/tree/r0.7/model_zoo/official/nlp/mass

user-id: MindSpore

used-for: inference/transfer-learning

train-backend: ascend

infer-backend: ascend

mindspore-version: 0.7

license: Apache2.0
summary: mass used to do conversation response on various dataset.
---

## Introduction

This MindSpore Hub model uses the implementation of MASSModel from the MindSpore model zoo on Gitee at model_zoo/official/nlp/mass.

This model has been trained on cnndm using the code published on Gitee.

All Parameters in the module are trainable.

## Usage

Refer to the readme description and code of modelzoo for specific usage:
https://gitee.com/mindspore/mindspore/tree/r0.7/model_zoo/official/nlp/mass/README.md
 
## Citation
Paper: Song, Kaitao, Xu Tan, Tao Qin, Jianfeng Lu and Tie-Yan Liu. “MASS: Masked Sequence to Sequence Pre-training for Language Generation.” ICML (2019).
