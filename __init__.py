# This software is dedicated to the public domain under the Creative Commons Zero (CC0) license.
# SPDX-License-Identifier: CC0-1.0

bl_info = {
    "name": "Playblast",
    "author": "Zhandos Kadyrkulov",
    "version": (0, 1),
    "blender": (3, 3, 0),
    "description": "Creates a playblast of the current animation in the specific frame range",
    "location": "Image Editor > Sidebar",
    "category": "Animation"
}


import bpy


from . import __reload__
from . import preferences
from . import ui
from . import utils


__reload__.reload_modules()


def register():
    preferences.register_classes()
    ui.register_modules()
    utils.register_modules()


def unregister():
    ui.unregister_modules()
    utils.unregister_modules()
    preferences.unregister_classes()


if __name__ == "__main__":
    register()