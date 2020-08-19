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
"""Transfer interface."""

def transform(net, model, method, device, dataset, use_sync=False):
    """
    Transform model for model acceleration or model lightweight.

    Args:
        net (Cell): Network.
        model (str): A string of model name or a url path of model. The value is None, if not set model.
        method (str): Method used to transforming model.
        device (str): Target device.
        dataset (Dataset): Dataset used to transforming model.
        use_sync (bool): Whether to synchronize cache on cloud side.

    Returns:
        Cell, return network after transformed.
    """
    raise NotImplementedError()
