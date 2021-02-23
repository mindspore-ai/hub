# TinyBert

---

模型名称：TinyBERT

骨干网络： TinyBertModel

模块类型：NLP

可微调：True

输入形状：[[1, 128], [1, 128], [1, 128]]

模型版本：1.0

训练数据集：cn-wiki

作者：MindSpore团队

更新时间：2020-9-22

代码仓链接：<https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/nlp/tinybert>。

用户ID：MindSpore

用途：推理/迁移学习

训练后端：Ascend

推理后端：Ascend

MindSpore版本：1.0

资源：

  -
    文件格式：.ckpt  
    资源链接：<https://download.mindspore.cn/model_zoo/official/nlp/tinybert/tinybert_ascend_1.0_cn-wiki_official_nlp_20200922/tinybert.ckpt>  
    资源SHA256校验码： 7f528d70605affc5c2fc0901a729444dc45cfa5bd72fc2fb742c8a3ff4d878b6

许可证：Apache 2.0

摘要：使用TinyBert对各种数据集进行分类、序列标记或SQuAD任务。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的TinyBertModel实现，目录为model_zoo/official/nlp/tinybert。

使用已在码云上发布的代码在cn-wiki数据集上训练该模型。

模块中所有参数均可训练。

## 用法

```python
import mindspore_hub as mshub
import mindspore
import mindspore.common.dtype as mstype
import mindspore.dataset.engine.datasets as de
import mindspore.dataset.transforms.c_transforms as C
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from model_zoo.official.nlp.tinybert.src.dataset import create_tinybert_dataset

context.set_context(mode=context.GRAPH_MODE, device_target="Ascend", device_id=0)
model = "mindspore/ascend/1.0/tinybert_v1.0_cn-wiki"
network = mshub.load(model, is_training=False)
network.set_train(False)
# 数据目录可以为GLUE数据集目录
dataset = create_tinybert_dataset('td', data_dir=data_dir)

columns_list = ["input_ids", "input_mask", "segment_ids", "label_ids"]
for data in dataset.create_dict_iterator():
    input_data = []
    for i in columns_list:
        input_data.append(data[i])
    input_ids, input_mask, token_type_id, label_ids = input_data
    logits = network(input_ids, token_type_id, input_mask)
    print("net output: ", logits)
# 更多下游任务，请参考https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/nlp/tinybert
```

## 参考论文

论文： Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. arXiv preprint arXiv:1810.04805.
