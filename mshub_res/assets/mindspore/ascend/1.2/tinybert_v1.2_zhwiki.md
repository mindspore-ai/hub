# tinybert

---

model-name: tinybert

backbone-name: tinybert

module-type: nlp

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: zhwiki

accuracy: 6

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/nlp/tinybert>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/tinybert_ascend_v120_zhwiki_official_nlp_bs1_acc6/tinybert_ascend_v120_zhwiki_official_nlp_bs1_acc6.ckpt>
    asset-sha256: 89771f6c27c791c351fe699fbb8da3e1c0bf5187aea2dfee5ac03711637ffc28

license: Apache2.0

summary: tinybert is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of tinybert from the MindSpore model zoo on Gitee at model_zoo/official/nlp/tinybert.

tinybert is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/nlp/tinybert](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/nlp/tinybert/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/tinybert_v1.2_zhwiki"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Xiaoqi Jiao, Yichun Yin, Lifeng Shang, Xin Jiang, Xiao Chen, Linlin Li, Fang Wang, Qun Liu. [TinyBERT: Distilling BERT for Natural Language Understanding](https://arxiv.org/abs/1909.10351). arXiv preprint arXiv:1909.10351.
