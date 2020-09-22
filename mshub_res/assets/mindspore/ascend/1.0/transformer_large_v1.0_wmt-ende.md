# Transformer

---

model-name: transformer_large

backbone-name: TransformerModel

module-type: nlp

fine-tunable: True

input-shape: [[1, 128], [1, 128], [1, 128], [1, 128]]

model-version: 1.0

train-dataset: WMT


author: MindSpore team

update-time: 2020-09-21

repo-link: https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/nlp/transformer

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

license: Apache2.0
summary: transformer_large used to do machine translation.
---

## Introduction

This MindSpore Hub model uses the implementation of TransformerModel from the MindSpore model zoo on Gitee at model_zoo/official/nlp/transformer.

This model has been trained on wmt-ende using the code published on Gitee. This model support dynamic input shape depanding on the input sequence length, max sequence length is 128. 

All Parameters in the module are trainable.

## Usage

Refer to the readme description and code of modelzoo for specific usage:
https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/nlp/transformer
 
## Citation
Paper: Ashish Vaswani, Noam Shazeer, Niki Parmar, JakobUszkoreit, Llion Jones, Aidan N Gomez, Ł ukaszKaiser, and Illia Polosukhin. 2017. Attention is all you need. In NIPS 2017, pages 5998–6008.
