# wide_and_deep

---

model-name: wide_and_deep

backbone-name: wide_and_deep

module-type: recommend

fine-tunable: True

input-shape: [[131072], [131072, 32], [131072, 5], [131072, 3], [131072, 8], [131072, 3],
[131072, 3], [131072, 6], [131072, 6], [131072, 6], [131072, 6], [131072, 3], [131072, 3],
[131072, 3], [131072, 3], [131072, 3], [131072, 3], [131072, 1], [131072, 1], [131072, 1],
[131072, 1]]

model-version: 1.0

Auc Score: 0.7473

author: MindSpore team

update-time: 2020-09-21

repo-link: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/recommend/wide_and_deep_multitable>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 0.7

license: Apache2.0

summary: wide_and_deep_multitable used in recommend system

---

## Introduction

This MindSpore Hub model uses the implementation of wide&deep from the MindSpore model zoo on Gitee at model_zoo/official/recommend/wide_and_deep_multitable.

## Citation

1. Cheng H T , Koc L , Harmsen J , et al. Wide & Deep Learning for Recommender Systems[J]. 2016.
