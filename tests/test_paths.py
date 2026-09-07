import os
from pathlib import Path
from typing import cast

import pytest
from PIL import Image

from src.image_utils.paths import AllowedExtensions, list_image_paths


class TestListImagePaths:
    def test_list_image_paths_returns_empty_list_when_folder_empty(self, tmp_path):
        result = list_image_paths(tmp_path)
        assert result == []

    def test_list_image_paths_returns_empty_list_when_folder_path_is_string(self, tmp_path):
        assert isinstance(tmp_path, Path)
        path_str = str(tmp_path)
        assert isinstance(path_str, str)
        result = list_image_paths(path_str)
        assert result == []

    @pytest.mark.parametrize("input_value", [123, True, [], (), 1.0, None])
    def test_list_image_paths_raises_type_error_when_input_is_not_path_or_string(self, input_value):
        with pytest.raises(TypeError, match="Folder path must be a pathlib.Path object or string."):
            list_image_paths(input_value)

    @pytest.mark.parametrize("input_value", ["test", ".test", "/test"])
    def test_list_image_paths_raises_value_error_when_directory_path_does_not_exist(self, tmp_path, input_value):
        with pytest.raises(ValueError, match="Path must be to a folder that already exists."):
            list_image_paths(tmp_path / input_value)

    def test_list_image_paths_raises_value_error_when_path_is_not_directory(self, tmp_path):
        temp_file_path = tmp_path / "temp_file.txt"
        with open(temp_file_path, "w") as file:
            file.write("Test text")

        with pytest.raises(ValueError, match="Path must be to a folder."):
            list_image_paths(tmp_path / "temp_file.txt")

    def test_list_image_paths_returns_list_of_paths(self, tmp_path):
        test_image_path = tmp_path / "temp_image.jpg"
        test_image = Image.new(mode="RGB", size=(10, 10), color=0)
        test_image.save(test_image_path)
        result = list_image_paths(tmp_path)
        assert isinstance(result, list)
        assert isinstance(result[0], Path)

    @pytest.mark.parametrize("extension", ["jpg", "jpeg", "JPG", "JPEG"])
    def test_list_image_paths_returns_list_of_jpgs(self, tmp_path, extension):
        test_image_path = tmp_path / f"temp_image.{extension}"
        test_image = Image.new(mode="RGB", size=(10, 10), color=0)
        test_image.save(test_image_path)
        result = list_image_paths(tmp_path)
        assert len(result) == 1

    @pytest.mark.parametrize("extension", ["tif", "tiff", "TIF", "TIFF"])
    def test_list_image_paths_returns_list_of_tiffs(self, tmp_path, extension):
        test_image_path = tmp_path / f"temp_image.{extension}"
        test_image = Image.new(mode="RGB", size=(10, 10), color=0)
        test_image.save(test_image_path)
        result = list_image_paths(tmp_path)
        assert len(result) == 1

    @pytest.mark.parametrize("extension", ["png", "PNG"])
    def test_list_image_paths_returns_list_of_pngs(self, tmp_path, extension):
        test_image_path = tmp_path / f"temp_image.{extension}"
        test_image = Image.new(mode="RGB", size=(10, 10), color=0)
        test_image.save(test_image_path)
        result = list_image_paths(tmp_path)
        assert len(result) == 1

    @pytest.mark.parametrize("extension", ["nef", "NEF"])
    def test_list_image_paths_returns_list_of_nef_raw(self, tmp_path, extension):
        test_image_path = tmp_path / f"temp_image.{extension}"
        test_image = Image.new(mode="RGB", size=(10, 10), color=0)
        test_image.save(test_image_path, format="tiff")
        result = list_image_paths(tmp_path)
        assert len(result) == 1

    @pytest.mark.parametrize("extension", ["cr2", "CR2"])
    def test_list_image_paths_returns_list_of_cr2_raw(self, tmp_path, extension):
        test_image_path = tmp_path / f"temp_image.{extension}"
        test_image = Image.new(mode="RGB", size=(10, 10), color=0)
        test_image.save(test_image_path, format="tiff")
        result = list_image_paths(tmp_path)
        assert len(result) == 1

    @pytest.mark.parametrize("extension", ["dng", "DNG"])
    def test_list_image_paths_returns_list_of_dng_raw(self, tmp_path, extension):
        test_image_path = tmp_path / f"temp_image.{extension}"
        test_image = Image.new(mode="RGB", size=(10, 10), color=0)
        test_image.save(test_image_path, format="tiff")
        result = list_image_paths(tmp_path)
        assert len(result) == 1

    @pytest.mark.parametrize("extension", ["txt", "doc", "docx", "xls", "py", "xmp"])
    def test_list_image_paths_ignores_text_files(self, tmp_path, extension):
        temp_file_path = tmp_path / f"temp_text.{extension}"
        with open(temp_file_path, "w") as file:
            file.write("Test text")
        result = list_image_paths(tmp_path)
        assert len(result) == 0

    @pytest.mark.parametrize(
        "subfolder_name",
        ["test_subfolder", ".test_subfolder", "jpg", ".jpg", ".DS_Store"],
    )
    def test_list_image_paths_ignores_subfolders(self, tmp_path, subfolder_name):
        subfolder_path = tmp_path / subfolder_name
        os.mkdir(subfolder_path)
        test_image_path = subfolder_path / "test_image.jpg"
        test_image = Image.new(mode="RGB", size=(10, 10), color=0)
        test_image.save(test_image_path)
        result = list_image_paths(tmp_path)
        assert len(result) == 0

    @pytest.mark.parametrize("file_extension", ["j", "p", "g"])
    def test_list_image_path_ignores_single_character_files(self, tmp_path, file_extension):
        test_image_path = tmp_path / f"test_image.{file_extension}"
        test_image = Image.new(mode="RGB", size=(10, 10), color=0)
        test_image.save(test_image_path, format="tiff")
        result = list_image_paths(tmp_path)
        assert len(result) == 0

    @pytest.mark.parametrize("allowed_extension", ["jpg", "JPG", ".jpg", ".JPG"])
    def test_list_image_paths_returns_jpg_only(self, tmp_path, allowed_extension):
        for file_type in ["jpg", "png", "tiff"]:
            temp_image_path = tmp_path / f"temp_image.{file_type}"
            temp_image = Image.new(mode="RGB", size=(10, 10), color=0)
            temp_image.save(temp_image_path)
        result = list_image_paths(tmp_path, allowed_extensions=allowed_extension)
        assert len(result) == 1
        assert str(result[0]).endswith("jpg")

    @pytest.mark.parametrize("allowed_extension", ["png", "PNG", ".png", ".PNG"])
    def test_list_image_paths_returns_png_only(self, tmp_path, allowed_extension):
        for file_type in ["jpg", "png", "tiff"]:
            temp_image_path = tmp_path / f"temp_image.{file_type}"
            temp_image = Image.new(mode="RGB", size=(10, 10), color=0)
            temp_image.save(temp_image_path)
        result = list_image_paths(tmp_path, allowed_extensions=allowed_extension)
        assert len(result) == 1
        assert str(result[0]).endswith("png")

    @pytest.mark.parametrize("allowed_extension", ["tiff", "TIFF", ".tiff", ".TIFF"])
    def test_list_image_paths_returns_tiff_only(self, tmp_path, allowed_extension):
        for file_type in ["jpg", "png", "tiff"]:
            temp_image_path = tmp_path / f"temp_image.{file_type}"
            temp_image = Image.new(mode="RGB", size=(10, 10), color=0)
            temp_image.save(temp_image_path)
        result = list_image_paths(tmp_path, allowed_extensions=allowed_extension)
        assert len(result) == 1
        assert str(result[0]).endswith("tiff")

    def test_list_image_paths_returns_raw_only(self, tmp_path):
        for file_type in ["jpg", "png", "tiff", "nef", "cr2", "dng"]:
            temp_image_path = tmp_path / f"temp_image.{file_type}"
            temp_image = Image.new(mode="RGB", size=(10, 10), color=0)
            temp_image.save(temp_image_path, format="tiff")
        allowed_extensions = cast(tuple[AllowedExtensions, ...], ("nef", "cr2", "dng"))
        result = list_image_paths(tmp_path, allowed_extensions=allowed_extensions)
        assert len(result) == 3
