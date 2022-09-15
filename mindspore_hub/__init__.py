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
"""MindSpore Hub is a pre-trained model application tool of the MindSpore ecosystem,
serving as a channel for model developers and application developers."""

import time
from .load import load
from .list import hub_list
from .version import __version__

__all__ = ['load', 'hub_list', '__version__']


def _mindspore_version_check():
    """
    Do the MindSpore version check for MindSpore Hub. If MindSpore can not be imported,
    it will raise ImportError. If its version is not compatible with current MindSpore Hub
    version, it will print a warning.
    """
    try:
        import mindspore as ms
        from mindspore import log as logger
    except ImportError:
        print("Can not find MindSpore in current environment. Please install "
              "MindSpore before using MindSpore Hub, by following "
              "the instruction at https://www.mindspore.cn/install")
        raise
    hub_mindspore_version_map = {
        '1.0.0': '1.2.0',
        '1.0.1': '1.2.0',
        '1.1.0': '1.2.0',
        '1.2.0': '1.2.0',
        '1.3.0': '1.3.0',
        '1.4.0': '1.4.0',
        '1.5.0': '1.5.0',
        '1.6.0': '1.6.0',
        '1.8.0': '1.8.0',
        '1.9.0': '1.9.0'
    }
    ms_version = ms.__version__
    required_ms_version = hub_mindspore_version_map[__version__]

    if ms_version != required_ms_version:
        logger.warning("Current version of MindSpore is not compatible with MindSpore Hub. "
                       "Some functions might not work or even raise error. Please install MindSpore "
                       "version == {}. For more details about dependency setting, please check "
                       "the instructions at MindSpore official website https://www.mindspore.cn/install "
                       "or check the README.md at https://gitee.com/mindspore/hub".format(required_ms_version))
        warning_countdown = 3
        for i in range(warning_countdown, 0, -1):
            logger.warning(
                f"Please pay attention to the above warning, countdonw: {i}")
            time.sleep(1)


_mindspore_version_check()
