# tinybert

---

model-name: tinybert

backbone-name: tinybert

module-type: nlp

fine-tunable: True

model-version: 1.3

train-dataset: enwiki128_qnli

evaluation: acc88.86

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/official/nlp/tinybert>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/tinybert_ascend_v130_enwiki128_qnli_official_nlp_acc88.86.ckpt>
    asset-sha256: d33ae2a4548502bc392ed286d7dfb17102efc5ca8a9203b70b40df6a381d52ed

license: Apache2.0

summary: tinybert is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of tinybert from the MindSpore model zoo on Gitee at official/nlp/tinybert.

tinybert is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [official/nlp/tinybert](https://gitee.com/mindspore/models/blob/r1.3/official/nlp/tinybert/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.3/tinybert_enwiki128_qnli"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Xiaoqi Jiao, Yichun Yin, Lifeng Shang, Xin Jiang, Xiao Chen, Linlin Li, Fang Wang, Qun Liu. TinyBERT: Distilling BERT for Natural Language Understanding. arXiv preprint arXiv:1909.10351.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
