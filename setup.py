#!/usr/bin/env python3
# encoding: utf-8
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
"""setup package."""
import os
from setuptools import setup, find_packages
from setuptools.command.egg_info import egg_info
from setuptools.command.build_py import build_py


version = '1.1'
package_name = "mindspore-hub"
cur_dir = os.path.dirname(os.path.realpath(__file__))
pkg_dir = os.path.join(cur_dir, 'build')

pwd = os.path.dirname(os.path.realpath(__file__))

def _read_file(filename):
    with open(os.path.join(pwd, filename), encoding='UTF-8') as f:
        return f.read()


readme = _read_file('README.md')
release = _read_file('RELEASE.md')

required_package = [
    'PyYAML >= 5.3',
    'mistune == 0.8.4',
]

package_data = {
    '': [
        '*.pyd',
        '*.sh',
    ]
}


def update_permissions(path):
    """
    Update permissions.

    Args:
        path (str): Target directory path.
    """
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            dir_fullpath = os.path.join(dirpath, dirname)
            os.chmod(dir_fullpath, stat.S_IREAD | stat.S_IWRITE | stat.S_IEXEC | stat.S_IRGRP | stat.S_IXGRP)
        for filename in filenames:
            file_fullpath = os.path.join(dirpath, filename)
            os.chmod(file_fullpath, stat.S_IREAD)


class EggInfo(egg_info):
    """Egg info."""
    def run(self):
        super().run()
        egg_info_dir = os.path.join(cur_dir, 'mindspore-hub.egg-info')
        update_permissions(egg_info_dir)


class BuildPy(build_py):
    """BuildPy."""
    def run(self):
        super().run()
        hub_dir = os.path.join(pkg_dir, 'lib', 'mindspore-hub')
        update_permissions(hub_dir)


setup(
    name=package_name,
    version=version,
    author='The MindSporeHub Authors',
    author_email='contact@mindspore.cn',
    url='https://www.mindspore.cn',
    download_url='https://gitee.com/mindspore/hub/tags',
    project_urls={
        'Sources': 'https://gitee.com/mindspore/hub',
        'Issue Tracker': 'https://gitee.com/mindspore/hub/issues',
    },
    description='MindSpore is a new open source deep learning training/inference '
    'framework that could be used for mobile, edge and cloud scenarios.',
    long_description="\n\n".join([readme, release]),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    package_data=package_data,
    include_package_data=True,
    cmdclass={
        'egg_info': EggInfo,
        'build_py': BuildPy,
    },
    python_requires='>=3.7',
    install_requires=required_package,
    license='Apache 2.0',
    keywords='mindspore machine learning',
)
