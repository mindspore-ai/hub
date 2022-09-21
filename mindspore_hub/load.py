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
import warnings
import tempfile
from mindspore import nn
from mindspore.train.serialization import load_checkpoint, load_param_into_net
from .info import CellInfo
from ._utils.download import _download_file_from_url, _download_repo_from_url  # url_exist
from .manage import get_hub_dir

HUB_CONFIG_FILE = 'mindspore_hub_conf.py'
ENTRY_POINT = 'create_network'


def _create_if_not_exist(path):
    """ Create not exist directory."""
    if not os.path.exists(path):
        os.makedirs(path)


def _delete_if_exist(path):
    """Delete backup files"""
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


def _get_md_file(source, uid, name, cache_path, force_reload):
    """Get the path of markdown file."""
    md_path = os.path.join(cache_path, name)
    tmp_dir = tempfile.TemporaryDirectory(dir=get_hub_dir())
    if force_reload or (not os.path.isfile(md_path)):
        if not force_reload:
            print(f'Warning. Can\'t find markdown cache, will reloading.')
        if source == 'gitee':
            hub_repo = 'https://gitee.com/mindspore/hub/'
        else:
            hub_repo = 'https://github.com/mindspore-ai/hub/'
        url = os.path.join(hub_repo, 'raw/master/mshub_res/assets/', uid + '.md')
        tmp_path = _download_file_from_url(url, None, tmp_dir.name)
        _delete_if_exist(md_path)
        os.rename(tmp_path, md_path)
    return md_path


def _get_md_from_uid(uid):
    """Get markdown name and network name from given name."""
    values = uid.split('/')
    if len(values) not in (3, 4):
        raise ValueError('Not input correct name.')
    return values[-1] + '.md'


