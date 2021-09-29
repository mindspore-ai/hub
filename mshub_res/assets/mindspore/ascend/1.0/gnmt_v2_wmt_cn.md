# GNMT

---

模型名称：GNMT_v2

骨干网络：GNMTv2模型

模块类型：NLP

可微调：True

输入形状： [[1, 128], [1, 128], [1, 128],[1, 128], [1, 128]]

模型版本：1.0

作者：MindSpore团队

更新时间：2020-12-23

代码仓链接： <https://gitee.com/mindspore/models/tree/master/official/nlp/gnmt_v2>

用户ID：MindSpore

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：1.0

资源：

-
    文件格式：.ckpt  
    资源链接： <https://download.mindspore.cn/model_zoo/official/nlp/gnmt_v2/gnmt_v2_ascend_1.0_wmt_corpus_official_text_summarization_20201110/gnmt_ascend.ckpt>  
    资源SHA256校验码： 0ee1a22237143ae175c90f68c4970ae55fef0a683bc0ac6f5aacd78b6486bc8b

许可证：Apache 2.0

摘要：使用GNMT_v2进行机器翻译。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的GNMTv2实现，目录为model_zoo/official/nlp/gnmt_v2。

该模型支持的动态输入形状取决于输入序列长度，最大序列长度为128。更多详情参见[码云MindSpore ModelZoo](https://gitee.com/mindspore/models/tree/master/official/nlp/gnmt_v2/README.md)。

模块中所有参数均可训练。

## 用法

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.0/gnmt_v2_wmt"

network = mshub.load(model, is_training=False)
network.set_train(False)
# 推理与MindSpore模型相同，请参考https://gitee.com/mindspore/models/tree/master/official/nlp/gnmt_v2
```

## 参考论文

论文： Wu Y , Schuster M , Chen Z , et al. Google's Neural Machine Translation System: Bridging the Gap between Human and Machine Translation[J]. 2016.
