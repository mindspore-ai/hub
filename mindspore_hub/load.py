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
Loading network or model.

Loding network definition or prtrained model from mindspore mindspore_hub.
"""

import sys
import os
import shutil
import importlib.util
import logging as logger
from mindspore import nn
from mindspore.train.serialization import load_checkpoint, load_param_into_net
from .info import CellInfo
from ._utils.download import _download_repo_from_url, extract_file, _download_file_from_url


HUB_CONFIG_FILE = 'mindsporehub.py'
ENTRY_POINT = 'create_net'


def _generate_repo_url(link):
    """Generate the url of repo."""
    raise NotImplementedError()


def _get_network_from_cache(info, *args, **kwargs):
    """
    Load network from cache.

    Args:
        info (CellInfo): The information of network.
        args (tuple): The arguments of init network.
        kwargs (dict): The key arguments of init network.

    Returns:
        Cell, return network.
    """
    net = None
    path = os.path.expanduser(info.path)
    sys.path.insert(0, path)
    config_path = os.path.abspath(path) + '/' + HUB_CONFIG_FILE
    if not os.path.exists(config_path):
        raise ValueError('{} not exists.'.format(config_path))
    spec = importlib.util.spec_from_file_location(HUB_CONFIG_FILE, config_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    net = None
    cwd = os.getcwd()
    os.chdir(path)
    if not hasattr(module, ENTRY_POINT):
        raise KeyError('Can\'t find `create_net` function.')
    func = getattr(module, ENTRY_POINT)
    net = func(*args, **kwargs)
    os.chdir(cwd)
    return net


def _backup(path, backup_path):
    """Backup files."""
    if os.path.exists(backup_path):
        shutil.rmtree(backup_path)
    if os.path.exists(path):
        os.rename(path, backup_path)


def _recover_backup(path, backup_path):
    """Recover files."""
    if os.path.exists(path):
        shutil.rmtree(path)
    if os.path.exists(backup_path):
        os.rename(backup_path, path)


def _get_network_from_url(info, *args, **kwargs):
    """
    Load network from url.

    Args:
        info (CellInfo): The information of network.
        args (tuple): The arguments of init network.
        kwargs (dict): The key arguments of init network.

    Returns:
        Cell, return network.
    """
    net = None
    url = _generate_repo_url(info.repo_link)
    path = os.path.expanduser(info.path)
    path = os.path.abspath(path)
    par_path = '/'.join(path.split('/')[:-1])
    backup_path = path + '.bk'
    _backup(path, backup_path)
    try:
        name = os.path.basename(url)
        file_path = par_path + '/' + name
        if _download_repo_from_url(url, par_path):
            extract_file(file_path, path)
            shutil.rmtree(backup_path)
        else:
            _recover_backup(path, backup_path)
    except Exception as err:
        _recover_backup(path, backup_path)
        raise IOError(err)
    net = _get_network_from_cache(info, *args, **kwargs)
    return net


def load(name, *args, pretrained=True, force_reload=False, **kwargs):
    """
    Load network with given name.

    Args:
        name (str): Network name or url.
        args (tuple): Arguments for network initialization.
        pretrained (bool): Whether load pretrained model. Default: True.
        force_reload (bool): Whether reload network from url. Default: False.
        kwargs (dict): Keyworded arguments for network initialization.
    Returns:
        Cell, a network.
    """
    if not isinstance(name, str):
        raise TypeError('Network name must be a string of name or a url.')
    if not isinstance(force_reload, bool):
        raise TypeError('`force_reload` must be a bool type.')
    info = CellInfo(name)
    net = None
    if not force_reload and os.path.exists(os.path.expanduser(info.path)):
        net = _get_network_from_cache(info, *args, **kwargs)
    else:
        net = _get_network_from_url(info, *args, **kwargs)
    if not isinstance(net, nn.Cell):
        raise TypeError('`create_net should be return a `Cell` type network, but got {}.'.format(type(net)))

    if pretrained:
        load_weights(net, handle=name, force_reload=force_reload)
    return net


def load_weights(network, handle=None, force_reload=True):
    """
    Load a k from MindSpore mindspore_hub, with pertained weights.

    Args:
        network (Cell): Cell network.
        handle (str, optional): uid or url link. Default: None.
        force_reload (bool, optional): Whether to force a fresh download unconditionally. Default: False.

    """
    if not isinstance(network, nn.Cell):
        logger.error("Failed to combine the net and the parameters.")
        msg = ("Argument net should be a Cell, but got {}.".format(type(network)))
        raise TypeError(msg)

    if handle.startwith('http'):
        if len(handle.split('/')) < 2:
            raise ValueError('Wrong url.')
        net_name, md_name = _get_md_and_name_from_name(handle)
        uid = md_name[:-3]
    else:
        net_name, md_name = _get_md_and_name_from_name(handle)
        uid = handle
    path = _generate_store_path(uid)
    _create_if_not_exist(path)
    _download_file_from_url(HUB_CONFIG_FILE + md_name, path)
    md_path = path + '/' + md_name.split('/')[-1]

    cell = CellInfo(net_name)
    cell.update(md_path)

    download_url = cell.asset[cell.asset_id]['asset-link']
    asset_sha256 = cell.asset[cell.asset_id]["asset-sha256"]

    if force_reload:
        ckpt_path = _download_file_from_url(download_url, asset_sha256, path)
    else:
        ckpt_name = os.path.basename(download_url.split("/")[-1])
        ckpt_path = os.path.join(path, ckpt_name)
        if not os.path.exists(ckpt_path):
            ckpt_path = _download_file_from_url(download_url, asset_sha256, path)

    param_dict = load_checkpoint(ckpt_path)
    load_param_into_net(network, param_dict)
