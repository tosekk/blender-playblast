# Copyright 2023 Zhandos Kadyrkulov
# SPDX-License-Identifier: MIT

import bpy
from bpy.props import (BoolProperty, IntProperty, 
                       PointerProperty, StringProperty)


from . import funcs, render


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
    
    render_viewport: BoolProperty(
        name="Render Using Viewport",
        description="Render the playblast using viewport settings, if not then use scene settings",
        default=True
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
        override={"LIBRARY_OVERRIDABLE"},
        get=lambda self: self.get_curr_frame(),
        set=lambda self, value: self.set_curr_frame(value),
        update=lambda self, context: self.show_image(context)
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
    
    def get_curr_frame(self):
        return self.get('curr_frame', 1)
    
    def set_curr_frame(self, value):
        if self.frame_start <= value <= self.frame_end:
            self['curr_frame'] = value
    
    def show_image(self, context):
        path = funcs.path_setup(self.render_folder, self.render_filename)

        render.update_image(self.curr_frame, path)



def register_classes():
    bpy.utils.register_class(PlayblastProperties)
    
    bpy.types.Scene.playblast = PointerProperty(type=PlayblastProperties)


def unregister_classes():
    bpy.utils.unregister_class(PlayblastProperties)
    
    del bpy.types.Scene.playblast