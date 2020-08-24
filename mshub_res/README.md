# Contributions guide to MindSpore Hub

## Overview
This location is used for storage the documents for [MindSpore Hub Website](http://www.mindspore.cn)

Please note that publishing a model to MindSpore Hub is in "testing stage". If you
are interested in publishing your own model to MindSpore Hub, please follow the directions below and 
we will process your submission as soon as possible. And the MindSpore Hub Website will be updated in
less than 24 hours.

### Terms of service
You should agree to the MindSpore Hub Terms before submitting a model into MindSpore Hub.

### License
**All the Model committed to the MindSpore Hub should use the Apache 2.0 License**

### UID
Model uid is alphanumeric token, in the pattern of ``publisher/backend/mindspore_version/markdown_file_name``, 
in which ``markdown_file_name`` is consisted of ``[model_name]_[model_version]_[dataset]``. Which could be the input of 
the ``hub.load`` interface.

See example below:

| UID | Url |
| ------ | --- |
| mindspore/ascend/0.6/alexnet_v1_cifar10 | https://hub.mindspore.com/mindspore/ascend/0.6/alexnet_v1_cifar10 |

| UID | repo_path|
| --- | ---      |
|mindspore/ascend/0.6/alexnet_v1_cifar10 | [repo_root]/mshub_res/assets/mindspore/ascend/0.6/alexnet_v1_cifar10.md |

### Model storage and Model Cache/Optimization

We don't restrict the location of the model file. But we suggest you set the term of ``allow_cache_ckpt`` to be 
``true`` in the markdown file you commit, so that we will cache the model file in our own file storage server to
 accelerate the download and will try to **optimize** the model, speeding up for the Edge Devices, 
 Mobile Phone for example.

## How to publish

The full process of publishing consists of:

1. Creating the model, and upload to a place which can be accessed
1. Adding a model generation python file named ``mindspore_hub_conf.py`` under the repo
1. Writing documentation, which is a markdown file and an example is located in ``examples``
1. Using the check script in ``tools/validator.py`` to self-checking the markdown file's pattern is good or not
1. Creating a publishing request.

See sections below for more details.

### Model

#### Exporting a model

The MindSpore Hub repository supports multiple kinds of model file-formats, 
including:

* [MindSpore CKPT](https://www.mindspore.cn/api/zh-CN/master/api/python/mindspore/mindspore.train.html?highlight=save_checkpoint#mindspore.train.serialization.save_checkpoint)
* [AIR](https://www.mindspore.cn/api/zh-CN/master/api/python/mindspore/mindspore.train.html?highlight=export#mindspore.train.serialization.export)
* [MindIR](https://www.mindspore.cn/api/zh-CN/master/api/python/mindspore/mindspore.train.html?highlight=export#mindspore.train.serialization.export)
* [ONNX](https://www.mindspore.cn/api/zh-CN/master/api/python/mindspore/mindspore.train.html?highlight=export#mindspore.train.serialization.export)

### Codes

#### Adding mindspore_hub_conf.py

This file is used to export the network definition to the hub interface. File location is listed below,

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

The Content in this file must include a function which name ``create_network``, this function's first args is the model
name which is supported to create. This name should match the ``model_name`` in markdown file. You should check the 
values in ``**kwargs``.
```python
from src.mobilenetv2 import mobilenet_v2

def mobilenet_v2(**kwargs):
    mobilenet_v2(**kwargs)


def create_network(name, **kwargs):
    return eval(name)(**kwargs)
```

### Documentation
#### [model_name]\_[model_version]\_[dataset].md

If you want to publish your model in MindSpore Model Hub, you should commit a pull request, along with a markdown file.
This markdown file can be split into two parts, first one is the meta information of the model, including the repo link 
and binary file link, these information will be shown in the MindSpore Hub Website. Second one is the detail information
will be shown in the detail page in MindSpore Hub Website. You should make sure your Usage section can be run.

You can download the example markdown file in the ``examples/commit_example.md``, change the information accordingly. 
After that, you can use the check file tool in the ``tools`` to check whether this markdown file is good or not.

#### Where to put the markdown file?

1. It has to be submitted inside the publisher directory,
   e.g. `.../assets/publisher/...`.
2. It has to be submitted inside the publisher directory, under the folder of specific backend and mindspore version
   e.g. `.../assets/mindspore/ascend/0.6/...`
3. It has to end with `.md`.

``.../assets/mindspore/ascend/0.6/alexnet_v1_cifar10.md``

#### Assets folder structure

```shell script
assets
|────publisher
|      └──publisher_intro.md
|      └──ascend
|      |   └──0.6
|      └──gpu
|          └──0.6
|              └──[model_name]_[model_version]_[dataset].md
|              └──[model_name2]_[model_version2]_[dataset2].md
```

### Submission

How to submit the model

#### Submitting the model

After the right location of the markdown file is identified (see the
[Writing the documentation](#Documentation) section above),
the file can be pulled into the master branch of
[mindspore/hub](https://gitee.com/mindspore/hub)

### Validating the documentation


After adding the markdown file, you can use the validator tool in the ``mshub_res/tools/validator.py`` to validate
the markdown file you write before you creating a pull request.

```
python mshub_res/tools/validator.py
```
### Advance

You can add some images as static file in your pull request for showing in the markdown file. You can have static folder 
under your folder as a publisher.

```shell script
assets
|────publisher
|      └──publisher_intro.md
|      └──ascend
|      |   └──0.6
|      └──gpu
|      |   └──0.6
|      |       └──[model_name]_[model_version]_[dataset].md
|      |       └──[model_name2]_[model_version2]_[dataset2].md
|      └──static
|          └──images
|               └──image1.jpg
|
|────publisher2
|      └──publisher_intro.md
|      └──ascend
|      |   └──0.6
|      └──gpu
|      |   └──0.6
|      |       └──[model_name]_[model_version]_[dataset].md
|      |       └──[model_name2]_[model_version2]_[dataset2].md
|      └──static
|          └──images
|               └──image1.jpg
```
