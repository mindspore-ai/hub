# BERT

---

模型名称：bert_thor

骨干网络：BertModel

模块类型：NLP

可微调：True

输入形状： [12, 512]

模型版本：1.0

训练数据集：MLPerf v0.7

作者：MindSpore团队

更新时间：2020-9-22

代码仓链接：<https://gitee.com/mindspore/models/tree/master/official/nlp/bert_thor>

用户ID：MindSpore

用途：推理/迁移学习

训练后端：Ascend

推理后端：Ascend

MindSpore版本：1.0

资源：

  -
    文件格式：.ckpt  
    资源链接：<https://download.mindspore.cn/model_zoo/official/nlp/bert_thor/bert_thor_ascend_1.0_mlperf_v0.7_dataset_official_nlp_20200922/bert_thor.ckpt>  
    资源SHA256校验码： 225354d0f82eda03ee9779e325042f1527fa92bf7f517a3d1b50794a9473586d

许可证：Apache 2.0

摘要：使用bert_thor对各种数据集进行分类、序列标记或SQuAD任务。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的BertModel实现，目录为model_zoo/official/nlp/bert_thor。

使用已在码云上发布的代码在MLPerf v0.7数据集上训练该模型。

模块中所有参数均可训练。

## 用法

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

## 参考论文

论文： Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. arXiv preprint arXiv:1810.04805.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.