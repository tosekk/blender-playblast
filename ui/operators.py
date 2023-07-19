# Copyright 2023 Zhandos Kadyrkulov
# SPDX-License-Identifier: GNU GPLv3

import bpy
from bpy.props import IntProperty
from bpy.types import Operator


from ..utils import funcs, render


class IMAGE_OT_PlayblastRender(Operator):
    """Render playblast in the set frame range"""
    bl_idname = "playblast.render_playblast"
    bl_label = "Render Playblast"
    bl_icon = "RESTRICT_RENDER_OFF"
    
    _timer = None
    curr_frame = 1
    
    def modal(self, context, event):
        if event.type == 'ESC':
            self.cancel(context)
            return {'CANCELLED'}
        
        if event.type == 'TIMER':
            scene = context.scene
            properties = scene.playblast
            path = funcs.path_setup(properties.render_folder,
                                    properties.render_filename)
            
            curr_progress = int(((self.curr_frame - properties.frame_start) / 
                                (properties.frame_end - properties.frame_start)) * 100)
            
            context.window_manager.progress_update(curr_progress)
            
            if self.curr_frame <= properties.frame_end:
                context.scene.frame_set(self.curr_frame)
                render.viewport_render(self.curr_frame, path, 
                                       properties.render_viewport)
                render.update_image(self.curr_frame, path)
                
                properties.curr_frame = self.curr_frame
                
                self.curr_frame += 1
                context.scene.frame_set(self.curr_frame)
            else:
                self.cancel(context)
                properties.playblast_exists = True
                properties.curr_frame = 1
                
                return {'FINISHED'}
        
        return {'PASS_THROUGH'}
    
    def execute(self, context):
        render.create_window()
        render.temp_window_setup()
        
        wm = context.window_manager
        self._timer = wm.event_timer_add(0.1, window=context.window)
        wm.modal_handler_add(self)

        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)


class IMAGE_OT_PlaybastClear(Operator):
    """Clear playblast data from the path"""
    bl_idname = "playblast.clear_playblast"
    bl_label = "Clear Playblast Folder"
    bl_icon = "TRASH"

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


# IMAGE EDITOR OPERATORS
class IMAGE_OT_PlayblastPlayPause(Operator):
    """Operator that handles playing and pausing playblast animation"""
    bl_idname = "playblast.play_pause"
    bl_label = "Play Pause"
    
    _timer = None
    _increment_interval = 1.0 / 24.0
    _running = False
    
    def execute(self, context):
        if self._timer is None:
            self._start_timer(context)
            self._running = True
        else:
            self._stop_timer(context)
            self._running = False
        
        return {'RUNNING_MODAL'}

    
    def modal(self, context, event):
        scene = context.scene
        properties = scene.playblast
        
        if event.type == 'TIMER':
            if self._running == True:
                self._running = False
                return {'FINISHED'}
            
            if properties.curr_frame >= properties.frame_end:
                return {'FINISHED'}
            
            properties.curr_frame += 1
        
        return {'PASS_THROUGH'}

    def _start_timer(self, context):
        wm = context.window_manager
        self._timer = wm.event_timer_add(self._increment_interval, 
                                         window=context.window)
        
        wm.modal_handler_add(self)
    
    def _stop_timer(self, context):
        wm = context.window_manager
        
        wm.event_timer_remove(self._timer)
        self._timer = None


# class IMAGE_OT_PlayblastPlay(Operator):
#     """Play the playblast animation"""
#     bl_idname = "playblast.play"
#     bl_label = "Play"
    
#     def execute(self, context):
#         bpy.ops.playblast.play_pause()
        
#         return {'FINISHED'}


# class IMAGE_OT_PlayblastPause(Operator):
#     """Pause the playblast animation"""
#     bl_idname = "playblast.pause"
#     bl_label = "Pause"

#     def execute(self, context):
#         bpy.ops.playblast.play_pause()
        
#         return {'FINISHED'}


class IMAGE_OT_PlayblastFirst(Operator):
    """Move to the first frame of the playblast"""
    bl_idname = "playblast.to_first"
    bl_label = "To First"
    
    def execute(self, context):
        scene = context.scene
        properties = scene.playblast
        
        path = funcs.path_setup(properties.render_folder,
                                properties.render_filename)
        
        render.update_image(properties.frame_start, path)
        properties.curr_frame = properties.frame_start
        
        return {'FINISHED'}


class IMAGE_OT_PlayblastLast(Operator):
    """Move to the last frame of the playblast"""
    bl_idname = "playblast.to_last"
    bl_label = "To Last"
    
    def execute(self, context):
        scene = context.scene
        properties = scene.playblast
        
        path = funcs.path_setup(properties.render_folder,
                                properties.render_filename)
        
        render.update_image(properties.frame_end, path)
        properties.curr_frame = properties.frame_end
        
        return {'FINISHED'}


classes = [
    IMAGE_OT_PlayblastRender,
    IMAGE_OT_PlaybastClear,
    # IMAGE_OT_PlayblastPlayPause,
    # IMAGE_OT_PlayblastPlay,
    # IMAGE_OT_PlayblastPause,
    IMAGE_OT_PlayblastFirst,
    IMAGE_OT_PlayblastLast
]


def register_classes():
    for cls in classes:
        bpy.utils.register_class(cls)
    

def unregister_classes():
    for cls in classes:
        bpy.utils.unregister_class(cls)