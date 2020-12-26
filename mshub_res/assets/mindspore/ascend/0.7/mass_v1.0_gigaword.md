# MASS

---

model-name: mass

backbone-name: MassModel

module-type: nlp

fine-tunable: True

input-shape: [[1, 64], [1, 64], [1, 64], [1, 64], [1, 64], [1, 64]]

model-version: 1.0

train-dataset: Gigaword corpus

author: MindSpore team

update-time: 2020-09-21

repo-link: <https://gitee.com/mindspore/mindspore/tree/r0.7/model_zoo/official/nlp/mass>

user-id: MindSpore

used-for: inference/transfer-learning

train-backend: ascend

infer-backend: ascend

mindspore-version: 0.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/official/nlp/mass/mass_ascend_0.3.0_gigaword_corpus_official_text_summarization_20200716.tar.gz>
    asset-sha256: 1cec4ec74dcf8e182b97e97a96e0d71a3911ec1b2aa25583a5930240ef962571

license: Apache2.0
summary: mass used to do text summary on various dataset.
---

## Introduction

This MindSpore Hub model uses the implementation of MASSModel from the MindSpore model zoo on Gitee at model_zoo/official/nlp/mass.

This model has been trained on gigaword-corpus using the code published on Gitee.

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

model = "mindspore/ascend/0.7/mass_v1.0_gigaword"

network = mshub.load(model, config="./config.json", is_training=False)
network.set_train(False)
columns_list=["source_eos_ids", "source_eos_mask", "target_sos_ids", "target_sos_mask", "target_eos_ids", "target_eos_mask"]
ds = de.TFRecordDataset(data_files, None, columns_list=columns_list)
for data in ds.create_dict_iterator():
    input_data = []
    for i in columns_list:
        input_data.append(Tensor(data[i]))
    source_eos_ids, source_eos_mask, target_sos_ids, target_sos_mask, target_eos_ids, target_eos_mask = input_data
    out = network(source_eos_ids, source_eos_mask, target_sos_ids, target_sos_mask, target_eos_ids, target_eos_mask)
```

## Citation

Paper: Song, Kaitao, Xu Tan, Tao Qin, Jianfeng Lu and Tie-Yan Liu. “MASS: Masked Sequence to Sequence Pre-training for Language Generation.” ICML (2019).
