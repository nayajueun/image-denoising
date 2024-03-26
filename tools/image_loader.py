import os
import cv2
import logging

class ImageLoader:
    def __init__(self, image_dir):
        self.image_dir = image_dir
    
    def load_images(self):
        images = []
        for filename in os.listdir(self.image_dir):
            if filename.endswith(".jpeg"):
                img = cv2.imread(os.path.join(self.image_dir, filename), cv2.IMREAD_GRAYSCALE)
                images.append(img)
                logging.info(f'Image {filename} loaded')
        
        logging.info(f"{len(images)} images loaded from {self.image_dir}")
        print("load")
        return images