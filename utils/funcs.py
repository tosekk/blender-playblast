# This software is dedicated to the public domain under the Creative Commons Zero (CC0) license.
# SPDX-License-Identifier: CC0-1.0

import os
import shutil


import bpy


def path_setup(folder: str, name: str) -> str:
    filepath = f"//{folder}/{name}_####"
    
    return filepath


def check_for_playblast_folder(folder: str) -> None:
    curr_filepath = bpy.data.filepath
    curr_dir = os.path.dirname(curr_filepath)

    tgt_dir_path = os.path.join(curr_dir, folder)

    return os.path.exists(tgt_dir_path)


def clear_playblast_data(folder: str) -> None:
    curr_filepath = bpy.data.filepath
    curr_dir = os.path.dirname(curr_filepath)

    pb_dir_path = os.path.join(curr_dir, folder)

    try:
        shutil.rmtree(pb_dir_path)
    except Exception as e:
        print(f"Error while clearing the folder: {e}")