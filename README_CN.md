![MindSpore标志](docs/MindSpore-logo.png "MindSpore logo")
============================================================

[View English](./README.md)

- [MindSpore Hub介绍](#mindspore_hub介绍)
    - [特性](#特性)
- [环境要求](#环境要求)
    - [系统要求和软件依赖](#系统要求和软件依赖)
- [安装](#安装)
    - [源码安装](#源码安装)
    - [二进制文件](#二进制文件)
- [快速入门](#快速入门)
- [文档](#文档)
- [社区](#社区)
    - [治理](#治理)
    - [交流](#交流)
- [贡献](#贡献)
- [版本说明](#版本说明)
- [许可证](#许可证)

## MindSpore Hub介绍

MindSpore Hub是MindSpore生态的预训练模型应用工具，作为模型开发者和应用开发者的管道:
- 向模型开发者提供方便快捷的模型发布、提交通道；
- 向应用开发者提供高质量的预训练模型，结合模型加载以及模型Fine-tune API快速完成模型的迁移到部署的工作。

当前MindSpore Hub提供的预训练模型主要包括
图像分类、目标检测、语义模型、推荐模型等。更多模型内容可以查看[官网](#TODO)。

### 特性
 - **即插即用的模型加载**： 通过在MindSpore Hub网站上搜索可以快速得到想要的模型，快速体验MindSpore预训练模型；
 - **简单易用的迁移学习**： 借助MindSpore灵活的接口，一步实现迁移学习。

## 环境要求

### 系统要求和软件依赖

| 版本号                 | 操作系统            | 可执行文件安装依赖                                           | 源码编译安装依赖         |
| ---------------------- | :------------------ | :----------------------------------------------------------- | :----------------------- |
| MindSpore Hub master | - Ubuntu 18.04 x86_64 <br> - Ubuntu 18.04 aarch64 <br> - EulerOS 2.8 aarch64 <br> - EulerOS 2.5 x86_64 <br> | - [Python](https://www.python.org/downloads/) 3.7.5 <br> - MindSpore master<br> - 其他依赖项参见[setup.py](https://gitee.com/mindspore/hub/blob/master/setup.py) | 与可执行文件安装依赖相同 |

- 在联网状态下，安装whl包时会自动下载`setup.py`中的依赖项，其余情况需自行安装。

## 安装

### 源码安装

1. 从Gitee下载源码。

   ```bash
   git clone https://gitee.com/mindspore/hub.git
   ```

2. 编译安装MindSpore Hub。

   ```bash
   $ cd hub
   $ python setup.py install
   ```

### 二进制文件

使用`pip`命令安装，`hub`依赖当前环境中安装的MindSpore版本。

1. 请从[MindSpore Hub下载页面](https://www.mindspore.cn/versions)下载并安装whl包。
   ```shell script
   pip install mindspore_hub-{version}-py3-none-any.whl
   ```

2. 在能联网的环境中执行以下命令，验证安装结果。
   ```python
   import mindspore_hub as mshub
   model = mshub.load("mindspore/ascend/0.7/googlenet_v1_cifar10", num_classes=10)
   ```

## 快速入门

参考[从Hub加载模型](https://www.mindspore.cn/tutorial/training/zh-CN/master/use/load_model_for_inference_and_transfer.html#hub)实现模型加载以及模型微调迁移。

## 文档

有关安装指南、教程和API的更多详细信息，请参阅[从Hub加载模型](https://www.mindspore.cn/tutorial/training/zh-CN/master/use/load_model_for_inference_and_transfer.html#hub)和[发布模型](https://www.mindspore.cn/tutorial/training/zh-CN/master/use/publish_model.html)。

## 社区
MindSpore Hub是MindSpore社区的一部分，关于社区的交流、贡献与治理内容与MindSpore社区一致。
### 治理

查看MindSpore如何进行[开放治理](https://gitee.com/mindspore/community/blob/master/governance.md)。

### 交流

- [MindSpore Slack](https://join.slack.com/t/mindspore/shared_invite/zt-dgk65rli-3ex4xvS4wHX7UDmsQmfu8w) 开发者交流平台。
- `#mindspore` IRC频道（仅用于会议记录）
- 视频会议：待定
- 邮件列表：<https://mailweb.mindspore.cn/postorius/lists>

## 贡献

欢迎参与贡献。更多详情，请参阅我们的[贡献者Wiki](CONTRIBUTING.md)。


## 版本说明

版本说明请参阅[RELEASE](RELEASE.md)。

## 许可证

[Apache License 2.0](LICENSE)

## FAQ
- 遇到`SSL: CERTIFICATE_VERIFY_FAILED`怎么办？
  由于你的网络环境，例如你使用代理连接互联网，往往会由于证书配置问题导致python出现ssl verification failed的问题，此时有两种解决方法：
  - 配置好SSL证书**（推荐）**
  - 在加载mindspore_hub前增加如下代码进行折中（最快解决）
```python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import mindspore_hub as mshub
model = mshub.load("mindspore/ascend/0.7/googlenet_v1_cifar10", num_classes=10)
```