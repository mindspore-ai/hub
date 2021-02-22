# LSTM

---

model-name: lstm

backbone-name: SentimentNet

module-type: nlp

fine-tunable: True

input-shape: [64, 500, 300]

model-version: 1.0

accuracy: 0.82

author: MindSpore team

update-time: 2020-08-26

repo-link: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/nlp/lstm>

user-id: MindSpore

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-version: 1.0

license: Apache2.0

summary: lstm used to classify 2 classes of aclimdb

---

## Introduction

This MindSpore Hub model uses the implementation of lstm from the MindSpore model zoo on Gitee at model_zoo/official/nlp/lstm.

This model has been trained on AclImdb using the code published on Gitee.

All Parameters in the module are trainable.

## Citation

1. [Paper](https://www.aclweb.org/anthology/P11-1015/):  Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, Christopher Potts. [Learning Word Vectors for Sentiment Analysis](https://www.aclweb.org/anthology/P11-1015/). Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies. 2011
