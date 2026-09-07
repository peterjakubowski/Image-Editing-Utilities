# Python-based image editing utilities
#
# Author: Peter Jakubowski
# Date: 9/6/2026
# Description: Python helper functions for image editing
#

from pathlib import Path
from typing import Literal, get_args

# ========================================
# === Function for listing image paths ===
# ========================================


AllowedExtensions = Literal["jpg", "jpeg", "tif", "tiff", "png", "nef", "cr2", "dng"]

ALL_ALLOWED_EXTENSIONS: tuple[AllowedExtensions, ...] = get_args(AllowedExtensions)


def list_image_paths(
        folder_path: str | Path,
        allowed_extensions: AllowedExtensions | tuple[AllowedExtensions, ...] = ALL_ALLOWED_EXTENSIONS) -> list[Path]:
    """Return paths to all image files in a directory that match allowed extensions.

    :param folder_path: Path to the directory containing images.
    :param allowed_extensions: Allowed file extension or tuple of extensions
                               (without leading dot).
    :return: List of Path objects for matching image files.
    :raises TypeError: If folder_path is not a pathlib.Path object.
    :raises ValueError: If folder_path does not exist or is not a directory.
    """

    if not isinstance(folder_path, Path | str):
        raise TypeError("Folder path must be a pathlib.Path object or string.")

    path = Path(folder_path)

    if not path.exists():
        raise ValueError("Path must be to a folder that already exists.")

    if not path.is_dir():
        raise ValueError("Path must be to a folder.")

    if isinstance(allowed_extensions, str):
        valid_extensions = {allowed_extensions.strip(".").lower()}
    else:
        valid_extensions = {ext.strip(".").lower() for ext in allowed_extensions}

    res = []

    for file_name in path.iterdir():
        file_path = folder_path / file_name
        if file_path.is_file():
            file_extension = file_path.suffix.strip(".").lower()
            if file_extension in valid_extensions:
                res.append(file_path)

    return res
