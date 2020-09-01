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
import re
import shutil
import importlib.util
import logging as logger
import warnings
import tempfile
from mindspore import nn
from mindspore.train.serialization import load_checkpoint, load_param_into_net
from .info import CellInfo
from ._utils.download import _download_file_from_url, _download_repo_from_url # url_exist
from .manage import get_hub_dir


HUB_CONFIG_FILE = 'mindspore_hub_conf.py'
ENTRY_POINT = 'create_network'
HUB_MD_DIR = 'https://gitee.com/mindspore/hub/raw/master/mshub_res/assets/'


def _get_network_from_cache(name, path, *args, **kwargs):
    """
    Load network from cache.

    Args:
        name (str): Network name.
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
    cwd = os.getcwd()
    os.chdir(path)
    if not hasattr(module, ENTRY_POINT):
        raise KeyError('Can\'t find `create_net` function.')
    func = getattr(module, ENTRY_POINT)
    net = func(name.lower(), *args, **kwargs)
    os.chdir(cwd)
    return net


def _delete_if_exist(path):
    """Delete backpu files"""
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


def _create_if_not_exist(path):
    """ Create not exist directory."""
    if not os.path.exists(path):
        os.makedirs(path)


def _get_md_from_url(url):
    """Get markdown name and network name from url."""
    values = url.split('/')
    return values[-1].split('.')[0] + '.md'


def _get_md_from_uid(uid):
    """Get markdown name and network name from given name."""
    return uid.split('/')[-1] + '.md'


def _get_uid_and_md_name(name):
    """Get uid and markdown name."""
    if re.match(r'^https?:/{2}\w.+$', name):
        # if not url_exist(name):
            # raise Exception('Please make sure the URL exists or the network connection is normal.')
        if len(name.split('/')) < 7:
            raise ValueError('Please make sure input correct url.')
        uid = _get_uid_from_url(name)
        md_name = _get_md_from_url(name)
    else:
        uid = name
        md_name = _get_md_from_uid(name)
    return uid, md_name


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

    hub_dir = get_hub_dir()
    _create_if_not_exist(hub_dir)

    if os.path.exists(os.path.expanduser(name)):
        warnings.warn('Use local network directory, `pretrained` maybe not work.')
        raise NotImplementedError('Load local path has not be supported.')

    uid, md_name = _get_uid_and_md_name(name)
    dirs = os.path.join(*uid.split('/')[:-1])
    target_path = os.path.join(hub_dir, dirs)
    _create_if_not_exist(target_path)

    md_path = os.path.join(target_path, md_name)
    tmp_dir = tempfile.TemporaryDirectory(dir=hub_dir)
    base_path = None
    if force_reload or (not os.path.isfile(md_path)):
        if not force_reload:
            print(f'Warning. Can\'t find markdown cache, will reloading.')
        base_path = tmp_dir.name
        tmp_path = _download_file_from_url(os.path.join(HUB_MD_DIR, dirs, md_name), None, base_path)
        _delete_if_exist(md_path)
        os.rename(tmp_path, md_path)

    info = CellInfo()
    info.update(md_path)
    basename = os.path.basename(info.repo_link)
    net_dir = os.path.join(target_path, basename)

    if force_reload or (not os.path.isdir(net_dir)):
        if not force_reload:
            print(f'Warning. Can\'t find net cache, will reloading.')
        _create_if_not_exist(os.path.dirname(net_dir))
        _download_repo_from_url(info.repo_link, base_path)
        _delete_if_exist(net_dir)
        os.rename(os.path.join(base_path, basename), net_dir)

    net = _get_network_from_cache(info.name, net_dir, *args, **kwargs)
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

    hub_dir = get_hub_dir()
    _create_if_not_exist(hub_dir)
    uid, md_name = _get_uid_and_md_name(handle)
    dirs = os.path.join(*uid.split('/')[:-1])
    target_path = os.path.join(hub_dir, dirs)
    _create_if_not_exist(target_path)

    md_path = os.path.join(target_path, md_name)
    tmp_dir = tempfile.TemporaryDirectory(dir=hub_dir)
    base_path = None
    if force_reload or (not os.path.isfile(md_path)):
        if not force_reload:
            print(f'Warning. Can\'t find markdown cache, will reloading.')
        base_path = tmp_dir.name
        tmp_path = _download_file_from_url(os.path.join(HUB_MD_DIR, dirs, md_name), None, base_path)
        os.rename(tmp_path, md_path)


    cell = CellInfo()
    cell.update(md_path)

    download_url = cell.asset[cell.asset_id]['asset-link']
    asset_sha256 = cell.asset[cell.asset_id]["asset-sha256"]

    if force_reload:
        ckpt_path = _download_file_from_url(download_url, asset_sha256, target_path)
    else:
        ckpt_name = os.path.basename(download_url.split("/")[-1])
        ckpt_path = os.path.join(target_path, ckpt_name)
        if not os.path.exists(ckpt_path):
            ckpt_path = _download_file_from_url(download_url, asset_sha256, target_path)

    param_dict = load_checkpoint(ckpt_path)
    load_param_into_net(network, param_dict)
