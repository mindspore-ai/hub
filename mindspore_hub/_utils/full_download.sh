#!/bin/bash
# Copyright 2019 Huawei Technologies Co., Ltd
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

#1.git_dir  2.save_path:.mscache 3.model_path 4.repo git 5.branch
git_dir=$1
save_path=$2
model_path=$3
repo=$4
branch=$5

cd $git_dir || exit
git clone -b $branch $repo
cd ..
rm $git_dir/$model_path/.git -rf
cp $git_dir/* $save_path -r
rm ${git_dir:?}/* -rf
if [ $? -ne 0 ]; then
  echo "failed"
else
  echo "succeed"
fi
