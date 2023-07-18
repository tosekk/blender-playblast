# Copyright 2023 Zhandos Kadyrkulov
# SPDX-License-Identifier: GNU GPLv3

import bpy


class PlayblastPreferences(bpy.types.AddonPreferences):
    """Playblast Add-On Preferences"""
    
    bl_idname = __package__
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        properties = scene.playblast

        layout.label(text="Playblast Add-On Preferences")
        layout.prop(properties, "render_folder")
        layout.prop(properties, "render_filename")


def register_classes():
    bpy.utils.register_class(PlayblastPreferences)


def unregister_classes():
    bpy.utils.unregister_class(PlayblastPreferences)