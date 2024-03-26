from tools.image_loader import ImageLoader
from tools.preprocessor import Preprocessor
from tools.denoiser import Denoiser
from tools.evaluator import Evaluator
from tools.visualizer import Visualizer
from tools.image_saver import ImageSaver
import random
import logging
import os
import cv2
import pandas as pd
import numpy as np

class Experiment:
    def __init__(self, image_dir_normal, image_dir_pneumonia, save_dir):
        self.loader_normal = ImageLoader(image_dir_normal)
        self.loader_pneumonia = ImageLoader(image_dir_pneumonia)
        self.preprocessor = Preprocessor()
        self.denoiser = Denoiser()
        self.evaluator = Evaluator()
        self.visualizer = Visualizer()
        self.saver = ImageSaver(save_dir)
        self.image_dir_normal = image_dir_normal
        self.image_dir_pneumonia = image_dir_pneumonia
        
    def run(self):
        # Load images
        original_images_normal = self.loader_normal.load_images()
        original_images_pneumonia = self.loader_pneumonia.load_images()
        original_images = original_images_normal + original_images_pneumonia
        
        # Preprocess images
        preprocessed_images = self.preprocessor.preprocess_images(original_images)
        
        # Apply denoising techniques
        nlm_images = self.denoiser.apply_nlm(preprocessed_images)
        wavelet_images = self.denoiser.apply_wavelet(preprocessed_images)
        
        # Evaluate and visualize
        psnr_nlm = self.evaluator.evaluate_images(original_images, nlm_images)
        psnr_wavelet = self.evaluator.evaluate_images(original_images, wavelet_images)
        # self.visualizer.visualize_comparisons(original_images, nlm_images, wavelet_images)
        
        print("done")

        # Save results
        image_normal_names = [name for name in os.listdir(self.image_dir_normal) if name.endswith('.jpeg')]
        image_pneumonia_names = [name for name in os.listdir(self.image_dir_pneumonia) if name.endswith('.jpeg')]
        image_names = image_normal_names + image_pneumonia_names

        print(image_names)
        results_df = pd.DataFrame({
        'Image': image_names,
        'PSNR_NLM': psnr_nlm,
        'PSNR_Wavelet': psnr_wavelet
        })


        results_df.to_csv('experiment_results.csv', index=False)

        # Save processed images
        save_dir = 'path_to_save_processed_images'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)


        for i, img in enumerate(nlm_images):
            img_name = f"NLM_{image_names[i]}"
            cv2.imwrite(os.path.join(save_dir, img_name), np.uint8(img * 255))

        for i, img in enumerate(wavelet_images):
            img_name = f"Wavelet_{image_names[i]}"
            cv2.imwrite(os.path.join(save_dir, img_name), np.uint8(img * 255))

        print("Processed images saved.")


        print("Results saved to experiment_results.csv")