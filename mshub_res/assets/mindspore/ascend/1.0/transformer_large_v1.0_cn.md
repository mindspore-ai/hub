# Transformer

---

模型名称：transformer_large

骨干网络： TransformerModel

模块类型：NLP

可微调：True

输入形状： [[1, 128], [1, 128], [1, 128], [1, 128]]

模型版本：1.0

作者：MindSpore团队

更新时间：2020-9-21

代码仓链接：<https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/nlp/transformer>

用户ID：MindSpore

用途：推理

训练后端：Ascend

推理后端：Ascend

MindSpore版本：1.0

许可证：Apache 2.0

摘要：使用transformer_large进行机器翻译。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的TransformerModel实现，目录为model_zoo/official/nlp/transformer。

该模型支持的动态输入形状取决于输入序列长度，最大序列长度为128。更多详情参见[码云MindSpore ModelZoo](https://gitee.com/mindspore/mindspore/blob/master/model_zoo/official/nlp/transformer/README.md)。

模块中所有参数均可训练。

## 参考论文

论文： Ashish Vaswani, Noam Shazeer, Niki Parmar, JakobUszkoreit, Llion Jones, Aidan N Gomez, Ł ukaszKaiser, and Illia Polosukhin. 2017. Attention is all you need. In NIPS 2017, pages 5998–6008.
