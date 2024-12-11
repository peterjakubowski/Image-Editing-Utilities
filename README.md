# Image-Editing-Utilities

Python helper functions for image editing tasks.

## rescale_width_height

Function for rescaling the width and height of an image to keep aspect ratio.

### Pillow Image Usage

```commandline
from PIL import Image
from image_utils import rescale_width_height

# Open an image with PIL
img = Image.open(img_path)

# Retrieve the image's original dimensions
w, h = img.size

# Rescale the image's dimensions where size is the longest edge
scaled_wh = rescale_width_height(width=w, height=h, size=1000)

# Resize the image with new dimensions
resized_img = img.resize(scaled_wh, Image.Resampling.BICUBIC)

```

### OpenCV Usage

```commandline
import cv2
from image_utils import rescale_width_height

# Open an image with OpenCV
img = cv2.imread(img_path)

# Retrieve the image's original dimensions
h, w, _ = img.shape

# Rescale the image's dimensions where size is the longest edge
scaled_wh = rescale_width_height(width=w, height=h, size=1000)

# Resize the image with new dimensions
resized_img = cv2.resize(img, scaled_wh, cv2.INTER_AREA)

```
