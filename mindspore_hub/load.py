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
import warnings
from mindspore import nn
from mindspore.train.serialization import load_checkpoint, load_param_into_net
from .info import CellInfo
from ._utils.download import _download_file_from_url, _download_repo_from_url
from .manage import get_hub_dir


HUB_CONFIG_FILE = 'mindspore_hub_conf.py'
ENTRY_POINT = 'create_network'
HUB_MD_DIR = 'https://gitee.com/mindspore/hub/raw/master/mshub_res/assets/'


def _generate_store_path(name):
    """
    Generate store path.
    """
    values = name.split('/')
    publisher = values[0]
    model_name = values[1].split('_')[0]
    cache_path = os.path.abspath(os.path.expanduser(get_hub_dir()))
    return os.path.join(cache_path, publisher, model_name)


def _get_network_from_cache(path, *args, **kwargs):
    """
    Load network from cache.

    Args:
        path (str): The path of network.
        args (tuple): The arguments of init network.
        kwargs (dict): The key arguments of init network.

    Returns:
        Cell, return network.
    """
    net = None
    sys.path.insert(0, path)
    config_path = os.path.join(os.path.abspath(path), HUB_CONFIG_FILE)
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


def _delete_backup(path):
    """Delete backpu files"""
    if os.path.exists(path):
        shutil.rmtree(path)


def _create_if_not_exist(path):
    """ Create not exist directory."""
    if not os.path.exists(path):
        os.makedirs(path)


def _get_network_from_url(url, path, *args, **kwargs):
    """
    Load network from url.

    Args:
        url (str): The url of network.
        path (str): The path of network.
        args (tuple): The arguments of init network.
        kwargs (dict): The key arguments of init network.

    Returns:
        Cell, return network.
    """
    net = None
    network_dir = os.path.join(path, os.path.basename(url))
    backup_path = network_dir + '.bk'
    _backup(network_dir, backup_path)
    try:
        _create_if_not_exist(path)
        if _download_repo_from_url(url, path):
            _delete_backup(backup_path)
        else:
            _recover_backup(network_dir, backup_path)
    except Exception as err:
        _recover_backup(network_dir, backup_path)
        raise IOError(err)
    net = _get_network_from_cache(network_dir, *args, **kwargs)
    return net


def _get_md_and_name_from_url(url):
    """Get markdown name and network name from url."""
    values = url.split('/')
    values[-1] = values[-1].split('.')[0]
    name = values[-1]
    md_name = os.path.join(*values[-2:]) + '.md'
    return name, md_name


def _get_md_and_name_from_name(name):
    """Get markdown name and network name from given name."""
    md_name = name + '.md'
    net_name = name.split('/')[-1]
    return net_name, md_name


def load(name, *args, pretrained=True, force_reload=True, **kwargs):
    """
    Load network with given name.

    Args:
        name (str): Network name or url.
        args (tuple): Arguments for network initialization.
        pretrained (bool): Whether load pretrained model. Default: True.
        force_reload (bool): Whether reload network from url. Default: True.
        kwargs (dict): Keyworded arguments for network initialization.
    Returns:
        Cell, a network.
    """
    if not isinstance(name, str):
        raise TypeError('Network name must be a string of name or a url.')
    if not isinstance(force_reload, bool):
        raise TypeError('`force_reload` must be a bool type.')
    if not isinstance(pretrained, bool):
        raise TypeError('`pretrained` must be a bool type.')

    if os.path.exists(os.path.expanduser(name)):
        warnings.warn('Use local network directory, `pretrained` maybe not work.')
        raise NotImplementedError('Load given path has not be supported.')
    md_name = None
    uid = None
    if name.startswith('http'):
        if len(name.split('/')) < 2:
            raise ValueError('Wrong url.')
        net_name, md_name = _get_md_and_name_from_url(name)
        uid = md_name[:-3]
    else:
        net_name, md_name = _get_md_and_name_from_name(name)
        uid = name
    path = _generate_store_path(uid)
    _create_if_not_exist(path)
    _download_file_from_url(os.path.join(HUB_MD_DIR, md_name), None, path)
    md_path = os.path.join(path, md_name.split('/')[-1])

    info = CellInfo(net_name)
    info.update(md_path)
    net = None
    if not force_reload and os.path.exists(path):
        net = _get_network_from_cache(os.path.join(path, os.path.basename(info.repo_link)), *args, **kwargs)
    else:
        net = _get_network_from_url(info.repo_link, path, *args, **kwargs)
    if not isinstance(net, nn.Cell):
        raise TypeError('`create_net should be return a `Cell` type network, but got {}.'.format(type(net)))

    if pretrained:
        load_weights(net, handle=name, force_reload=force_reload)
    return net


def load_weights(network, handle=None, force_reload=True):
    """
    Load a model from MindSpore mindspore_hub, with pertained weights.

    Args:
        network (Cell): Cell network.
        handle (str, optional): uid or url link. Default: None.
        force_reload (bool, optional): Whether to force a fresh download unconditionally. Default: False.
    """
    if not isinstance(network, nn.Cell):
        logger.error("Failed to combine the net and the parameters.")
        msg = ("Argument net should be a Cell, but got {}.".format(type(network)))
        raise TypeError(msg)

    if handle.startswith('http'):
        if len(handle.split('/')) < 2:
            raise ValueError('Wrong url.')
        net_name, md_name = _get_md_and_name_from_name(handle)
        uid = md_name[:-3]
    else:
        net_name, md_name = _get_md_and_name_from_name(handle)
        uid = handle
    path = _generate_store_path(uid)
    _create_if_not_exist(path)
    _download_file_from_url(HUB_MD_DIR + md_name, None, path)
    md_path = os.path.join(path, md_name.split('/')[-1])

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
