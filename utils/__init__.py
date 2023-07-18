# Copyright 2023 Zhandos Kadyrkulov
# SPDX-License-Identifier: GNU GPLv3

import bpy


from . import funcs
from . import props
from . import render


def register_modules():
    props.register_classes()


def unregister_modules():
    props.unregister_classes()
