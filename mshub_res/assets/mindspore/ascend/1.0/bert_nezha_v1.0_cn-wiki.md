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
from model_zoo.official.nlp.bert.src.bert_model import BertConfig
from model_zoo.official.nlp.bert.src import GetMaskedLMOutput

context.set_context(mode=context.GRAPH_MODE, device_target="Ascend", device_id=0)
model = "mindspore/ascend/1.0/bert_nezha_v1.0_cn-wiki"

bert_nezha_cfg = BertConfig(
    seq_length=128,
    vocab_size=21128,
    hidden_size=1024,
    num_hidden_layers=24,
    num_attention_heads=16,
    intermediate_size=4096,
    hidden_act="gelu",
    hidden_dropout_prob=0.0,
    attention_probs_dropout_prob=0.0,
    max_position_embeddings=512,
    type_vocab_size=2,
    initializer_range=0.02,
    use_relative_positions=True,
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

    def construct(self, input_ids, input_mask, token_type_id, masked_pos):
        sequence_output, _, embedding_table = self.bert(input_ids, token_type_id, input_mask)
        prediction_scores = self.cls1(sequence_output, embedding_table, masked_pos)
        return prediction_scores

columns_list=["input_ids", "input_mask", "segment_ids", "masked_lm_positions"]
# data_files can be cn-wiki tfrecord
ds = de.TFRecordDataset(data_files, None, columns_list=["input_ids", "input_mask", "segment_ids", "masked_lm_positions"])
mlm_net = MLM(bert_nezha_cfg)
for data in ds.create_dict_iterator():
    input_data = []
    for i in columns_list:
        input_data.append(Tensor(data[i]))
    input_ids, input_mask, segment_ids, masked_lm_positions = input_data
    out = mlm_net(input_ids, input_mask, segment_ids, masked_lm_positions)
# For more downstream tasks, please refer to https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/nlp/bert
```

## Citation
Paper: Junqiu Wei, Xiaozhe Ren, Xiaoguang Li, Wenyong Huang, Yi Liao, Yasheng Wang, Jiashu Lin, Xin Jiang, Xiao Chen, Qun Liu. NEZHA: Neural Contextualized Representation for Chinese Language Understanding. arXiv preprint arXiv:1909.00204.
