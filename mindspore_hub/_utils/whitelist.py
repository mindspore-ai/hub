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
"""White list"""
import socket
from urllib.parse import urlparse

_WHITE_LIST = ('https://download.mindspore.cn',
               'https://gitee.com/mindspore/mindspore',
               'https://github.com/mindspore-ai/mindspore')
_WHITE_LIST_INFO = None


class UrlInfo:
    def __init__(self, url):
        parsed = urlparse(url)
        self.domain = parsed.netloc
        self.ip = socket.gethostbyname(parsed.netloc)
        self.path = parsed.path

def _get_whitelist_info():
    global _WHITE_LIST_INFO
    if _WHITE_LIST_INFO is None:
        _WHITE_LIST_INFO = set()
        for url in _WHITE_LIST:
            info = UrlInfo(url)
            _WHITE_LIST_INFO.add(info)
    return _WHITE_LIST_INFO

def verify_url(url):
    """
    Verify that the URL is in the whitelist.

    Args:
        url (str): A string of url.

    Returns:
        bool, whether the url in whitlist.
    """
    target_info = UrlInfo(url)
    whitelist_info = _get_whitelist_info()
    for info in whitelist_info:
        if (target_info.ip == info.ip or target_info.domain == info.domain) and \
            target_info.path.startswith(info.path):
            return True
    return False
