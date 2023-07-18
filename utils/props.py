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

    playblast_exists: BoolProperty(
        name="Playblast Exists",
        description="Status that indicates if playblast exists",
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
        subtype="UNSIGNED",
        min=1
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
        subtype="UNSIGNED",
        min=1
    )
    
    # Strings
    render_folder: StringProperty(
        name="Folder Name",
        description="Playblast output folder",
        default="playblast"
    )

    render_filename: StringProperty(
        name="Filename",
        description="Playblast output image filename",
        default="frame"
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