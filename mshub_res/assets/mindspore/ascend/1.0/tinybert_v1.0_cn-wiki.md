# TinyBert

---

model-name: tinybert

backbone-name: TinyBertModel

module-type: nlp

fine-tunable: True

input-shape: [[1, 128], [1, 128], [1, 128]]

model-version: 1.0

train-dataset: cn-wiki


author: MindSpore team

update-time: 2020-09-22

repo-link: https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/nlp/tinybert

user-id: MindSpore

used-for: inference/transfer-learning

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

asset:
  -
    file-format: ckpt
    asset-link: https://download.mindspore.cn/model_zoo/official/nlp/tinybert/tinybert_ascend_1.0_cn-wiki_official_nlp_20200922/tinybert.ckpt
    asset-sha256: 7f528d70605affc5c2fc0901a729444dc45cfa5bd72fc2fb742c8a3ff4d878b6

license: Apache2.0
summary: tinybert used to do classification, sequence labeling or squad tasks on various dataset.
---

## Introduction

This MindSpore Hub model uses the implementation of TinyBertModel from the MindSpore model zoo on Gitee at model_zoo/official/nlp/tinybert.

This model has been trained on cn-wiki using the code published on Gitee.

All Parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
import mindspore.dataset.engine.datasets as de
from mindspore import context, Tensor, nn
from mindspore.train.model import Model

context.set_context(mode=context.GRAPH_MODE, device_target="Ascend", device_id=0)
model = "mindspore/ascend/1.0/tinybert_v1.0_cn-wiki"
network = mshub.load(model, is_training=False)
network.set_train(False)

columns_list=["input_ids", "input_mask", "segment_ids", "masked_lm_positions"]
# data_files can be cn-wiki tfrecord
ds = de.TFRecordDataset(data_files, None, columns_list=["input_ids", "input_mask", "segment_ids"])
for data in ds.create_dict_iterator():
    input_data = []
    for i in columns_list:
        input_data.append(Tensor(data[i]))
    input_ids, input_mask, segment_ids = input_data
    out = network(input_ids, input_mask, segment_ids)
# For more downstream tasks, please refer to https://gitee.com/mindspore/mindspore/tree/v1.0/model_zoo/official/nlp/tinybert
```

## Citation
Paper: Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. arXiv preprint arXiv:1810.04805. 
