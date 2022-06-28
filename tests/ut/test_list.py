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
"""test list"""

from mindspore_hub import hub_list


class TestLoad:
    """Test list function."""

    def test_list(self):
        """
        Feature: Test normal cases.
        Description: mindspore_hub.list function
        Expectation: success.
        """
        versions = (None, 'master')
        force_reloads = (True, False)
        for version in versions:
            for force_reload in force_reloads:
                hub_list(version, force_reload)
