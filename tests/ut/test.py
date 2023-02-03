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
"""ut test of hub."""

import os
import glob
from mindspore_hub.manage import get_hub_dir, set_hub_dir
from mindspore_hub._utils.check import ValidMarkdown
from mindspore_hub.info import CellInfo
from mindspore_hub._utils.download import _download_repo_from_url, _download_file_from_url
from mindspore_hub._utils.auto_rename import auto_rename
from mindspore_hub.load import load_weights
from mindspore_hub.load import _get_network_from_cache


def test_check_md(file_path='../mshub_res/assets/mindspore/1.3/googlenet_cifar10.md'):
    """
    Feature: Check markdown file.
    Description: file_path, mindspore/1.3/googlenet_cifar10.md
    Expectation: success.
    """
    ValidMarkdown(file_path).check_markdown_file()


def test_check_md_of_dir(check_dir='../mshub_res/assets/mindspore/1.3/'):
    """
    Feature: Check markdown file if dir.
    Description: check_dir, mindspore/1.3/
    Expectation: success.
    """
    check_dir = os.path.join(check_dir, '*.md')
    for each_file in glob.glob(check_dir):
        # Skip documentation
        if os.path.basename(each_file) in ('README_CN.md', 'README.md'):
            continue
        ValidMarkdown(each_file).check_markdown_file()


def test_check_all_md_of_dir(check_dir='../mshub_res/assets/'):
    """
    Feature: Check all markdown files of dir.
    Description: check_dir, /mshub_res/assets/
    Expectation: success.
    """
    skip_check_list = ['README_CN.md', 'README.md']

    def record(folder, md_list):
        for name in os.listdir(folder):
            if os.path.isdir(os.path.join(folder, name)):
                record(os.path.join(folder, name), md_list)
            elif name.endswith('.md') and name not in skip_check_list:
                md_list.append(os.path.join(folder, name))

    markdown_list = []
    record(check_dir, markdown_list)
    for each_file in markdown_list:
        ValidMarkdown(each_file).check_markdown_file()


def test_download_ckpt():
    """
    Feature: Test download ckpt.
    Description: _download_file_from_url function
    Expectation: success.
    """
    md_path = '../mshub_res/assets/mindspore/1.3/googlenet_cifar10.md'
    cell = CellInfo("googlenet")
    cell.update(md_path)

    asset_link = cell.asset[cell.asset_id]['asset-link']
    asset_sha256 = cell.asset[cell.asset_id]["asset-sha256"]
    set_hub_dir('.cache')
    path = get_hub_dir()

    ckpt_path = _download_file_from_url(asset_link, hash_sha256=asset_sha256, save_path=path)
    assert os.path.exists(ckpt_path)


def test_download_repo():
    """
    Feature: Test download repo link.
    Description: _download_repo_from_url function
    Expectation: success.
    """
    git_url = 'https://gitee.com/mindspore/models/tree/master/research/cv/googlenet'
    set_hub_dir('.cache')
    path = get_hub_dir()
    ret = _download_repo_from_url(git_url, path)
    assert ret


def test_download_repo_of_dir():
    """
    Feature: Test download repo link of dir.
    Description: _download_repo_from_url function
    Expectation: success.
    """
    md_path = '../mshub_res/assets/mindspore/1.3/googlenet_cifar10.md'
    cell = CellInfo("googlenet")
    cell.update(md_path)

    git_url = cell.repo_link
    set_hub_dir('.cache')
    path = get_hub_dir()
    ret = _download_repo_from_url(git_url, path)
    assert ret


def test_load_weights_input_uid():
    """
    Feature: Test load_weights.
    Description: load_weights function
    Expectation: success.
    """
    set_hub_dir('.cache')
    path = get_hub_dir()

    repo_link = 'https://gitee.com/mindspore/models/tree/master/research/cv/googlenet'
    _download_repo_from_url(repo_link, path)

    net = _get_network_from_cache('GoogleNet', path + '/googlenet', 10)
    # handle = 'mindspore/1.3/googlenet_cifar10'
    load_weights(net, source='gitee', force_reload=True)
    print(net)


def test_load_weights_input_url():
    """
    Feature: Test load_weights.
    Description: load_weights function
    Expectation: success.
    """
    set_hub_dir('.cache')
    path = get_hub_dir()

    repo_link = 'https://gitee.com/mindspore/models/tree/master/research/cv/googlenet'
    _download_repo_from_url(repo_link, path)

    net = _get_network_from_cache('GoogleNet', path + '/googlenet', 10)
    # handle = 'https://hub.mindspore.com/mindspore/1.3/googlenet_cifar10'
    load_weights(net, source='gitee', force_reload=True)
    print(net)


def test_auto_rename():
    """
    Feature: Test auto_rename.
    Description: load_weights function
    Expectation: success.
    """
    test_download_ckpt()
    source_file_path = '.cache/googlenet.ckpt'
    save_path = './cache1'
    md_path = '../mshub_res/assets/mindspore/1.3/googlenet_v1_cifar10.md'
    des_file_path = auto_rename(source_file_path, save_path, md_path)
    assert os.path.exists(des_file_path)
