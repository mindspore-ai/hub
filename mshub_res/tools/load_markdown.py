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
"""
Tool for checking load local path markdown file.
"""


import os
import tempfile
from mindspore import nn
from mindspore.train.serialization import load_checkpoint, load_param_into_net
from mindspore_hub.info import CellInfo
from mindspore_hub.load import _get_network_from_cache
from mindspore_hub._utils.download import _download_repo_from_url, _download_file_from_url


def load_local_md(path, *args, **kwargs):
    """
    Load network from local md file.

    This function is used to check whether the network can be load normally.

    Args:
        path (str): The path of md file.
        args (tuple): Arguments for network initialization.
        kwargs (dict): Keyworded arguments for network initialization.
    """
    if not isinstance(path, str):
        raise TypeError(f'`path` must be a string, but got {type(path)}')
    if not os.path.exists(path):
        raise ValueError('Please make sure input is a path.')
    try:
        info = CellInfo(path)
        with tempfile.TemporaryDirectory() as target_path:
            _download_repo_from_url(info.repo_link, target_path)
            net_dir = os.path.join(target_path, os.path.basename(info.repo_link))
            net = _get_network_from_cache(info.name, net_dir, *args, **kwargs)
            if not isinstance(net, nn.Cell):
                raise TypeError('`create_net` should be return a `Cell` type network, but got {}.'.format(type(net)))
            download_url = info.asset[info.asset_id]['asset-link']
            asset_sha256 = info.asset[info.asset_id]["asset-sha256"]
            ckpt_path = _download_file_from_url(download_url, asset_sha256, target_path)
            param_dict = load_checkpoint(ckpt_path)
            load_param_into_net(net, param_dict)
        print('*********** Success. ***********')
    except Exception as e:
        raise Exception(e)
