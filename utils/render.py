# This software is dedicated to the public domain under the Creative Commons Zero (CC0) license.
# SPDX-License-Identifier: CC0-1.0

import bpy


def create_window() -> None:
    wm = bpy.context.window_manager
    
    if len(wm.windows.items()) == 1:
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
    space = area.spaces.active
    
    return space


def viewport_render(frame: int, filepath: str) -> None:
    render_path = filepath.replace("####", str(frame).zfill(4))
    
    scene = bpy.context.scene
    properties = scene.playblast
    
    scene.render.filepath = render_path
    scene.render.image_settings.file_format = "PNG"
    
    scene.render.resolution_x = properties.res_x
    scene.render.resolution_y = properties.res_y


def update_image(frame: int, filepath: str) -> None:
    space = get_space()

    bpy.ops.image.reload()
    
    if bpy.data.images.get('Playblast'):
        bpy.data.images.remove(bpy.data.images["Playblast"])
    
    frame_str = str(frame).zfill(4)
    read_path = filepath.replace("####", frame_str) + ".png"

    try:
        image = bpy.data.images.load(read_path)
        image.name = "Playblast"

        space.image = image
    except RuntimeError:
        print(f"There is no such frame: {frame_str}")