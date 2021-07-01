# googlenet

---

model-name: googlenet

backbone-name: googlenet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: imagenet2012

accuracy: 73

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/googlenet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/googlenet_ascend_v120_imagenet2012_official_cv_bs256_acc73/googlenet_ascend_v120_imagenet2012_official_cv_bs256_acc73.ckpt>
    asset-sha256: 211bb53836ab82171d44ab59322bd1cc69198e0a62f9850045d78afb60b3c0cc

license: Apache2.0

summary: googlenet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of googlenet from the MindSpore model zoo on Gitee at model_zoo/official/cv/googlenet.

googlenet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/googlenet](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/googlenet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/googlenet_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, num_classes=1001)
network.set_train(False)

# ...
```

## Citation

1. Christian Szegedy, Wei Liu, Yangqing Jia, Pierre Sermanet, Scott Reed, Dragomir Anguelov, Dumitru Erhan, Vincent Vanhoucke, Andrew Rabinovich. "Going deeper with convolutions." *Proceedings of the IEEE conference on computer vision and pattern recognition*. 2015.
