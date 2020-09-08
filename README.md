![MindSporelogo](docs/MindSpore-logo.png "MindSpore logo")
============================================================

[查看中文](./README_CN.md)

- [What Is MindSpore Hub](#what-is-mindspore-hub)
    - [Features](#features)
- [Installation](#installation)
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

## Installation

### Binaries

Install MindSpore Hub using `pip` command. `hub` depends on the MindSpore version used in current environment. 

1. Please download whl package from [MindSpore Hub download page](https://www.mindspore.cn/versions).
   ```shell script
   pip install #TODO
   ```

2. Run the following command in a network-enabled environment to verify the installation. 
   ```python
   import mindspore_hub as mshub
   model = mshub.load("mindspore/ascend/0.7/googlenet_v1_cifar10")
   ```

## Quickstart

See the [Quick Start](#TODO) to implement model loading and fine-tuning.

## Docs
For more information about installation guide, tutorials and APIs, please check out the [User Documentation](#TODO).

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