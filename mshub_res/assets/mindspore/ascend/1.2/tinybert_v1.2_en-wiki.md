# TinyBert

---

model-name: tinybert

backbone-name: TinyBertModel

module-type: nlp

fine-tunable: True

input-shape: [[1, 128], [1, 128], [1, 128]]

model-version: 1.2

train-dataset: en-wiki

author: MindSpore team

update-time: 2021-03-26

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/nlp/tinybert>

user-id: MindSpore

used-for: inference/transfer-learning

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

  -
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/official/nlp/tinybert/tinybert_ascend_1.2_en-wiki_official_nlp_20210326/bert_base_ascend_1.2_en-wiki.ckpt>
    asset-sha256: a62718990ca7dd8ce8982f9f2dc57a4dcd03e05945f234b6467539436907a03a
    asset-link: <https://download.mindspore.cn/model_zoo/official/nlp/tinybert/tinybert_ascend_1.2_en-wiki_official_nlp_20210326/bert_base_finetune_ascend_1.2_sst2.ckpt>
    asset-sha256: 286596339651a16b6fa70dd077e4cc11e0baef9a318eaa2ada4457de63d98d07
    asset-link: <https://download.mindspore.cn/model_zoo/official/nlp/tinybert/tinybert_ascend_1.2_en-wiki_official_nlp_20210326/bert_base_finetune_ascend_1.2_mnli.ckpt>
    asset-sha256: e8892e2491b238bfac88dd9843a7cb17a322a5c57dc194bbcfb2801ba6b68e62
    asset-link: <https://download.mindspore.cn/model_zoo/official/nlp/tinybert/tinybert_ascend_1.2_en-wiki_official_nlp_20210326/bert_base_finetune_ascend_1.2_qnli.ckpt>  
    asset-sha256: 89eb32e1d9e54bde96f239406b9701bd8457e2be814e4338e5d2507b88110f20  

license: Apache2.0

summary: tinybert used to do classification, sequence labeling or squad tasks on various dataset.

---

## Introduction

This MindSpore Hub model uses the implementation of TinyBertModel from the MindSpore model zoo on Gitee at model_zoo/official/nlp/tinybert.

This model has been trained on en-wiki using the code published on Gitee.

All Parameters in the module are trainable.

## Usage

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
# data dir can be glue dataset dir
dataset = create_tinybert_dataset('td', data_dir=data_dir)

columns_list = ["input_ids", "input_mask", "segment_ids", "label_ids"]
for data in dataset.create_dict_iterator():
    input_data = []
    for i in columns_list:
        input_data.append(data[i])
    input_ids, input_mask, token_type_id, label_ids = input_data
    logits = network(input_ids, token_type_id, input_mask)
    print("net output: ", logits)
# For more downstream tasks, please refer to https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/nlp/tinybert
```

## Citation

Paper: Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. arXiv preprint arXiv:1810.04805.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.