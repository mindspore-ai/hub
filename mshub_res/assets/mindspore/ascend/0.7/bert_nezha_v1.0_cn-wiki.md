# Bert

---

model-name: bert_nezha

backbone-name: BertModel

module-type: nlp

fine-tunable: True

input-shape: [[1, 128], [1, 128], [1, 128]]

model-version: 1.0

train-dataset: cn-wiki


author: MindSpore team

update-time: 2020-09-07

repo-link: https://gitee.com/mindspore/mindspore/tree/r0.7/model_zoo/official/nlp/bert

user-id: MindSpore

used-for: inference/transfer-learning

train-backend: ascend

infer-backend: ascend

mindspore-version: 0.7

asset:
  -
    file-format: ckpt
    asset-link: https://download.mindspore.cn/model_zoo/official/nlp/bert/bert_nezha_ascend_0.5.0_cn-wiki_official_nlp_20200720/bert_NEZHA_large.ckpt
    asset-sha256: 9318c64997db20c1e1cc51bf4e9c70b44ca7d724382f6cb96192647f2cebac78

license: Apache2.0
summary: bert_nezha used to do classification, sequence labeling or squad tasks on various dataset.
---

## Introduction

This MindSpore Hub model uses the implementation of BertModel from the MindSpore model zoo on Gitee at model_zoo/official/nlp/bert.

This model has been trained on cn-wiki using the code published on Gitee.

All Parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
import mindspore.dataset.engine.datasets as de
from mindspore import context, Tensor
from mindspore.common import dtype as mstype

context.set_context(mode=context.GRAPH_MODE, device_target="Ascend", device_id=0)
model = "mindspore/ascend/0.7/bert_nezha_v1.0_cn-wiki"
network = mshub.load(model, is_training=False, batch_size=1)
network.set_train(False)
columns_list=["input_ids", "input_mask", "segment_ids"]
ds = de.TFRecordDataset(data_files, None, columns_list=["input_ids", "input_mask", "segment_ids"])
for data in ds.create_dict_iterator():
    input_data = []
    for i in columns_list:
        input_data.append(Tensor(data[i]))
    input_ids, input_mask, segment_ids = input_data
    out = network(input_ids, segment_ids, input_mask)
```

## Citation
Paper: Junqiu Wei, Xiaozhe Ren, Xiaoguang Li, Wenyong Huang, Yi Liao, Yasheng Wang, Jiashu Lin, Xin Jiang, Xiao Chen, Qun Liu. NEZHA: Neural Contextualized Representation for Chinese Language Understanding. arXiv preprint arXiv:1909.00204.
