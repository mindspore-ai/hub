# ![MindSporelogo](docs/MindSpore-logo.png "MindSpore logo")

[查看中文](./README_CN.md)

- [What Is MindSpore Hub](#what-is-mindspore-hub)
    - [Features](#features)
- [Environment Requirements](#environment-requirements)
    - [System Requirements and Software Dependencies](#system-requirements-and-software-dependencies)
- [Installation](#installation)
    - [Installation from source code](#Installation-from-source-code)
    - [Installation from pip command](#Installation-from-pip-command)
    - [Verification](#Verification)
- [Quickstart](#quickstart)
- [Docs](#docs)
- [Community](#community)
    - [Governance](#governance)
    - [Communication](#communication)
- [Contributing](#contributing)
- [Release Notes](#release-notes)
- [License](#license)
- [FAQ](#FAQ)

## What is MindSpore Hub

MindSpore Hub is a pre-trained model application tool of the MindSpore ecosystem, serving as a channel for model developers and application developers.

- Provide model developers with a convenient and fast channel for model release and submission.
- Provide application developers with high-quality pre-trained models, and complete the work of model migration to deployment quickly using model loading and fine-tuning APIs.

Current pre-trained models in MindSpore Hub mainly cover four mainstream task scenarios including image classification, object detection, semantic segmentation and recommendation. You can check more models in [MindSpore Hub Website](https://www.mindspore.cn/resources/hub/en).

## Features

- **Flexible model loading**： Access and experience pre-trained models quickly by searching models of interest on MindSpore Hub Website.
- **Easy-to-use transfer learning**: Achieve transfer learning in one step via MindSpore's flexbile interface.

## Environment Requirements

### System Requirements and Software Dependencies

| Version | Operating System | Executable File Installation Dependencies | Source Code Compilation and Installation Dependencies |
| ---- | :--- | :--- | :--- |
| MindSpore Hub master | - Ubuntu 18.04 x86_64 <br> - Ubuntu 18.04 aarch64 <br> - EulerOS 2.8 aarch64 <br> - EulerOS 2.5 x86_64 <br> | - [Python](https://www.python.org/downloads/) 3.7.5 <br> - MindSpore master <br> - For details about other dependency items, see [setup.py](https://gitee.com/mindspore/hub/blob/master/setup.py). | Same as the executable file installation dependencies. |

- When the network is connected, dependency items in the `setup.py` file are automatically downloaded during .whl package installation. In other cases, you need to manually install dependency items.

## Installation

The Hub depends on MindSprore because the Hub depends on the models repository of MindSpore. Please follow the table below and install the corresponding MindSpore verision from [MindSpore download page](https://www.mindspore.cn/versions/en).

| MindSpore Hub|                             Branch                    | MindSpore |
| :----------: | :------------------------------------------------: | :-------: |
|     1.9.0    | [r1.9](https://gitee.com/mindspore/hub/tree/r1.9/) |   1.9.0   |
|     1.8.0    | [r1.8](https://gitee.com/mindspore/hub/tree/r1.8/) |   1.8.0   |
|     1.6.0    | [r1.6](https://gitee.com/mindspore/hub/tree/r1.6/) |   1.6.0   |
|     1.5.0    | [r1.5](https://gitee.com/mindspore/hub/tree/r1.5/) |   1.5.0   |
|     1.4.0    | [r1.4](https://gitee.com/mindspore/hub/tree/r1.4/) |   1.4.0   |
|     1.3.0    | [r1.3](https://gitee.com/mindspore/hub/tree/r1.3/) |   1.3.0   |
|     1.2.0    | [r1.2](https://gitee.com/mindspore/hub/tree/r1.2/) |   1.2.0   |
|     1.1.0    | [r1.1](https://gitee.com/mindspore/hub/tree/r1.1/) |   1.2.0   |
|     1.0.1    | [r1.0.1](https://gitee.com/mindspore/hub/tree/r1.0.1/) |   1.2.0  |
|     1.0.0    | [r1.0](https://gitee.com/mindspore/hub/tree/r1.0/) |   1.2.0   |

### Installation from source code

1. Download source code from Gitee.

   ```bash
   git clone https://gitee.com/mindspore/hub.git
   ```

2. Compile and install in MindSpore Hub directory.

   ```bash
   cd hub
   python setup.py install
   ```

### Installation from pip command

Install MindSpore Hub using `pip` command. Please download whl package from [MindSpore Hub download page](https://www.mindspore.cn/versions/en).

   ```shell script
   pip install mindspore_hub-{version}-py3-none-any.whl
   ```

### Verification

If you can successfully execute following command, then the installation is completed.

```python
import mindspore_hub as mshub
```

## Quickstart

See the [Loading the Model from Hub](https://www.mindspore.cn/hub/docs/en/master/loading_model_from_hub.html) to implement model loading and fine-tuning.

## Docs

For more information about installation guide, tutorials and APIs, please check out the [Loading the Model from Hub](https://www.mindspore.cn/hub/docs/en/master/loading_model_from_hub.html) and [Publishing Models using MindSpore Hub](https://www.mindspore.cn/hub/docs/en/master/publish_model.html).

## Community

As one part of MindSpore community, the following information in MindSpore Hub including governance, communication and contributing is consistent with the content in MindSpore community.

### Governance

Check out how MindSpore Open Governance [works](https://gitee.com/mindspore/community/blob/master/governance.md).

### Communication

- [MindSpore Slack](https://join.slack.com/t/mindspore/shared_invite/zt-dgk65rli-3ex4xvS4wHX7UDmsQmfu8w) - Communication platform for developers.
- IRC channel at `#mindspore` (only for meeting minutes logging purpose)
- Video Conference：TBD
- Mailing-list：<https://mailweb.mindspore.cn/postorius/lists>

## Contributing

Welcome contributions. See our [Contributor Wiki](CONTRIBUTING.md) for more details。

## Release Notes

The release notes, see our [RELEASE](RELEASE.md)。

## License

[Apache License 2.0](LICENSE)

## FAQ

- What to do when `SSL: CERTIFICATE_VERIFY_FAILED` occurs?
   When you behind a proxy, it sometimes will have some ssl verification fail problems. You can add the certificate into system to fix this problem. The fastest method is to disable python's ssl verification. Before import mindspore_hub, please add the codes.

```python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import mindspore_hub as mshub
model = mshub.load("mindspore/1.6/googlenet_cifar10", num_classes=10)
```

- What to do when `No module named src.*` occurs?
  When you use `mindspore_hub.load` to load differenet model in the same process, because the model file path needs to be inserted into `sys.path`. Test results show that Python only looks for `src.*` in the first inserted path. It's no use to delete the first inserted path. To solve the problem, you can copy all model files to the working directory. The code is as follows:

```python
# mindspore_hub_install_path/load.py
def _copy_all_file_to_target_path(path, target_path):
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    path = os.path.realpath(path)
    target_path = os.path.realpath(target_path)
    for p in os.listdir(path):
        copy_path = os.path.join(path, p)
        target_dir = os.path.join(target_path, p)
        _delete_if_exist(target_dir)
        if os.path.isdir(copy_path):
            _copy_all_file_to_target_path(copy_path, target_dir)
        else:
            shutil.copy(copy_path, target_dir)

def _get_network_from_cache(name, path, *args, **kwargs):
    _copy_all_file_to_target_path(path, os.getcwd())
    config_path = os.path.join(os.getcwd(), HUB_CONFIG_FILE)
    if not os.path.exists(config_path):
        raise ValueError('{} not exists.'.format(config_path))
    ......
```

  **Note**: Some files of the previous model may be replaced when the next model is loaded. However， necessary model files must exist during model training. Therefore, you must finish training the previous model before the next model loads.
