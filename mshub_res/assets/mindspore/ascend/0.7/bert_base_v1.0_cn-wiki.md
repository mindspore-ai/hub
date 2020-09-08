# Bert
 
---
 
model-name: bert_base
 
backbone-name: BertModel
 
module-type: NLP
 
fine-tunable: True
 
input-shape: [[1, 128], [1, 128], [1, 128]]

model-version: 1.0
 
train-dataset: cn-wiki
 
 
 
author: mindspore
 
update-time: 2020-09-07
 
repo-link: https://gitee.com/mindspore/mindspore/tree/r0.7/model_zoo/official/nlp/bert
 
user-id: mindspore
 
used-for: inference/transfer-learning
 
train-backend: ascend
 
infer-backend: ascend
 
mindspore-version: 0.7

asset:
  -
    file-format: ckpt
    asset-link: https://download.mindspore.cn/model_zoo/official/nlp/bert/bert_base_ascend_0.5.0_cn-wiki_official_nlp_20200720/bert_base.ckpt
    asset-sha256: 1cec4ec74dcf8e182b97e97a96e0d71a3911ec1b2aa25583a5930240ef962571
 
license: Apache2.0
summary: bert_base used to do classification, sequence labeling or squad tasks on various dataset.
---
 
## Introduction
 
This MindSpore Hub model uses the implementation of BertModel from the MindSpore model zoo on Gitee at model_zoo/official/nlp/bert.

This model has been trained on cn-wiki using the code published on Gitee.
 
All Parameters in the module are trainable.
 
## Usage
 
```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
 
context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)
 
model = "mindspore/ascend/0.7/bert_base_v1.0_cn-wiki"
 
network = mshub.load(model)
network.set_train(False)
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
