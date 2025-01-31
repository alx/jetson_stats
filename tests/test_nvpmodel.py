# -*- coding: UTF-8 -*-
# Copyright (C) 2019, Raffaello Bonghi <raffaello@rnext.it>
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING,
# BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from jtop import NVPmodel
from jtop import JetsonClocks


def test_nvp_good():
    # Initialize NVPmodel
    nvp = NVPmodel("PC")
    # Check values
    assert isinstance(nvp.mode, str)
    assert isinstance(nvp.num, int)


def test_initialization():
    # Test board in list
    nvp = NVPmodel("PC")
    assert isinstance(nvp.modes, list)


def test_mode():
    # Test board in list
    nvp = NVPmodel("PC")
    assert nvp.mode == nvp.modes[nvp.num]["Name"]
    assert nvp.num == nvp.modes[nvp.num]["ID"]


def test_set_mode():
    # Initialize NVPmodel
    nvp = NVPmodel("PC")
    # Set value
    assert nvp.set(0)


def test_increase_mode():
    # Initialize NVPmodel
    nvp = NVPmodel("PC")
    # Set value
    assert nvp.increase()


def test_decrease_mode():
    # Initialize NVPmodel
    nvp = NVPmodel("PC")
    # Set value
    assert nvp.decrease()


def test_set_jc_mode():
    # Load JetsonClocks controller
    jc = JetsonClocks()
    jc.start = True
    # Initialize NVPmodel
    nvp = NVPmodel("PC", jetson_clocks=jc)
    # Set value
    set_status = nvp.set(0)
    # stop jc
    jc.start = False
    assert set_status
# EOF
