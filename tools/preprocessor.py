import cv2
import logging
import numpy as np

class Preprocessor:
    def __init__(self, histogram_eq=True):
        self.histogram_eq = histogram_eq
    
    def preprocess_images(self, images):
        processed_images = []
        for img in images:
            img_normalized = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
            if self.histogram_eq:
                img = cv2.equalizeHist(np.uint8(img_normalized*255))
                logging.info('Histogram Equalization applied')
            processed_images.append(img)
        return processed_images
