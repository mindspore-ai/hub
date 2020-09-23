# Warpctc

---

model-name: warpctc

backbone-name: LSTM

module-type: cv

fine-tunable: False

input-shape: [64, 3, 64, 160]

model-version: 1.0

train-dataset: captcha 0.1.1

author: MindSpore team

update-time: 2020-09-23

repo-link: https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/cv/warpctc

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

license: Apache2.0

summary: warpctc used to do captcha recognition.

---

## Introduction

This MindSpore Hub model uses the implementation of Warpctc Model from the MindSpore model zoo on Gitee at model_zoo/official/cv/warpctc.

This model has been trained on captcha using the code published on Gitee.
All Parameters in the module are trainable.

## Usage

Refer to the readme description and code of modelzoo for specific usage:
https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/cv/warpctc
