from PIL import Image, ImageOps
import numpy as np

def apply_filter(image: Image.Image, filter_name: str) -> Image.Image:
    if filter_name == "Averaging":
        kernel = np.array([
            [1/9, 1/9, 1/9],
            [1/9, 1/9, 1/9],
            [1/9, 1/9, 1/9]
        ])
        return convolution(image, kernel)
    
    elif filter_name == "Custom Filter 1":
        pass
        
    elif filter_name == "Custom Filter 2":
        pass
        
    return image

def convolution(image: Image.Image, kernel: np.ndarray) -> Image.Image:
    img_array = np.array(image, dtype=np.float32)
    image_height, image_width, image_channels = img_array.shape
    kernel_height, kernel_width = kernel.shape

    output_img_array = np.zeros_like(img_array)
    for i in range(image_height):
        for j in range(image_width):

            sum = np.zeros(image_channels, dtype=np.float32)

            for n in range(kernel_height):
                for m in range(kernel_width):

                    weight = kernel[n,m]
                    pixel_value = img_array[i + n, j + m, :]
                    sum += pixel_value*weight

            output_img_array[i, j, :]= sum

    output_img_array = np.clip(output_img_array, 0, 255).astype(np.uint8)
    return Image.fromarray(output_img_array)