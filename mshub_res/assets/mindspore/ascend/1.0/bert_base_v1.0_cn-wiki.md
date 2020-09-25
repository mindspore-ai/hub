# Bert

---

model-name: bert_base

backbone-name: BertModel

module-type: nlp

fine-tunable: True

input-shape: [[1, 128], [1, 128], [1, 128]]

model-version: 1.0

train-dataset: cn-wiki


author: MindSpore team

update-time: 2020-09-23

repo-link: https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/nlp/bert

user-id: MindSpore

used-for: inference/transfer-learning

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

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
import mindspore.dataset.engine.datasets as de
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.ops import operations as P
from model_zoo.official.nlp.bert.src.bert_model import BertConfig
from model_zoo.official.nlp.bert.src import GetMaskedLMOutput

context.set_context(mode=context.GRAPH_MODE, device_target="Ascend", device_id=0)
model = "mindspore/ascend/1.0/bert_base_v1.0_cn-wiki"

bert_base_cfg = BertConfig(
    seq_length=128,
    vocab_size=21128,
    hidden_size=768,
    num_hidden_layers=12,
    num_attention_heads=12,
    intermediate_size=3072,
    hidden_act="gelu",
    hidden_dropout_prob=0.0,
    attention_probs_dropout_prob=0.0,
    max_position_embeddings=512,
    type_vocab_size=2,
    initializer_range=0.02,
    use_relative_positions=False,
    dtype=mstype.float32,
    compute_type=mstype.float16
)


class MLM(nn.Cell):
    def __init__(self, config):
        super(MLM, self).__init__()
        network = mshub.load(model, is_training=False)
        network.set_train(False)
        self.bert = network
        self.cls1 = GetMaskedLMOutput(config)
        self.cast = P.Cast()
        self.argmax = P.Argmax(axis=-1, output_type=mstype.int32)
    
    def construct(self, input_ids, input_mask, token_type_id, masked_pos):
        input_ids = self.cast(input_ids, mstype.int32)
        input_mask = self.cast(input_mask, mstype.int32)
        token_type_id = self.cast(token_type_id, mstype.int32)
        masked_pos = self.cast(masked_pos, mstype.int32)
        sequence_output, _, embedding_table = self.bert(input_ids, token_type_id, input_mask)
        prediction_scores = self.cls1(sequence_output, embedding_table, masked_pos)
        index = self.argmax(prediction_scores)
        return index

columns_list=["input_ids", "input_mask", "segment_ids", "masked_lm_positions"]
# data_files can be cn-wiki tfrecord
ds = de.TFRecordDataset(data_files, None, columns_list=columns_list)
mlm_net = MLM(bert_base_cfg)
for data in ds.create_dict_iterator():
    input_data = []
    for i in columns_list:
        input_data.append(Tensor(data[i]))
    input_ids, input_mask, segment_ids, masked_lm_positions = input_data
    out = mlm_net(input_ids, input_mask, segment_ids, masked_lm_positions)
    print("net output: ", out)
# For more downstream tasks, please refer to https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/nlp/bert
```
 
## Citation
Paper: Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. arXiv preprint arXiv:1810.04805. 
