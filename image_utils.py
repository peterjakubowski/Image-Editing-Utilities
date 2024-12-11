# Python-based image editing utilities
#
# Author: Peter Jakubowski
# Date: 12/11/2024
# Description: Python helper functions for image editing
#

# =====================================
# === Functions for resizing images ===
# =====================================

def rescale_width_height(width: int, height: int, size: int) -> tuple[int, ...]:
    """
    Function for rescaling the width and height
    of an image to keep aspect ratio.
    :param width: original image width
    :param height: original image height
    :param size: desired length of the longest edge in pixels.
    :return: width (w) and height (h) of resized image.
    """

    # check if the image is vertical,
    # height is the longest edge
    if height > width:
        # set height to size
        h = size
        # determine the ratio for resizing
        ratio = height / size
        # calculate new width by dividing by ratio
        w = int(width / ratio)
    # check if the image is horizontal,
    # width is the longest edge
    elif height < width:
        # set width to size
        w = size
        # determine the ratio for resizing
        ratio = width / size
        # calculate new height by dividing by ratio
        h = int(height / ratio)
    # if image is not vertical or horizontal,
    # image must be square
    else:
        # set width and height to size
        w = h = size
    # return the new width and height
    return tuple([w, h])
