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
import tempfile
import re
import subprocess
import hashlib
import errno
import stat
import urllib
from urllib.request import urlretrieve, HTTPError, URLError
from mindspore_hub.manage import get_hub_dir

REPO_INFO_LEN = 5
REAL_PATH = os.path.split(os.path.realpath(__file__))[0]
SPARSE_SHELL_PATH = os.path.join(REAL_PATH, "sparse_download.sh")
FULL_SHELL_PATH = os.path.join(REAL_PATH, "full_download.sh")
MAX_FILE_SIZE = 5 * 1024 * 1024 * 1024  # 5GB
SUFFIX_LIST = ['.ckpt', '.air', '.geir', '.meta', '.onnx', '.md']


def handle_remove_read_only(func, path, exc):
    exc_value = exc[1]
    if func in (os.rmdir, os.remove, os.unlink) and exc_value.errno == errno.EACCES:
        os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
        func(path)


def url_exist(url):
    """
    Whether the url exist.
    """
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    try:
        opener.open(url)
        return True
    except HTTPError as e:
        print(e.code)
    except URLError as e:
        print(e.reason)
    return False


def _unpacking_targz(input_filename, save_path):
    """
    Unpacking the input filename to dirs.
    """
    try:
        t = tarfile.open(input_filename)
        t.extractall(path=save_path)
    except Exception as e:
        raise OSError("Cannot untar file {} for - {}".format(input_filename, e))


def _remove_path_if_exists(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path, ignore_errors=False, onerror=handle_remove_read_only)


def _create_path_if_not_exists(path):
    if not os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
        else:
            os.mkdir(path)


def get_repo_info_from_url(git_url):
    """
    Get repo information from url.
    """
    if git_url is None:
        return None
    git_url = git_url.strip('<>')
    git_url = git_url.rstrip('/')
    webs_name = re.findall(".*http[s]?://(.*).com.*", git_url)
    if len(webs_name) != 1:
        raise ValueError("invalid repo link: {}".format(git_url))
    web_name = webs_name[0]

    prefix = re.findall(r'http[s]?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', git_url)
    if len(prefix) != 1:
        raise ValueError("invalid repo link: {}".format(git_url))

    suffix = git_url[len(prefix[0]):].lstrip('/')
    repo_info = suffix.split("/", REPO_INFO_LEN-1)

    git_info = dict()
    git_info["is_repo"] = True

    if len(repo_info) == 2:
        uid = ':'.join([web_name, repo_info[1], "master"])
        git_info["branch"] = "master"
        git_info["dst_dir"] = repo_info[1]

    elif len(repo_info) == REPO_INFO_LEN - 1:
        if repo_info[2] != 'tree' and repo_info[2] != 'blob':
            raise ValueError("invalid repo link: {}".format(git_url))
        uid = ':'.join([web_name, repo_info[1], repo_info[3]])
        git_info["branch"] = repo_info[3]
        git_info["dst_dir"] = repo_info[1]

    elif len(repo_info) == REPO_INFO_LEN:
        if repo_info[2] != 'tree' and repo_info[2] != 'blob':
            raise ValueError("invalid repo link: {}".format(git_url))
        uid = ':'.join([web_name, repo_info[4], repo_info[3]])
        git_info["branch"] = repo_info[3]
        git_info["dst_dir"] = repo_info[4]

        git_info["is_repo"] = False

    else:
        raise ValueError("invalid repo link: {}".format(git_url))

    git_info["web"] = prefix[0]
    git_info["group"] = repo_info[0]
    git_info["repo"] = repo_info[1]

    git_ssh = '/'.join([git_info["web"], git_info["group"], git_info["repo"]])
    git_ssh = ''.join([git_ssh, ".git"])

    git_info["git_ssh"] = git_ssh
    git_info["uid"] = uid

    return git_info


