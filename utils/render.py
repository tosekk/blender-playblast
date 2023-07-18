# Copyright 2023 Zhandos Kadyrkulov
# SPDX-License-Identifier: GNU GPLv3

import bpy


def create_window() -> None:
    bpy.ops.wm.window_new()


def temp_window_setup() -> None:
    temp = 0
    temp_windows = []
    
    screens = bpy.data.screens.items()
    
    for name, block in screens:
        if 'temp' in name:
            temp += 1
            temp_windows.append(name)
    
    area = bpy.data.screens[temp_windows[temp - 1]].areas[0]
    
    bpy.context.scene.playblast.window_name = temp_windows[temp - 1]
    
    area.ui_type = 'IMAGE_EDITOR'


def get_space():
    area_name = bpy.context.scene.playblast.window_name
    area = bpy.data.screens[area_name].areas[0]
    space = area.spaces[0]
    
    return space


def viewport_render(frame: int, filepath: str) -> None:
    render_path = filepath.replace("####", str(frame).zfill(4))
    
    bpy.context.scene.render.filepath = render_path
    bpy.ops.render.opengl(write_still=True, view_context=True)


def update_image(frame: int, filepath: str) -> None:
    space = get_space()
    
    if bpy.data.images.get('Playblast'):
        bpy.data.images.remove(bpy.data.images["Playblast"])
    
    read_path = filepath.replace("####", str(frame).zfill(4)) + ".png"
    
    bpy.ops.image.reload()
    bpy.data.images.load(read_path)
    
    space.image = bpy.data.images[read_path.split("/")[-1]]
    space.image.name = "Playblast"


def create_playblast(frame_start: int, frame_end: int,
                     filepath: str) -> None:
    for frame in range(frame_start, frame_end + 1):
        bpy.context.scene.frame_set(frame)
        viewport_render(frame, filepath)
        update_image(frame, filepath)