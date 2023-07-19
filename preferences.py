# This software is dedicated to the public domain under the Creative Commons Zero (CC0) license.
# SPDX-License-Identifier: CC0-1.0

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