# MASS

---

模型名称：MASS

骨干网络：MassModel

模块类型：NLP

可微调：True

输入形状： [[1, 64], [1, 64], [1, 64], [1, 64], [1, 64], [1, 64]]

模型版本：1.0

训练数据集： Gigaword corpus

作者：MindSpore团队

更新时间：2020-9-21

代码仓链接： <https://gitee.com/mindspore/mindspore/tree/r0.7/model_zoo/official/nlp/mass>

用户ID：MindSpore

用途：推理/迁移学习

训练后端：Ascend

推理后端：Ascend

MindSpore版本：0.7

资源：

-
    文件格式：.ckpt  
    资源链接： <https://download.mindspore.cn/model_zoo/official/nlp/mass/mass_ascend_0.3.0_gigaword_corpus_official_text_summarization_20200716.tar.gz>  
    资源SHA256校验码：1cec4ec74dcf8e182b97e97a96e0d71a3911ec1b2aa25583a5930240ef962571

许可证：Apache 2.0

摘要：使用MASS对各种数据集进行文本摘要。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的MASSModel实现，目录为model_zoo/official/nlp/mass。

使用已在码云上发布的代码在gigaword-corpus数据集上训练该模型。

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

## 参考论文

论文： Song, Kaitao, Xu Tan, Tao Qin, Jianfeng Lu and Tie-Yan Liu. “MASS: Masked Sequence to Sequence Pre-training for Language Generation.” ICML (2019).
