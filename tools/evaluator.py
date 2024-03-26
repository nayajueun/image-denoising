import skimage.metrics as metrics
import logging

class Evaluator:
    @staticmethod
    def evaluate_images(original, processed):
        psnr_values = [metrics.peak_signal_noise_ratio(orig, proc) for orig, proc in zip(original, processed)]
        logging.info('PSNR calculated for images')
        return psnr_values