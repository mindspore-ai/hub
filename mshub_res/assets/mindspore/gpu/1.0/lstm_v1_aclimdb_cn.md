# LSTM

---

模型名称：LSTM

骨干网络： SentimentNet

模块类型：NLP

可微调：True

输入形状： [64, 500, 300]

模型版本：1.0

准确率： 0.82

作者：MindSpore团队

更新时间：2020-8-26

代码仓链接： <https://gitee.com/mindspore/models/tree/master/official/nlp/lstm>

用户ID：MindSpore

用途：推理

训练后端：GPU

推理后端：GPU

MindSpore版本：1.0

许可证：Apache 2.0

摘要：使用LSTM对aclimdb的2个类进行分类。

---

## 简介

该MindSpore Hub模型使用码云上MindSpore ModelZoo中的LSTM实现，目录为model_zoo/official/nlp/lstm。

使用已在码云上发布的代码在AclImdb数据集上训练该模型。

模块中所有参数均可训练。

## 参考论文

1. [论文](https://www.aclweb.org/anthology/P11-1015/)：  Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, Christopher Potts. [Learning Word Vectors for Sentiment Analysis](https://www.aclweb.org/anthology/P11-1015/). Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies. 2011
