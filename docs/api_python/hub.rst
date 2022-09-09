mindspore_hub
=========================

MindSpore Hub是MindSpore生态系统的预训练模型应用工具，作为模型开发者和应用开发者的通道。

.. py:function:: mindspore_hub.load(name, *args, source='gitee', pretrained=True, force_reload=False, **kwargs)

    用于加载指定网络。加载完成后，可用于推理验证、迁移学习等。

    **参数：**

    - **name** (str) - 网络的 `uid` 或 `url` ，或者md文件的本地路径。
    - **args** (tuple) - 网络初始化的参数。
    - **source** (str) - 是否将 `name` 解析为gitee模型URI、github模型URI或本地资源。默认值：gitee。
    - **pretrained** (bool) - 是否加载预训练模型。 默认值：True。
    - **force_reload** (bool) - 是否从 `url` 重新加载网络。 默认值：False。
    - **kwargs** (dict) - 网络初始化的关键字参数。

    **返回：**

    Cell，网络。

.. py:function:: mindspore_hub.hub_list(version=None, force_reload=True)

    列出MindSpore Hub支持的所有asset。

    **参数：**

    - **version** (str) - 指定要列出的版本。`None` 表示最新版本。默认值：None。
    - **force_reload** (bool) - 是否从 `url` 重新加载网络。 默认值：True。

    **返回：**

    list，MindSpore Hub支持的asset列表。
