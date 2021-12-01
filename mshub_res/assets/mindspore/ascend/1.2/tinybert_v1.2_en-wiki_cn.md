# TinyBert

---

模型名称：TinyBERT

骨干网络： TinyBertModel

模块类型：NLP

可微调：True

输入形状：[[1, 128], [1, 128], [1, 128]]

模型版本：1.2

训练数据集：en-wiki

作者：MindSpore团队

更新时间：2021-3-26

代码仓链接：<https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/nlp/tinybert>。

用户ID：MindSpore

用途：推理/迁移学习

训练后端：Ascend

推理后端：Ascend

MindSpore版本：1.2

资源：

  -
    文件格式：.ckpt  
    资源链接：<https://download.mindspore.cn/model_zoo/official/nlp/tinybert/tinybert_ascend_1.2_en-wiki_official_nlp_20210326/bert_base_ascend_1.2_en-wiki.ckpt>  
    资源SHA256校验码： a62718990ca7dd8ce8982f9f2dc57a4dcd03e05945f234b6467539436907a03a
    资源链接：<https://download.mindspore.cn/model_zoo/official/nlp/tinybert/tinybert_ascend_1.2_en-wiki_official_nlp_20210326/bert_base_finetune_ascend_1.2_sst2.ckpt>  
    资源SHA256校验码： 286596339651a16b6fa70dd077e4cc11e0baef9a318eaa2ada4457de63d98d07
    资源链接：<https://download.mindspore.cn/model_zoo/official/nlp/tinybert/tinybert_ascend_1.2_en-wiki_official_nlp_20210326/bert_base_finetune_ascend_1.2_mnli.ckpt>  
    资源SHA256校验码： e8892e2491b238bfac88dd9843a7cb17a322a5c57dc194bbcfb2801ba6b68e62
    资源链接：<https://download.mindspore.cn/model_zoo/official/nlp/tinybert/tinybert_ascend_1.2_en-wiki_official_nlp_20210326/bert_base_finetune_ascend_1.2_qnli.ckpt>  
    资源SHA256校验码： 89eb32e1d9e54bde96f239406b9701bd8457e2be814e4338e5d2507b88110f20

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
model = "mindspore/ascend/1.0/tinybert_v1.2_en-wiki"
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

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.