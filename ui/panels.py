# Copyright 2023 Zhandos Kadyrkulov
# SPDX-License-Identifier: GNU GPLv3

import bpy
from bpy.types import Panel


from ..utils import funcs


class PlayblastPanel:
    """Playblast Panel"""
    
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Playblast"


class IMAGE_PT_PlayblastMainPanel(Panel, PlayblastPanel):
    """Playblast Main Panel"""
    
    bl_label = "Playblast"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene


class IMAGE_PT_PlayblastRenderSettings(Panel, PlayblastPanel):
    """Playblast Render Settings UI Panel"""
    
    bl_label = "Render Settings"
    bl_parent_id = "IMAGE_PT_PlayblastMainPanel"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        properties = scene.playblast
        
        pr_col = layout.column()
        pr_col.label(text="Playblast Resolution")
        pr_col.separator()
        
        col = pr_col.column()
        col.prop(properties, "res_x")
        col.prop(properties, "res_y")
        col.separator()
        
        as_col = layout.column()
        as_col.label(text="Animation Settings")
        as_col.separator()
        
        col = as_col.column()
        col.prop(properties, "frame_start")
        col.prop(properties, "frame_end")
        col.separator()
        
        col = as_col.column()
        col.label(text="Playblast Render Path")
        col.prop(properties, "render_folder")
        col.prop(properties, "render_filename")
        
        if properties.override_filepath == False:
            col.enabled = False
        
        col = as_col.column()
        col.prop(properties, "override_filepath")
        col.separator()

        col = layout.column()
        row = col.row()
        row.operator("playblast.render_playblast")
        row.operator("playblast.clear_playblast")
        


class IMAGE_PT_PlayblastControls(Panel):
    """Playblast Controls Panel"""
    
    bl_label = "Playblast Controls"
    bl_space_type = "IMAGE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Playblast"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        properties = scene.playblast
        
        col = layout.column()
        col.label(text="Frame in View")
        col.prop(properties, "curr_frame")

        if properties.playblast_exists == False:
            col.enabled = False


classes = [
    IMAGE_PT_PlayblastMainPanel,
    IMAGE_PT_PlayblastRenderSettings,
    IMAGE_PT_PlayblastControls,
]


def register_classes():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister_classes():
    for cls in classes:
        bpy.utils.unregister_class(cls)