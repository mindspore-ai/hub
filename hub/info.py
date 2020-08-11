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
The information of network in hub.
"""

class CellInfo:
    """
    Information of network.

    Args:
        name (str): Network name or url.
    """
    def __init__(self, name):
        # do something to read information bellow.
        self.name = name
        self.type = None
        self.fine_tunable = False
        self.input_shape = None
        self.author = None
        self.update_time = None
        self.repo_link = None
        self.user_id = None
        self.format = None
        self.tags = None
        self.img = None
        self.backend = None
        self.allow_cache_ckpt = None
        self.dataset = None
        self.license = None
        self.have_cache = False
        self.path = None
        self.ckpt_path = None
