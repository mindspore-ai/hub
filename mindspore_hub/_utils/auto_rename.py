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
"""rename file to giving path."""

import os
import shutil
import sys
import time
from mindspore_hub._utils.check import ValidMarkdown


def auto_rename(source_file_path, save_path, md_path):
    """
    The function will auto rename file according to json file
     and copy source file to save path.

    Args:
        source_file_path (str): path of source file
        save_path (str): save path
        md_path (str): MarkDown path
    """
    if os.path.isfile(md_path):
        info_dict = ValidMarkdown(md_path).check_markdown_file()
    else:
        raise FileNotFoundError(f"{md_path} not exists")

    if os.path.isfile(source_file_path):
        # Create new file name
        file_format = os.path.splitext(source_file_path)[-1]
        name_list = [info_dict['backbone-name'], info_dict['train-backend'], info_dict['mindspore-version'],
                     info_dict['train-dataset']]
        now_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        name_list.append(now_time)
        new_file_name = '_'.join([str(x) for x in name_list]) + file_format
        new_file_name = new_file_name.replace('/', '-')

        # Create new file path
        des_file_path = os.path.join(save_path, info_dict['module-type'], info_dict['backbone-name'], new_file_name)

    # If file path is not exist, create des file path
    if not os.path.exists(os.path.dirname(des_file_path)):
        os.makedirs(os.path.dirname(des_file_path))

    # Copy file
    if source_file_path and des_file_path:
        try:
            shutil.copyfile(source_file_path, des_file_path)
        except IOError as e:
            raise Exception(e)
        except:
            raise Exception('Unexcepted error: ', sys.exc_info())

        print('Rename and copy file done!')
    return des_file_path
