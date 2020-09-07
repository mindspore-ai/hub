# Release 0.7.0
## Main Features
### Publish models quickly and easily

- Follow the guides in [publish readme](./mshub_res/README.md), your model will be shown in less than 24 hours.

### Supported Models
- GoogLeNet
- ResNet
- TODO

### Load Model in a convenient way
```python
import mindspore_hub as mshub
network = mshub.load("mindspore/ascend/0.2/googlenet_v1_cifar10", num_classes=10)
```