def _download_repo_from_url(url, path=get_hub_dir()):
    """
    Download file form url.

    Args:
        url (str): A url to download file.
        path (str): A path to store download file.

    Returns:
        bool, return whether success download file.
    """
    _create_path_if_not_exists(path)

    repo_infos = get_repo_info_from_url(url)
    arg = dict()
    arg["bash"] = "bash"
    arg["git_ssh"] = repo_infos["git_ssh"]
    arg["path"] = path
    arg["model_path"] = repo_infos["dst_dir"]
    arg["branch"] = repo_infos["branch"]
    is_repo = repo_infos["is_repo"]

    with tempfile.TemporaryDirectory() as git_dir:
        arg["git_dir"] = git_dir

        # is repo or dir of repo
        if is_repo:
            arg["shell_path"] = FULL_SHELL_PATH
        else:
            arg["shell_path"] = SPARSE_SHELL_PATH

        cmd = [arg["bash"], arg["shell_path"], arg["git_dir"], arg["path"],
               arg["model_path"], arg["git_ssh"], arg["branch"]]
        out = subprocess.check_output(cmd, shell=False)
        ret = "succeed" in out.decode('utf-8')
        return ret


def extract_file(file_path, dst):
    """
    Extract file to specified path.

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
        path = os.path.join(dst, name)
        if os.path.isdir(path):
            files = os.listdir(path)
            for item in files:
                shutil.move(path + item, dst)
            shutil.rmtree(path)


def _download_file_from_url(url, hash_sha256=None, save_path=get_hub_dir()):
    """
    download checkpoint weight from giving url.

    Args:
       url(string): checkpoint url path.
       hash_sha256(string): checkpoint file sha256.
       save_path(string): checkpoint download save path.

    Returns:
       string.
    """

    def reporthook(a, b, c):
        percent = a * b * 100.0 / c
        percent = 100 if percent > 100 else percent
        if c > 0:
            print("\rDownloading...%5.1f%%" % percent, end="")

    def sha256sum(file_name, hash_sha256):
        fp = open(file_name, 'rb')
        content = fp.read()
        fp.close()
        m = hashlib.sha256()
        m.update(content)
        download_sha256 = m.hexdigest()
        return download_sha256 == hash_sha256

    _create_path_if_not_exists(os.path.realpath(save_path))
    ckpt_name = os.path.basename(url.split("/")[-1])
    # identify file exist or not
    file_path = os.path.join(save_path, ckpt_name)
    if os.path.isfile(file_path):
        if hash_sha256 and sha256sum(file_path, hash_sha256):
            print('File already exists!')
            return file_path
        print('File already exists, but sha256 checking failed. Will download again')

    _remove_path_if_exists(file_path)

    # download the checkpoint file
    print('Downloading data from url {}'.format(url))
    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        urlretrieve(url, file_path, reporthook=reporthook)
    except HTTPError as e:
        raise Exception(e.code, e.msg, url)
    except URLError as e:
        raise Exception(e.errno, e.reason, url)
    print('\nDownload finished!')

    # Check file integrity
    if hash_sha256:
        result = sha256sum(file_path, hash_sha256)
        if not result:
            raise Exception('INTEGRITY ERROR: File: {} is not integral'.format(file_path))

    # Check file size
    # Get file size and turn the file size to Mb format
    file_size = os.path.getsize(file_path)
    if file_size < 1024 * 10:
        print('File size = %.2f kb' % (file_size / 1024))
    elif file_size < 1024 * 1024 * 1024:
        print('File size = %.2f Mb' % (file_size / 1024 / 1024))
    else:
        print('File size = %.2f Gb' % (file_size / 1024 / 1024 / 1024))
    # Start check
    if file_size > MAX_FILE_SIZE:
        os.remove(file_path)
        raise Exception('SIZE ERROR: Download file is too large,'
                        'the max size is {}Mb'.format(MAX_FILE_SIZE / 1024 / 1024))

    # Check file type
    suffix = os.path.splitext(file_path)[1]
    if suffix not in SUFFIX_LIST:
        os.remove(file_path)
        raise Exception('SUFFIX ERROR: File: {} with Suffix: {} '
                        'can not be recognized'.format(file_path, suffix))
    return file_path
