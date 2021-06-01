# TinyBert

---

model-name: tinybert

backbone-name: TinyBertModel

module-type: nlp

fine-tunable: True

input-shape: [[1, 128], [1, 128], [1, 128]]

model-version: 1.1

train-dataset: zhwiki

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/nlp/tinybert>

user-id: MindSpore

used-for: inference/transfer-learning

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

  -
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/tinybert_ascend_v111_zhwiki_offical_nlp_bs32_loss6/tinybert_ascend_v111_zhwiki_offical_nlp_bs32_loss6.44.ckpt>
    asset-sha256: 897d9d0c0712995f5e76f3138210f83453b891b4354a33d547db650465086632

license: Apache2.0

summary: tinybert used to do classification, sequence labeling or squad tasks on various dataset.

---

## Introduction

This MindSpore Hub model uses the implementation of TinyBertModel from the MindSpore model zoo on Gitee [model_zoo/official/nlp/tinybert](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/nlp/tinybert/README.md).

This model has been trained on cn-wiki using the code published on Gitee.

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
model = "mindspore/ascend/1.1/tinybert_v1.1_zhwiki"
network = mshub.load(model, is_training=False)
network.set_train(False)
# data dir can be glue dataset dir
# dataset = create_tinybert_dataset('td', data_dir=data_dir)
#
# columns_list = ["input_ids", "input_mask", "segment_ids", "label_ids"]
# for data in dataset.create_dict_iterator():
#     input_data = []
#     for i in columns_list:
#         input_data.append(data[i])
#     input_ids, input_mask, token_type_id, label_ids = input_data
#     logits = network(input_ids, token_type_id, input_mask)
#     print("net output: ", logits)
# For more downstream tasks, please refer to https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/nlp/tinybert
```

## Citation

Paper: Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. arXiv preprint arXiv:1810.04805.
