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
"""Download or extract file."""

import os
import shutil
import zipfile
import tarfile


def download_url_to_file(url, path):
    """
    Download file form url.

    Args:
        url (str): A url to download file.
        path (str): A path to store download file.

    Returns:
        bool, return whether success downlad file.
    """
    raise NotImplementedError()


def extract_file(file_path, dst):
    """
    Extrace file to specified path.

    Args:
        file_path (str): The path of compressed file.
        dst (str): The target path.
    """
    name = None
    if zipfile.is_zipfile(file_path):
        with zipfile.ZipFile(file_path) as cached_zipfile:
            cached_zipfile.extractall(dst)
            name = cached_zipfile.infolist()[0].filename
    if tarfile.is_tarfile(file_path):
        with tarfile.TarFile(file_path) as cached_tarfile:
            cached_tarfile.extractall(dst)
            name = cached_tarfile.infolist()[0].filename

    if isinstance(name, str):
        path = dst + '/' + name
        if os.path.isdir(path):
            files = os.listdir(path)
            for item in files:
                shutil.move(path + item, dst)
            shutil.rmtree(path)
