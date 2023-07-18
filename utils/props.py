# Copyright 2023 Zhandos Kadyrkulov
# SPDX-License-Identifier: GNU GPLv3

import bpy
from bpy.props import (BoolProperty, IntProperty, 
                       PointerProperty, StringProperty)


class PlayblastProperties(bpy.types.PropertyGroup):
    """Playblast Add-On Properties"""
    
    # Booleans
    override_filepath: BoolProperty(
        name="Override Path",
        description="Override viewport render location for current playblast",
        default=False
    )
    
    # Integers
    res_x: IntProperty(
        name="Width",
        description="Playblast image width",
        default=1920,
        subtype="PIXEL"
    )

    res_y: IntProperty(
        name="Height",
        description="Playblast image height",
        default=1080,
        subtype="PIXEL"
    )
    
    frame_start: IntProperty(
        name="Frame Start",
        description="Playblast frame range start frame number",
        default=1,
        subtype="UNSIGNED"
    )
    
    frame_end: IntProperty(
        name="Frame End",
        description="Playblast frame range end frame number",
        default=250,
        subtype="UNSIGNED"
    )
    
    curr_frame: IntProperty(
        name="Current Frame",
        description="Playblast's current frame",
        default=1,
        subtype="UNSIGNED"
    )
    
    # Strings
    render_loc: StringProperty(
        name="Playblast Output Path",
        description="Playblast output image path with extension",
        default="",
        subtype="FILE_PATH"
    )
    
    window_name: StringProperty(
        name="Playblast Window Name",
        description="Playblast viewing window name",
        default="temp"
    )


def register_classes():
    bpy.utils.register_class(PlayblastProperties)
    
    bpy.types.Scene.playblast = PointerProperty(type=PlayblastProperties)


def unregister_classes():
    bpy.utils.unregister_class(PlayblastProperties)
    
    del bpy.types.Scene.playblast