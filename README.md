![MindSporelogo](docs/MindSpore-logo.png "MindSpore logo")
============================================================

[查看中文](./README_CN.md)

- [What Is MindSpore Hub](#what-is-mindspore-hub)
    - [Features](#features)
- [Environment Requirements](#environment-requirements)
    - [System Requirements and Software Dependencies](#system-requirements-and-software-dependencies)
- [Installation](#installation)
    - [Installation for development](#installation-for-development)
    - [Binaries](#binaries)
- [Quickstart](#quickstart)
- [Docs](#docs)
- [Community](#community)
    - [Governance](#governance)
    - [Communication](#communication)
- [Contributing](#contributing)
- [Release Notes](#release-notes)
- [License](#license)

## What is MindSpore Hub

MindSpore Hub is a pre-trained model application tool of the MindSpore ecosystem, serving as a channel for model developers and application developers. 
- Provide model developers with a convenient and fast channel for model release and submission. 
- Provide application developers with high-quality pre-trained models, and complete the work of model migration to deployment quickly using model loading and fine-tuning APIs.

Current pre-trained models in MindSpore Hub mainly cover four mainstream task scenarios including image classification, object detection, semantic segmentation and recommendation. You can check more models in [MindSpore Hub Website](#TODO). 

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

### Installation for development

1. Download source code from Gitee.

   ```bash
   git clone https://gitee.com/mindspore/hub.git
   ```

2. Compile and install in MindSpore Hub directory.

   ```bash
   $ cd hub
   $ python setup.py install
   ```

### Binaries

Install MindSpore Hub using `pip` command. `hub` depends on the MindSpore version used in current environment. 

1. Please download whl package from [MindSpore Hub download page](https://www.mindspore.cn/versions/en).
   ```shell script
   pip install mindspore_hub-{version}-py3-none-any.whl
   ```

2. Run the following command in a network-enabled environment to verify the installation. 
   ```python
   import mindspore_hub as mshub
   model = mshub.load("mindspore/ascend/0.7/googlenet_v1_cifar10", num_classes=10)
   ```

## Quickstart

See the [Quick Start](https://www.mindspore.cn/tutorial/en/master/advanced_use/hub_tutorial.html) to implement model loading and fine-tuning.

## Docs
For more information about installation guide, tutorials and APIs, please check out the [User Documentation](https://www.mindspore.cn/tutorial/en/master/advanced_use/hub_tutorial.html).

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
When you behind a proxy, it sometimes will have some ssl verification fail problems. You can add the certificate into
system to fix this problem. The fastest method is to disable python's ssl verification. Before import mindspore_hub, please add the codes.
```python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import mindspore_hub as mshub
model = mshub.load("mindspore/ascend/0.7/googlenet_v1_cifar10", num_classes=10)
``` 