def _get_md_from_url(url):
    """Get markdown name and network name from url."""
    values = url.split('/')
    return values[-1].split('.')[0] + '.md'


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
    sys.path.insert(0, path)
    config_path = os.path.join(os.path.abspath(path), HUB_CONFIG_FILE)
    if not os.path.exists(config_path):
        raise ValueError('{} not exists.'.format(config_path))
    spec = importlib.util.spec_from_file_location(HUB_CONFIG_FILE, config_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not hasattr(module, ENTRY_POINT):
        raise KeyError('Can\'t find `create_net` function.')
    func = getattr(module, ENTRY_POINT)
    net = func(name.lower(), *args, **kwargs)
    return net


def _get_uid_and_md_name(name):
    """Get uid and markdown name."""
    if re.match(r'^https?:/{2}\w.+$', name):
        if len(name.split('/')) < 7:
            raise ValueError('Please make sure input correct url.')
        uid = _get_uid_from_url(name)
        md_name = _get_md_from_url(name)
    else:
        uid = name
        md_name = _get_md_from_uid(name)
    return uid, md_name


def _get_uid_from_url(url):
    """Get uid from given url."""
    values = url.split('/')
    values[-1] = values[-1].split('.')[0]
    return os.path.join(*values[-3:])


def load(name, *args, source='gitee', pretrained=True, force_reload=False, **kwargs):
    r"""
    Load network with the given name. After loading, it can be used for inference verification, migration learning, etc.
    If `source` is `local`, it will load the local model, if the model is not exist in local, it will auto-download.
    If `pre_trained` is `True`, the model will load the local ckpt file, if the ckpt file is not exist in local,
    it will auto-download and load the downloaded ckpt file.

    Args:
        name (str): Uid or url of the network or local path.
        args (tuple): Arguments for network initialization.
        source (str): Whether to parse `name` as gitee model URI, github model URI or local resource. Default: gitee.
        pretrained (bool): Whether to load the pretrained model. Default: True.
        force_reload (bool): Whether to reload the network and the ckpt file from url. Default: False.
        kwargs (dict): Keyword arguments for network initialization.

    Returns:
        Cell, a network.

    Examples:
        >>> import mindspore_hub
        >>> net = mindspore_hub.load('mindspore/1.3/alexnet_cifar10', 10, pretrained=True)
        >>> # For details about how to call the parameters of the network,
        >>> # please refer to the "Usage" in the md file of the network.
        >>> #
        >>> # 1. To find the corresponding md file, there are two methods:
        >>> #
        >>> # 1.1. Find the corresponding md file from the local hub source code.
        >>> # 1.1.1. Use 'git clone' command to copy the hub repository from
        >>> # Mindspore/hub<https://gitee.com/mindspore/hub.git>. Assume that the hub repository is cloned to <D:\hub\>.
        >>> # 1.1.2. The preceding address is <D:\hub\mshub_res\assets\mindspore\1.3\alexnet_cifar10.md>.
        >>> #
        >>> # 1.2. Find the corresponding md file from the website.
        >>> # 1.2.1. The prefix is fixed: <https://gitee.com/mindspore/hub/tree/master/mshub_res/assets/>
        >>> # + <address where you want to load the md file>.
        >>> # 1.2.2. The preceding address is
        >>> # <https://gitee.com/mindspore/hub/tree/master/mshub_res/assets/
        >>> # mindspore/1.3/alexnet_cifar10.md>.
        >>> #
        >>> # 2. Want to find more information about this network?
        >>> # 2.1. Go to the corresponding website to learn more.
        >>> # 2.2. To obtain the corresponding website, perform the following steps:
        >>> # 2.2.1. After you have found the md file, there is a repo-link in the md file that allows
        >>> # you to directly access the web page of the corresponding network.
        >>> # 2.2.2. The web page corresponding to the preceding code is
        >>> # <https://gitee.com/mindspore/models/tree/r1.3/official/cv/alexnet>.
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
    if source not in ('local', 'gitee'):
        raise ValueError('`source` must be "local" or "gitee"')

    hub_dir = get_hub_dir()
    _create_if_not_exist(hub_dir)
    if source == 'local':
        warnings.warn('Use local directory, `pretrained` maybe not work.')
        md_path = os.path.realpath(os.path.expanduser(name))
        target_path = os.path.dirname(md_path)
    else:
        uid, md_name = _get_uid_and_md_name(name)
        target_path = os.path.dirname(os.path.join(hub_dir, uid))
        _create_if_not_exist(target_path)
        md_path = _get_md_file(source, uid, md_name, target_path, force_reload)

    info = CellInfo(md_path)
    basename = os.path.basename(info.repo_link).strip("<>")
    net_dir = os.path.join(target_path, basename)

    if force_reload or (not os.path.isdir(net_dir)):
        if not force_reload:
            print(f'Warning. Can\'t find net cache, will reloading.')
        _create_if_not_exist(target_path)
        _download_repo_from_url(info.repo_link, target_path)

    net = _get_network_from_cache(info.name, net_dir, *args, **kwargs)
    if not isinstance(net, nn.Cell):
        raise TypeError('`create_net` should be return a `Cell` type network, but got {}.'.format(type(net)))

    if pretrained:
        if not info.asset:
            raise ValueError(f'`pretrained` must be False when {info.name} has no asset.')
        param_dict = load_weights(name, source=source, force_reload=force_reload)
        load_param_into_net(net, param_dict)
    return net


def load_weights(name, source='gitee', force_reload=False):
    """
    Load a model from MindSpore mindspore_hub, with pertained weights.

    Args:
        name (str): Uid or url of the network.
        source (str): Whether to parse `name` as gitee model URI, github model URI or local resource. Default: gitee.
        force_reload (bool): Whether to force a fresh download unconditionally. Default: False.

    Returns:
        param_dict (dict) : Parameter dict for network weights.

    Examples:
        >>> uid = 'mindspore/1.3/alexnet_cifar10'
        >>> param_dict = load_weights(uid, source='gitee', force_reload=True)
        >>> url = 'https://gitee.com/mindspore/hub/blob/master/mshub_res/assets/mindspore/1.3/alexnet_cifar10.md'
        >>> param_dict = load_weights(url, source='gitee', force_reload=True)
    """
    hub_dir = get_hub_dir()
    _create_if_not_exist(hub_dir)
    if source == 'local':
        md_path = os.path.realpath(os.path.expanduser(name))
        target_path = os.path.dirname(md_path)
    else:
        uid, md_name = _get_uid_and_md_name(name)
        target_path = os.path.dirname(os.path.join(hub_dir, uid))
        _create_if_not_exist(target_path)
        md_path = _get_md_file(source, uid, md_name, target_path, force_reload)

    cell = CellInfo(md_path)

    download_url = cell.asset[cell.asset_id]['asset-link'].strip("<>")
    asset_sha256 = cell.asset[cell.asset_id]["asset-sha256"]

    if force_reload:
        ckpt_path = _download_file_from_url(download_url, asset_sha256, target_path)
    else:
        ckpt_name = os.path.basename(download_url.split("/")[-1])
        ckpt_path = os.path.join(target_path, ckpt_name)
        if not os.path.exists(ckpt_path):
            print(f'Warning. The `{ckpt_name}` is not exist in local, '
                  f'it will auto-download.')
            ckpt_path = _download_file_from_url(download_url, asset_sha256, target_path)

    param_dict = load_checkpoint(ckpt_path)
    return param_dict
