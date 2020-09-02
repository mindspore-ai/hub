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

version = '0.1.0'
package_name = "MindSporeHub"

pwd = os.path.dirname(os.path.realpath(__file__))

def _read_file(filename):
    with open(os.path.join(pwd, filename), encoding='UTF-8') as f:
        return f.read()


readme = _read_file('README.md')
release = _read_file('RELEASE.md')

required_package = [
    'PyYAML >= 5.3',
    'mistune >= 0.8.4',
]

package_data = {
    '': [
        '*.pyd',
    ]
}

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
    python_requires='>=3.7',
    install_requires=required_package,
    license='Apache 2.0',
    keywords='mindspore machine learning',
)
