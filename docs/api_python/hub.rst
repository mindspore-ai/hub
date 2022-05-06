mindspore_hub
=========================

MindSpore Hub是MindSpore生态系统的与训练模型应用工具，作为模型开发者和应用开发者的通道。

.. py:function:: mindspore_hub.load(name, *args, pretrained=True, force_reload=True, **kwargs)

    使用给定**name**加载网络。

    **参数：**

    - **name** (int) - 网络的 `uid` 或 `url` 。
    - **args** (tuple) - 网络初始化的参数。
    - **pretrained** (bool) - 是否加载预训练模型。 默认值：True。
    - **force_reload** (bool) - 是否从 `url` 重新加载网络。 默认值：True。
    - **kwargs** (dict) - 网络初始化的关键字参数。

    **返回：**

    Cell，网络。
