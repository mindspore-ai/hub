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
"""test validate md files."""

import os
import random
from mindspore_hub.info import CellInfo


def _find_md(path, dst_depth, depth=1):
    """Find network md files."""
    mds = []
    files = os.listdir(path)
    if dst_depth < depth:
        return []

    if dst_depth == depth:
        for f in files:
            tmp = os.path.join(path, f)
            if os.path.isfile(tmp) and tmp.endswith('.md'):
                mds.append(tmp)
    else:
        for f in files:
            tmp = os.path.join(path, f)
            if os.path.isdir(tmp):
                mds += _find_md(tmp, dst_depth, depth + 1)
    return mds


def test_validate_md():
    """Test validate md files in assets folder."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    asset_dir = os.path.join(current_dir, '../../mshub_res/assets/mindspore/2.5')
    mds = _find_md(os.path.abspath(asset_dir), 1)
    for md in random.choices(mds, k=1):
        CellInfo(md)
