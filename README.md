![Run Python Tests](https://github.com/peterjakubowski/Image-Editing-Utilities/actions/workflows/ci.yaml/badge.svg)
<img src="https://img.shields.io/badge/python-3.10%2B-blue.svg" alt="python" />
<img src="https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg" alt="platform" />

# Image-Editing-Utilities

Python helper functions for image editing tasks.

## list_image_paths

Function to list image paths in a folder filtered by allowed file extensions.

### Basic Usage

By default, `list_image_paths` finds all supported image formats (`jpg`, `jpeg`, `tif`, `tiff`, `png`, `nef`, `cr2`, `dng`).


```python
from pathlib import Path
from image_utils import list_image_paths

# Specify directory
image_directory = Path("path/to/folder/of/images")

# List all supported image paths
image_paths = list_image_paths(image_directory)

print(f"Found {len(image_paths)} images.")

# Iterate and process each image
for img_path in image_paths:
    print(img_path.name)

```
### Filtering by File Extension

You can restrict the search to a single file type or a tuple of specific extensions using the `allowed_extensions` parameter.


#### Single Type

```python
jpg_images = list_image_paths(image_directory, allowed_extensions="jpg")

```

#### Multiple Types

```python
raw_images = list_image_paths(image_directory, allowed_extensions=("cr2", "dng", "nef"))

```

#### Notes

* **Path Input:** Accepts both `pathlib.Path` objects and strings.

* **Default Supported Extensions:** jpg, jpeg, tif, tiff, png, nef, cr2, and dng.

* **Non-recursive:** Only files in the immediate directory are scanned (subdirectories are ignored).

## rescale_width_height

Function for rescaling the width and height of an image to keep aspect ratio.

### Pillow Image Usage

```python
from PIL import Image
from image_utils import rescale_width_height

# Open an image with PIL
img = Image.open("path/to/img.jpg")

# Retrieve the image's original dimensions
w, h = img.size

# Rescale the image's dimensions where size is the longest edge
scaled_wh = rescale_width_height(width=w, height=h, size=1000)

# Resize the image with new dimensions
resized_img = img.resize(scaled_wh, Image.Resampling.BICUBIC)

```

### OpenCV Usage

```python
import cv2
from image_utils import rescale_width_height

# Open an image with OpenCV
img = cv2.imread("path/to/img.jpg")

# Retrieve the image's original dimensions
h, w, _ = img.shape

# Rescale the image's dimensions where size is the longest edge
scaled_wh = rescale_width_height(width=w, height=h, size=1000)

# Resize the image with new dimensions
resized_img = cv2.resize(img, scaled_wh, cv2.INTER_AREA)

```
