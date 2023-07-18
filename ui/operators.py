# Copyright 2023 Zhandos Kadyrkulov
# SPDX-License-Identifier: GNU GPLv3

import bpy
from bpy.types import Operator


from ..utils import funcs, render


class IMAGE_OT_PlayblastRender(Operator):
    """Render playblast in the set frame range"""
    bl_idname = "playblast.render_playblast"
    bl_label = "Render Playblast"
    
    def execute(self, context):
        scene = context.scene
        properties = scene.playblast
        
        render.create_window()
        render.temp_window_setup()
        
        path = funcs.path_setup(properties.render_folder, properties.render_filename)
        
        frame_start = properties.frame_start
        frame_end = properties.frame_end

        render.create_playblast(frame_start, frame_end, path)

        properties.playblast_exists = True

        return {'FINISHED'}


class IMAGE_OT_PlaybastClear(Operator):
    """Clear playblast data from the path"""
    bl_idname = "playblast.clear_playblast"
    bl_label = "Clear Playblast Folder"

    @classmethod
    def poll(cls, context):
        scene = context.scene
        properties = scene.playblast

        return properties.playblast_exists

    def execute(self, context):
        scene = context.scene
        properties = scene.playblast

        funcs.clear_playblast_data(properties.render_folder)

        return {'FINISHED'}


classes = [
    IMAGE_OT_PlayblastRender,
    IMAGE_OT_PlaybastClear
]


def register_classes():
    for cls in classes:
        bpy.utils.register_class(cls)
    

def unregister_classes():
    for cls in classes:
        bpy.utils.unregister_class(cls)