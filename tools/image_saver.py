import numpy as np
import os
import cv2

class ImageSaver:
    def __init__(self, save_dir):
        self.save_dir = save_dir
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

    def save_images(self, images, image_names, prefix):
        for i, img in enumerate(images):
            img_name = f"{prefix}_{image_names[i]}"
            cv2.imwrite(os.path.join(self.save_dir, img_name), np.uint8(img * 255))
