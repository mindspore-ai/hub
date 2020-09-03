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
"""Expose markdown validator to model submitter."""

import os
import argparse
from mindspore_hub._utils.check import ValidMarkdown


def parse_args():
    args_parser = argparse.ArgumentParser("Get Sha256 from specific file")
    args_parser.add_argument("--check_path", type=str, default="../assets/",
                             help="Resource Directory or path of the Markdown file")
    return args_parser.parse_args()


def check_md_of_path(check_dir='../assets/'):
    """check all markdown files of dir."""
    skip_check_list = ['README_CN.md', 'README.md']
    if not os.path.exists(check_dir):
        print(f"{check_dir} does not exist!")

    def record(folder, md_list):
        for name in os.listdir(folder):
            if os.path.isdir(os.path.join(folder, name)):
                record(os.path.join(folder, name), md_list)
            elif name.endswith('.md') and name not in skip_check_list:
                md_list.append(os.path.join(folder, name))

    markdown_list = []
    if os.path.isdir(check_dir):
        record(check_dir, markdown_list)
        print(f"Checking Directory {check_dir}, totally have {len(markdown_list)} markdown files.")
    elif os.path.isfile(check_dir):
        if check_dir.endswith(".md"):
            markdown_list.append(check_dir)
        else:
            print(f"Input Path {check_dir} does not end with .md")

    if not markdown_list:
        print(f"Don't have any Markdown file in the Directory {check_dir}")
    pass_flag = True
    for each_file in markdown_list:
        try:
            ValidMarkdown(each_file).check_markdown_file()
        except (ValueError, TypeError) as e:
            pass_flag = False
            print(f"{each_file} cannot pass the examination of the markdown file checker, "
                  f"error message is '{e}'")
    if pass_flag:
        print("\033[1;32mAll Passed!\033[0m")
    else:
        print("\033[1;31mFailed!\033[0m")


if __name__ == "__main__":
    args = parse_args()
    check_md_of_path(args.check_path)
