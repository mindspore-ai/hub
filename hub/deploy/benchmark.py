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
"""Benchmark interface."""

def run_benchmark(name, device, address, script):
    """
    Run benchmark.

    Args:
        name (str): The name or url of network.
        device (list): A list of target device.
        address (str): A string of device address to run benchmark.
        script (str): A path of script to run benchmark.

    Returns:
        dict, return a dictory of benchmark result.
    """
    raise NotImplementedError()
