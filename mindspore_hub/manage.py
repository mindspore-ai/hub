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
"""Manage network in mindspore_hub."""

CACHE_DIR = '~/.cache'


def set_hub_dir(dir_path='~/.cache'):
    """
    Set the path of cache.

    Args:
        dir (str): The path of cahce.
    """
    global CACHE_DIR
    CACHE_DIR = dir_path


def get_hub_dir():
    """
    Get the path of cache.

    Returns:
        str, return a string of path.
    """
    return CACHE_DIR


def listall(sync=False):
    """
    List all model.

    Args:
        sync (bool): Whether synchronize information from mindspore_hub repo. Default: False.

    Returns:
        list, a list of model.
    """
    raise NotImplementedError()

def search(name):
    """
    Search model use given name.

    Args:
        name (str): Model name.

    Returns:
        list, a list of model.
    """
    raise NotImplementedError()
