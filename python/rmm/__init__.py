# Copyright (c) 2018-2019, NVIDIA CORPORATION.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import weakref

from rmm._lib.device_buffer import DeviceBuffer
from rmm.mr import _initialize
from rmm.rmm import (
    RMMError,
    RMMNumbaManager,
    _numba_memory_manager,
    device_array,
    device_array_from_ptr,
    device_array_like,
    is_initialized,
    reinitialize,
    rmm_cupy_allocator,
    to_device,
)

# Initialize RMM on import
_initialize()
