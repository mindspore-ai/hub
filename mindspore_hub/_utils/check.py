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
Check MarkDown files in hub and extract info to the json file.
"""

import argparse
import os
import glob
import ssl
import json
import numbers
from urllib.request import Request, urlopen, HTTPError
import yaml
import mistune
from mindspore_hub._utils.download import get_repo_info_from_url
from mindspore_hub._utils.whitelist import verify_url


class ValidMarkdown:
    r"""
    Check MarkDown files in hub and extract info.
    """
    def __init__(self, filename):
        self.filename = filename
        self.required_user_fields = ['backbone-name', 'module-type', 'fine-tunable', 'input-shape', 'model-version',
                                     'author', 'update-time', 'repo-link', 'user-id', 'used-for', 'infer-backend',
                                     'mindspore-version', 'license', 'summary']
        self.optional_backend_fields = 'train-backend'
        self.optional_image_fields = ['featured-image']
        self.optional_accuracy_field = 'accuracy'
        self.optional_allow_cache_ckpt_field = 'allow-cache-ckpt'

        self.valid_module_type = ['audio', 'cv', 'nlp', 'recommend', 'other']
        self.valid_train_dataset = ['widerface', 'cifar10', 'cifar100', 'zh-wiki', 'Gigaword corpus', 'captcha 0.1.1',
                                    'sentence', 'sst2', 'zhwiki', 'citeseer', 'imagenet2017',
                                    'musictag', 'yelp', 'movilens', 'subj', 'criteio',
                                    'amazonbeauty', 'voc2017', 'mr', 'icdar', 'wmtende',
                                    'MJSynth', 'Speech Commands Version1', 'MagnaTagATune', 'ml-1m', 'wmtende',
                                    'imagenet2012', 'cora', 'icdar2015', 'coco2014',
                                    'captcha', 'coco2017', 'dpbedia', 'imagenet', 'isbi', 'cn-wiki',
                                    'openimage', 'Oxford-IIIT Pet', 'mnist', 'MLPerf v0.7 dataset',
                                    'Rain100L', 'Set14', 'Set5', 'en-wiki']
        self.valid_file_format = ['air', 'ckpt', 'onnx', 'mindir', 'mslite']
        self.valid_used_for = ['inference', 'extract-feature', 'transfer-learning']
        self.valid_backend = ['cpu', 'gpu', 'ascend']

        self.valid_categories = ['researchers', 'developers']
        # The current sections list below will be required.
        # If necessary, please add it, like 'Model Description'.
        self.required_sections = []

    def _validate_asset(self, assets):
        require_keys = ["asset-link", "asset-sha256", "file-format"]
        for asset in assets:
            for k in require_keys:
                if k not in asset:
                    raise ValueError('field: ``{}`` is required in {}, but not found.'
                                     .format(k, self.filename))
            self._validate_repo_link(asset['asset-link'])
            self._validate_file_format(asset['file-format'])

    def _validate_repo_link(self, link):
        r"""
        Make sure the github or gitee repo exists
        """
        if link is None:
            return
        link = link.strip('<>')
        if not verify_url(link):
            raise ValueError('url: ``{}`` is not trust in {}'.format(link, self.filename))

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        try:
            req = Request(link, headers={'User-Agent': 'ms.hub'})
            urlopen(req, context=ctx)
        except HTTPError:
            raise ValueError('``{}`` is not valid url in {}'.format(link, self.filename))

    def _validate_train_dataset(self, train_dataset):
        r"""
        Only allow train_dataset in predefined set
        """
        if train_dataset not in self.valid_train_dataset:
            raise ValueError('train_dataset ``{}`` is not valid in {}. Choose from {}'
                             .format(train_dataset, self.filename, self.valid_train_dataset))

    def _validate_file_format(self, file_format):
        r"""
        Only allow file_format in predefined set
        """
        if file_format.lower() not in self.valid_file_format:
            raise ValueError('file_format ``{}`` is not valid in {}. Choose from {}'
                             .format(file_format, self.filename, self.valid_file_format))

    def _validate_used_for(self, used_for):
        r"""
        Only allow used_for in predefined set
        """
        used_for_list = used_for.split('/')
        for item in used_for_list:
            if item.lower() not in self.valid_used_for:
                raise ValueError('used_for ``{}`` is not valid in {}. Choose from {}'
                                 .format(item, self.filename, self.valid_used_for))

    def _validate_backend(self, backend):
        r"""
        Only allow file_format in predefined set
        """
        backend_lst = backend.split('/')
        for bk in backend_lst:
            if bk.lower() not in self.valid_backend:
                raise ValueError('backend ``{}`` is not valid in {}. Choose from {}'
                                 .format(bk, self.filename, self.valid_backend))

    def _validate_module_type(self, module_type):
        r"""
        Only allow module_type in predefined set
        """
        items = module_type.lower().split('-')
        if len(items) > 2:
            raise Exception("module-type could only no more than one '-' ")
        first_class = items[0]
        if first_class not in self.valid_module_type:
            raise ValueError('module_type ``{}`` is not valid in {}. Valid module_type set is {}'
                             .format(module_type, self.filename, self.valid_module_type))

    def _validate_image(self, image_name):
        r"""
        Make sure reference image exists in images/
        """
        images = [os.path.basename(i) for i in glob.glob('images/*')] \
                 + ['no-image']
        if image_name not in images:
            raise ValueError('Image ``{}`` referenced in {} not found in images/'
                             .format(image_name, self.filename))

    def _validate_header(self, header):
        r"""
        Make sure the header is in the required format
        """
        for field in self.required_user_fields:
            if field not in header:
                raise ValueError("field: ``{}`` is required in {}, but not found."
                                 .format(field, self.filename))

        if not isinstance(header['fine-tunable'], bool):
            raise TypeError("`fine-tunable` must be `bool`, but got {}".format(header['fine-tunable']))

        if not isinstance(header['input-shape'], list):
            raise TypeError("`input-shape` must be `list` of `int`, but got {}".format(header['input-shape']))
        for i in header['input-shape']:
            if not isinstance(i, int) and not isinstance(i, list):
                raise TypeError("`input-shape` must be `list` of `int`, but got {}".format(header['input-shape']))

        self._validate_repo_link(header['repo-link'])
        if header.get('train-dataset', None):
            self._validate_train_dataset(header['train-dataset'])
        self._validate_used_for(header['used-for'])
        self._validate_backend(header['infer-backend'])
        self._validate_module_type(header['module-type'])
        if header.get('asset', None):
            self._validate_asset(header['asset'])

        for field in self.optional_image_fields:
            if field in header.keys():
                self._validate_image(header[field])

        if self.optional_accuracy_field in header.keys():
            if not isinstance(header[self.optional_accuracy_field], numbers.Number):
                raise TypeError("`accuracy` must be `number`, but got {}".
                                format(header[self.optional_accuracy_field]))

        if self.optional_allow_cache_ckpt_field in header.keys():
            if not isinstance(header[self.optional_allow_cache_ckpt_field], bool):
                raise TypeError("`allow-cache-ckpt` must be `bool`, but got {}".
                                format(header[self.optional_allow_cache_ckpt_field]))

        if self.optional_backend_fields in header.keys():
            self._validate_backend(header[self.optional_backend_fields])

        for k in header.keys():
            if k not in ('repo-link', 'asset'):
                self._no_extra_colon(k, header[k])

    def _no_extra_colon(self, field, value):
        if ':' in str(value):
            raise ValueError('Remove extra \':\' in field ``{}`` with value ``{}`` in file ``{}``'
                             .format(field, value, self.filename))

    def validate_markdown(self, markdown):
        r"""
        Validate MarkDown with required sections.
        """
        m = mistune.Markdown()
        blocks = m.block(mistune.preprocessing(markdown))

        for block in blocks:
            if block['type'] == 'heading':
                # we dont want colon after section names
                assert not block['text'].endswith(':')
                if block['text'] in self.required_sections:
                    self.required_sections.remove(block['text'])

        if self.required_sections:
            raise ValueError("Missing required sections: {}".format(self.required_sections))

    def check_markdown_file(self):
        r"""
        Check MarkDown file with yaml.
        """
        print('Checking {}...'.format(self.filename), end="")
        try:
            header = []
            markdown = []
            header_read = False
            flag_num = 0
            with open(self.filename, 'r') as file:
                for line in file:
                    if line.startswith('---'):
                        header_read = not header_read
                        flag_num += 1
                        continue
                    if header_read:
                        header += [line]
                    else:
                        markdown += [line]

            if flag_num != 2:
                raise TypeError("MarkDown file: {} should have two '---'.".format(self.filename))
            # checks that it's valid yamp
            header = yaml.load(''.join(header), Loader=yaml.FullLoader)
            if not header:
                raise TypeError("Failed to parse a valid yaml header")

            module_type_list = header['module-type'].split('-', 1)
            header['module-type'] = module_type_list[0]
            if len(module_type_list) > 1:
                header['module-type-detail'] = module_type_list[1]

            self._validate_header(header)

            # check markdown
            markdown = "".join(markdown)
            self.validate_markdown(markdown)

            header_dict = dict(header)
            header_dict["markdown_name"] = os.path.basename(os.path.splitext(self.filename)[0])
            git_info = get_repo_info_from_url(header_dict.get("repo-link"))
            if git_info is None:
                header_dict["uid"] = ''
            else:
                header_dict["uid"] = get_repo_info_from_url(header_dict.get("repo-link")).get("uid")
            asset_id = 0
            if header_dict.get("asset", None):
                for idx in range(len(header_dict["asset"])):
                    if header_dict["asset"][idx]["file-format"].lower() == "ckpt":
                        asset_id = idx
                header_dict["asset-id"] = asset_id
        except (TypeError, ValueError) as e:
            print("\033[1;31m Failed\033[0m")
            raise e

        print("\033[1;32mPassed!\033[0m")
        return header_dict

    def extract_info_to_json(self, json_path):
        header = self.check_markdown_file()
        json_str = json.dumps(header, indent=4, sort_keys=False, default=str)
        with open(json_path, 'w') as json_file:
            json_file.write(json_str)


def sanity_check(json_path, check_dir=''):
    check_dir = os.path.join(check_dir, '*.md')
    with open(json_path, "w") as json_file:
        for each_file in glob.glob(check_dir):
            # Skip documentation
            if os.path.basename(each_file) in ('README_CN.md', 'README.md'):
                continue
            headers = ValidMarkdown(each_file).check_markdown_file()
            json_str = json.dumps(headers, sort_keys=False, default=str, ensure_ascii=False)
            json_file.write(json_str + '\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('json_path', default='markdown_info.json', help='write into json file')
    parser.add_argument('-f', '--file', default=None, help='filename')
    parser.add_argument('-d', '--dir', default=None, help='check-directory.'
                                                          'When --file is given, --dir is useless.')
    args = parser.parse_args()
    if args.file:
        # args.dir is useless
        header_md = ValidMarkdown(args.file).check_markdown_file()
        json_string = json.dumps(header_md, sort_keys=False, default=str, ensure_ascii=False)
        with open(args.json_path, 'w') as f:
            f.write(json_string)
    else:
        if args.dir:
            sanity_check(args.json_path, args.dir)
        else:
            sanity_check(args.json_path)
