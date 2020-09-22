# Bert

---

model-name: bert_thor

backbone-name: BertModel

module-type: nlp

fine-tunable: True

input-shape: [12, 512]

model-version: 1.0

train-dataset: MLPerf v0.7 dataset


author: MindSpore team

update-time: 2020-09-22

repo-link: https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/nlp/bert_thor

user-id: MindSpore

used-for: inference/transfer-learning

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

asset:
  -
    file-format: ckpt
    asset-link: https://download.mindspore.cn/model_zoo/official/nlp/bert_thor/bert_thor_ascend_1.0_mlperf_v0.7_dataset_official_nlp_20200922/bert_thor.ckpt
    asset-sha256: 225354d0f82eda03ee9779e325042f1527fa92bf7f517a3d1b50794a9473586d

license: Apache2.0
summary: bert_thor used to do classification, sequence labeling or squad tasks on various dataset.
---

## Introduction

This MindSpore Hub model uses the implementation of BertModel from the MindSpore model zoo on Gitee at model_zoo/official/nlp/bert_thor.

This model has been trained on MLPerf v0.7 dataset using the code published on Gitee.

All Parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
import mindspore.dataset.engine.datasets as de
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype

context.set_context(mode=context.GRAPH_MODE, device_target="Ascend", device_id=0)

model = "mindspore/ascend/1.0/bert_thor_v1.0_MLPerf_v0.7_dataset"

network = mshub.load(model, is_training=False, batch_size=12)
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
Paper: Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. arXiv preprint arXiv:1810.04805. 
