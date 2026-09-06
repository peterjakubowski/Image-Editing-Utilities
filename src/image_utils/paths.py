# Python-based image editing utilities
#
# Author: Peter Jakubowski
# Date: 9/6/2026
# Description: Python helper functions for image editing
#

import os
from pathlib import Path
from typing import Literal, get_args

# ========================================
# === Function for listing image paths ===
# ========================================


AllowedExtensions = Literal["jpg", "jpeg", "tif", "tiff", "png", "nef", "cr2", "dng"]

ALL_ALLOWED_EXTENSIONS: tuple[AllowedExtensions, ...] = get_args(AllowedExtensions)


def list_image_paths(
        folder_path: Path,
        allowed_extensions: AllowedExtensions | tuple[AllowedExtensions, ...] = ALL_ALLOWED_EXTENSIONS) -> list[Path]:
    """Given a folder path, return a list of paths for all images in the folder.

    :param folder_path: Pathname for the folder of images
    :param allowed_extensions: Allowed image types / file extensions
    """

    if not isinstance(folder_path, Path):
        raise TypeError("Folder path must be a pathlib.Path object.")

    elif not folder_path.exists():
        raise ValueError("Path must be to a folder that already exists.")

    elif not folder_path.is_dir():
        raise ValueError("Path must be to a folder.")

    res = []

    for file_name in os.listdir(folder_path):
        file_path = folder_path / file_name
        if file_path.is_file():
            file_extension = file_name.split(".")[-1].lower()
            if file_extension in allowed_extensions:
                res.append(file_path)

    return res
