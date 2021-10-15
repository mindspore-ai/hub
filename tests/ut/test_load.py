# Copyright 2020 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""test load"""
import pytest
from mindspore_hub import load


class TestLoad:
    """Test load function."""
    def test_load(self):
        """Test normal cases."""
        names = ('mindspore/ascend/0.7/lenet_v1_mnist',
                 'https://gitee.com/mindspore/hub/blob/master/mshub_res/assets/mindspore/ascend/0.7/lenet_v1_mnist.md')
        pretraineds = (True, False)
        force_reloads = (True, False)
        for name in names:
            for pretrained in pretraineds:
                for force_reload in force_reloads:
                    load(name, 10, pretrained=pretrained, force_reload=force_reload)

    def test_load_name(self):
        """Test wrong name."""
        with pytest.raises(ValueError):
            load('https://www.baidu.com')

        with pytest.raises(ValueError):
            load('test/test/test')

        with pytest.raises(Exception):
            load('mindspore/gpu/0.6/test')

        with pytest.raises(Exception):
            load('https://gitee.com/mindspore/hub/raw/master/mshub_res/assets/mindspore')

    def test_load_type(self):
        """Test wrong type."""
        name = 1
        with pytest.raises(TypeError):
            load(name)

        name = 'mindspore/ascend/0.7/googlenet_v1_cifar10'
        pretrained = 'True'
        with pytest.raises(TypeError):
            load(name, pretrained=pretrained)

        force_reload = 1.0
        with pytest.raises(TypeError):
            load(name, force_reload=force_reload)
