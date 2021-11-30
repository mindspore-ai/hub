# BERT

---

模型名称：bert_nezha

骨干网络： BertModel

模块类型：NLP

可微调：True

输入形状： [[1, 128], [1, 128], [1, 128]]

模型版本：1.0

训练数据集：cn-wiki

作者：MindSpore团队

更新时间：2020-9-23

代码仓链接：<https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/nlp/bert>

用户ID：MindSpore

用途：推理/迁移学习

训练后端：Ascend

推理后端：Ascend

MindSpore版本：1.0

资源：

  -
    文件格式：.ckpt  
    资源链接： <https://download.mindspore.cn/model_zoo/official/nlp/bert/bert_nezha_ascend_0.5.0_cn-wiki_official_nlp_20200720/bert_NEZHA_large.ckpt>  
    资源SHA256校验码： 9318c64997db20c1e1cc51bf4e9c70b44ca7d724382f6cb96192647f2cebac78

许可证：Apache 2.0

摘要：使用bert_nezha对各种数据集进行分类、序列标记或SQuAD任务。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的BertModel实现，目录为model_zoo/official/nlp/bert。

使用已在码云上发布的代码在cn-wiki 数据集上训练该模型。

模块中所有参数均可训练。

## 用法

```python
import mindspore_hub as mshub
import mindspore
import mindspore.dataset.engine.datasets as de
from mindspore import context, Tensor
from mindspore.common import dtype as mstype
from mindspore.ops import operations as P
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
# data_files可以是cn-wiki TFRecord
ds = de.TFRecordDataset(data_files, None, columns_list=columns_list)
mlm_net = MLM(bert_nezha_cfg)
for data in ds.create_dict_iterator():
    input_data = []
    for i in columns_list:
        input_data.append(Tensor(data[i]))
    input_ids, input_mask, segment_ids, masked_lm_positions = input_data
    out = mlm_net(input_ids, input_mask, segment_ids, masked_lm_positions)
    print("net output: ", out)
# 更多下游任务，请参考https://gitee.com/mindspore/models/tree/master/official/nlp/bert。
```

## 参考论文

论文： Junqiu Wei, Xiaozhe Ren, Xiaoguang Li, Wenyong Huang, Yi Liao, Yasheng Wang, Jiashu Lin, Xin Jiang, Xiao Chen, Qun Liu. NEZHA: Neural Contextualized Representation for Chinese Language Understanding. arXiv preprint arXiv:1909.00204.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.