# This software is dedicated to the public domain under the Creative Commons Zero (CC0) license.
# SPDX-License-Identifier: CC0-1.0

import sys
from importlib import reload


import bpy


from . import preferences
from . import ui
from . import utils


def reload_modules():
    if not bpy.context.preferences.view.show_developer_ui:
        return
    
    reload(sys.modules[__name__])
    reload(preferences)
    reload(ui)
    reload(utils)