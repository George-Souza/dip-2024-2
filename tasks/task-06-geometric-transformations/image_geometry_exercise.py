# image_geometry_exercise.py
# STUDENT'S EXERCISE FILE

"""
Exercise:
Implement a function `apply_geometric_transformations(img)` that receives a grayscale image
represented as a NumPy array (2D array) and returns a dictionary with the following transformations:

1. Translated image (shift right and down)
2. Rotated image (90 degrees clockwise)
3. Horizontally stretched image (scale width by 1.5)
4. Horizontally mirrored image (flip along vertical axis)
5. Barrel distorted image (simple distortion using a radial function)

You must use only NumPy to implement these transformations. Do NOT use OpenCV, PIL, skimage or similar libraries.

Function signature:
    def apply_geometric_transformations(img: np.ndarray) -> dict:

The return value should be like:
{
    "translated": np.ndarray,
    "rotated": np.ndarray,
    "stretched": np.ndarray,
    "mirrored": np.ndarray,
    "distorted": np.ndarray
}
"""

import numpy as np

def translate_image(img, tx=10, ty=10):
    H, W = img.shape
    translated = np.zeros_like(img)
    translated[ty:, tx:] = img[:H - ty, :W - tx]
    return translated

def rotate_image(img):
    return np.rot90(img, k=-1)

def stretch_image(img, scale_x=1.5):
    H, W = img.shape
    new_W = int(W * scale_x)
    stretched = np.zeros((H, new_W))

    for i in range(new_W):
        src_x = int(i / scale_x)
        if src_x >= W:
            src_x = W - 1
        stretched[:, i] = img[:, src_x]
    return stretched

def mirror_image(img):
    return img[:, ::-1]

def barrel_distort_image(img):
    H, W = img.shape
    center_x = W / 2
    center_y = H / 2
    distorted = np.zeros_like(img)

    k = 0.0005

    for y in range(H):
        for x in range(W):
            dx = (x - center_x)
            dy = (y - center_y)
            r = np.sqrt(dx ** 2 + dy ** 2)
            factor = 1 + k * (r ** 2)

            src_x = int(center_x + dx * factor)
            src_y = int(center_y + dy * factor)

            if 0 <= src_x < W and 0 <= src_y < H:
                distorted[y, x] = img[src_y, src_x]
    
    return distorted

def apply_geometric_transformations(img: np.ndarray) -> dict:
    return {
        "translated": translate_image(img),
        "rotated": rotate_image(img),
        "stretched": stretch_image(img),
        "mirrored": mirror_image(img),
        "distorted": barrel_distort_image(img)
    }
