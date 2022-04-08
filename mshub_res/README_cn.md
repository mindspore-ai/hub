# MindSpore Hub贡献指南

## 概述

该位置用于存储[MindSpore Hub网站](http://www.mindspore.cn)文档。

请注意，向MindSpore Hub发布模型正处于“测试阶段”。如果您有兴趣将自己的模型发布到MindSpore Hub，请遵循以下指引，我们将尽快处理您的提交。
MindSpore Hub网站将在24小时内更新。

### 服务条款

在向MindSpore Hub提交模型之前，请先同意MindSpore Hub条款。

### 许可证

所有提交到MindSpore Hub的模型应使用Apache 2.0许可证。

### UID

模型UID是一个字母数字令牌，格式为``发布者/后端/MindSpore版本/Markdown文件名``，其中``Markdown文件名``由``[模型名称]_[模型版本]_[数据集]``组成，可以是``hub.load``接口的输入。

示例：

| UID | URL |
| ------ | --- |
| mindspore/ascend/1.0/alexnet_v1_cifar10 | https://gitee.com/mindspore/hub/blob/master/mshub_res/assets/mindspore/ascend/1.0/alexnet_v1_cifar10.md |

| UID | 代码仓路径 |
| --- | ---      |
|mindspore/ascend/1.0/alexnet_v1_cifar10 | [repo_root]/mshub_res/assets/mindspore/ascend/1.0/alexnet_v1_cifar10.md |

### 模型存储、模型缓存和优化

我们不限制模型文件的位置，但建议您在提交的Markdown文件中将`allow_cache_ckpt`设为`true`。这种情况下，我们可以将模型文件缓存在自己的文件存储服务器中，加快下载速度，并可以尝试**优化**模型，例如为边缘设备（手机）加速。

## 发布

整个发布过程包括：

1. 创建模型并上传到可访问的地址。
2. 在repo下添加一个模型生成文件（.python），文件名为``mindspore_hub_conf.py``。
3. 编写Markdown文档，示例位于``examples``。
4. 使用``tools/md_validator.py``中的检查脚本自检Markdown文件的模式是否可用。
5. 创建发布请求。

更多详细，请参阅以下章节。

### 模型

#### 导出模型

MindSpore Hub仓库支持多种模型文件格式，包括：

* [MindSpore CKPT](https://www.mindspore.cn/docs/zh-CN/master/api_python/mindspore.train.html#mindspore.train.serialization.save_checkpoint)
* [AIR](https://www.mindspore.cn/docs/zh-CN/master/api_python/mindspore.train.html#mindspore.train.serialization.export)
* [MindIR](https://www.mindspore.cn/docs/zh-CN/master/api_python/mindspore.train.html#mindspore.train.serialization.export)
* [ONNX](https://www.mindspore.cn/docs/zh-CN/master/api_python/mindspore.train.html#mindspore.train.serialization.export)
* [MSLite](https://www.mindspore.cn/lite/docs/zh-CN/master/use/converter_tool.html)

### 代码

#### 添加minspore_hub_conf.py

该文件用于导出网络定义到Hub接口。文件位置如下：

```shell script
mobilenetv2
|- src
|   └──mobilenetv2.py
|- script
|   └──run_train.sh
|- train.py
|- test.py
|- mindspore_hub_conf.py
```

此文件必须包含一个函数，函数名为``create_network``，该函数的第一个args为支持创建的模型名称。**该名称中的小写字母应与Markdown文件中的``模型名称``匹配。**
请检查`*args`和``**kwargs``的值。

```python
import src.resnet as src_resnet

def resnet50(*args, **kwargs):
    return src_resnet.resnet50(*args, **kwargs)

def resnet101(*args, **kwargs):
    return src_resnet.resnet101(*args, **kwargs)

def create_network(name, *args, **kwargs):
    if name == "resnet50":
        return resnet50(*args, **kwargs)
    elif name == "resnet101":
        return resnet101(*args, **kwargs)
    else:
        raise NotImplementedError(f"{name} is not implemented in the repo")
```

### 资料文档

#### [模型名称]\_[模型版本]\_[数据集].md

如果您想在MindSpore Model Hub中发布模型，请提交一个拉取请求，以及一个Markdown文件。
这个Markdown文件包含两部分，第一部分是模型的元信息，包括代码仓链接和二进制文件链接。这些信息将在MindSpore Hub网站中显示。第二部分是在MindSpore Hub网站的详情页显示的详细信息。
请确保“用法”部分内容可运行。

您可以在``examples/commit_example.md``中下载示例Markdown文件，并更改相应信息。之后，可以使用``tools``中的文件检查工具来检查这个Markdown文件是否可用。

#### **重要**

Markdown文件中的内容应与示例文件保持一致。例如，我们使用``---``将文件分成两部分，第一部分用yaml格式加载。另一部分是Markdown格式。

``资源``项是字典列表。请用相同的模式来编写资源。

#### Markdown文件位置

1. 找到资源下发布者的目录，例如`.../assets/publisher/...`。

2. 找到发布者对应不同后端和MindSpore版本的目录，例如`.../assets/mindspore/ascend/1.0/...`

3. 在这个目录下放一个.md结尾的Markdown文件。

``.../assets/mindspore/ascend/1.0/alexnet_v1_cifar10.md``

#### 资源文件夹结构

```shell
assets
|────publisher
|      └──publisher_intro.md
|      └──ascend
|      |   └──1.0
|      └──gpu
|          └──1.0
|              └──[model_name]_[model_version]_[dataset].md
|              └──[model_name2]_[model_version2]_[dataset2].md
```

### 提交

下面介绍如何提交模型。

#### 提交模型

确定了Markdown文件位置后（参见上面的[资料文档](#资料文档)部分)，文件可以拉入[MindSpore Hub](https://gitee.com/mindspore/hub)的主分支。

### 验证资料文档

添加Markdown文件后，在创建拉取请求前，可以使用``mshub_res/tools/md_validator.py``中的校验器工具对所编写的Markdown文件进行校验。

```shell script
python mshub_res/tools/md_validator.py
```

### 高阶

您可以在拉取请求中添加图像作为静态文件，在Markdown文件中展示。您作为发布者可以将静态文件夹放在您的文件夹下。

```shell script
assets
|────publisher
|      └──publisher_intro.md
|      └──ascend
|      |   └──1.0
|      └──gpu
|      |   └──1.0
|      |       └──[model_name]_[model_version]_[dataset].md
|      |       └──[model_name2]_[model_version2]_[dataset2].md
|      └──static
|          └──images
|               └──image1.jpg
|
|────publisher2
|      └──publisher_intro.md
|      └──ascend
|      |   └──1.0
|      └──gpu
|      |   └──1.0
|      |       └──[model_name]_[model_version]_[dataset].md
|      |       └──[model_name2]_[model_version2]_[dataset2].md
|      └──static
|          └──images
|               └──image1.jpg
```
