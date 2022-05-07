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

Loading network definition or pretrained model from mindspore mindspore_hub.
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


def _get_uid_from_url(url):
    """Get uid from given url."""
    values = url.split('/')
    values[-1] = values[-1].split('.')[0]
    return os.path.join(*values[-4:])


def _get_md_from_url(url):
    """Get markdown name and network name from url."""
    values = url.split('/')
    return values[-1].split('.')[0] + '.md'


def _get_md_from_uid(uid):
    """Get markdown name and network name from given name."""
    values = uid.split('/')
    if len(values) != 4:
        raise ValueError('Not input correct name.')
    return values[-1] + '.md'


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


def _get_md_file(uid, name, cache_path, force_reload):
    """Get the path of markdown file."""
    md_path = os.path.join(cache_path, name)
    tmp_dir = tempfile.TemporaryDirectory(dir=get_hub_dir())
    if force_reload or (not os.path.isfile(md_path)):
        if not force_reload:
            print(f'Warning. Can\'t find markdown cache, will reloading.')
        tmp_path = _download_file_from_url(os.path.join(HUB_MD_DIR, uid + '.md'), None, tmp_dir.name)
        _delete_if_exist(md_path)
        os.rename(tmp_path, md_path)
    return md_path


def load(name, *args, pretrained=True, force_reload=True, **kwargs):
    r"""
    Load network with the given name. After loading, it can be used for inference verification, migration learning, etc.

    Args:
        name (str): Uid or url of the network.
        args (tuple): Arguments for network initialization.
        pretrained (bool): Whether to load the pretrained model. Default: True.
        force_reload (bool): Whether to reload the network from url. Default: True.
        kwargs (dict): Keyword arguments for network initialization.

    Returns:
        Cell, a network.

    Examples:
        >>> net = mindspore_hub.load('mindspore/ascend/1.1/alexnet_v1.1_cifar10', 10, pretrained=True)
        >>> # For details about how to call the parameters of the network,
        >>> # please refer to the "Usage" in the md file of the network.
        >>> #
        >>> # 1. To find the corresponding md file, there are two methods:
        >>> #
        >>> # 1.1. Find the corresponding md file from the local hub source code.
        >>> # 1.1.1. Use 'git clone' command to copy the hub repository from
        >>> # Mindspore/hub<https://gitee.com/mindspore/hub.git>. Assume that the hub repository is cloned to <D:\hub\>.
        >>> # 1.1.2. The preceding address is <D:\hub\mshub_res\assets\mindspore\ascend\1.1\alexnet_v1.1_cifar10.md>.
        >>> #
        >>> # 1.2. Find the corresponding md file from the website.
        >>> # 1.2.1. The prefix is fixed: <https://gitee.com/mindspore/hub/tree/master/mshub_res/assets/>
        >>> # + <address where you want to load the md file>.
        >>> # 1.2.2. The preceding address is
        >>> # <https://gitee.com/mindspore/hub/tree/master/mshub_res/assets/
        >>> # mindspore/ascend/1.1/alexnet_v1.1_cifar10.md>.
        >>> #
        >>> # 2. Want to find more information about this network?
        >>> # 2.1. Go to the corresponding website to learn more.
        >>> # 2.2. To obtain the corresponding website, perform the following steps:
        >>> # 2.2.1. After you have found the md file, there is a repo-link in the md file that allows
        >>> # you to directly access the web page of the corresponding network.
        >>> # 2.2.2. The web page corresponding to the preceding code is
        >>> # <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/alexnet>.
        >>> #
        >>> # 2.3. The web page of operation 2.2 contains a "mindspore_hub_conf.py",
        >>> # which is invoked by the load function. Therefore, to call more parameters,
        >>> # or if you want to DIY interfaces to be called, you can modify this file.
        >>> # It is recommended that you back up the mindspore_hub_conf.py file.
        >>> # 2.4. In addition to the function of mindspore_hub_conf.py, you can also call files in the src files of the
        >>> # corresponding web page. More Alexnet network information can be obtained from here.
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
    target_path = os.path.dirname(os.path.join(hub_dir, uid))
    _create_if_not_exist(target_path)

    md_path = _get_md_file(uid, md_name, target_path, force_reload)
    info = CellInfo(md_path)
    basename = os.path.basename(info.repo_link).strip("<>")
    net_dir = os.path.join(target_path, basename)

    if force_reload or (not os.path.isdir(net_dir)):
        if not force_reload:
            print(f'Warning. Can\'t find net cache, will reloading.')
        _create_if_not_exist(os.path.dirname(net_dir))
        tmp_dir = tempfile.TemporaryDirectory(dir=get_hub_dir())
        _download_repo_from_url(info.repo_link, tmp_dir.name)
        _delete_if_exist(net_dir)
        os.rename(os.path.join(tmp_dir.name, basename), net_dir)

    net = _get_network_from_cache(info.name, net_dir, *args, **kwargs)
    if not isinstance(net, nn.Cell):
        raise TypeError('`create_net` should be return a `Cell` type network, but got {}.'.format(type(net)))

    if pretrained:
        if not info.asset:
            raise ValueError(f'`pretrained` must be False when {info.name} has no asset.')
        load_weights(net, handle=name, force_reload=force_reload)
    return net


def load_weights(network, handle=None, force_reload=True):
    """
    Load a model from MindSpore mindspore_hub, with pertained weights.

    Args:
        network (Cell): Cell network.
        handle (str, optional): Uid or url link. Default: None.
        force_reload (bool, optional): Whether to force a fresh download unconditionally. Default: False.

    Examples:
        >>> uid = 'mindspore/ascend/1.2/googlenet_v1_cifar10'
        >>> load_weights(net, handle=uid, force_reload=True)
        >>> url = 'https://gitee.com/mindspore/hub/tree/master/mshub_res/assets/mindspore/ascend/1.2/googlenet_v1.2_cifar10.md'
        >>> load_weights(net, handle=url, force_reload=True)
    """
    if not isinstance(network, nn.Cell):
        logger.error("Failed to combine the net and the parameters.")
        msg = ("Argument net should be a Cell, but got {}.".format(type(network)))
        raise TypeError(msg)

    hub_dir = get_hub_dir()
    _create_if_not_exist(hub_dir)
    uid, md_name = _get_uid_and_md_name(handle)
    target_path = os.path.dirname(os.path.join(hub_dir, uid))
    _create_if_not_exist(target_path)

    md_path = _get_md_file(uid, md_name, target_path, force_reload)
    cell = CellInfo(md_path)

    download_url = cell.asset[cell.asset_id]['asset-link'].strip("<>")
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
