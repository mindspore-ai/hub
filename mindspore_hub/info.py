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
The information of network in mindspore_hub.
"""

from ._utils.check import ValidMarkdown


class CellInfo:
    """
    Information of network.
    """
    def __init__(self, md_path):
        json_dict = ValidMarkdown(md_path).check_markdown_file()
        self.name = json_dict.get('model-name')
        self.backbone_name = json_dict.get('backbone-name')
        self.type = json_dict.get('module-type')
        self.fine_tunable = json_dict.get('fine-tunable')
        self.input_shape = json_dict.get('input-shape')
        self.author = json_dict.get('author')
        self.update_time = json_dict.get('update-time')
        self.repo_link = json_dict.get('repo-link')
        self.user_id = json_dict.get('user-id')
        self.backend = json_dict.get('backend')
        if json_dict.get('allow-cache-ckpt') is not None:
            self.allow_cache_ckpt = json_dict.get('allow-cache-ckpt')
        self.dataset = json_dict.get('train-dataset')
        self.license = json_dict.get('license')
        self.accuracy = json_dict.get('accuracy')
        self.used_for = json_dict.get('used-for')
        self.model_version = json_dict.get('model-version')
        self.mindspore_version = json_dict.get('mindspore-version')
        self.asset = json_dict.get('asset')
        self.asset_id = json_dict.get('asset-id')
        self.evaluation = json_dict.get('evaluation')
