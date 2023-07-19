# This software is dedicated to the public domain under the Creative Commons Zero (CC0) license.
# SPDX-License-Identifier: CC0-1.0

import bpy


from . import funcs
from . import props
from . import render


def register_modules():
    props.register_classes()


def unregister_modules():
    props.unregister_classes()
