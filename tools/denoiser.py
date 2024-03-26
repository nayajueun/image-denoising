import skimage.restoration as restoration
import pywt
import logging
import cv2

class Denoiser:
    def apply_nlm(self, images, param=1.0):
        logging.info(f'NLM to be applied: parameter = {param}')
        nlm_images = [restoration.denoise_nl_means(img, h=param, fast_mode=True) for img in images]
        logging.info('NLM applied')
        return nlm_images
    
    def apply_wavelet(self, images):
        logging.info('Wavelet Transform to bee applied')
        wavelet_images = []
        for img in images:
            # Apply the forward wavelet transform
            coeffs2 = pywt.dwt2(img, 'bior1.3')
            LL, (LH, HL, HH) = coeffs2
            # Reconstruct the image from the wavelet coefficients
            img_reconstructed = pywt.idwt2(coeffs2, 'bior1.3')
            # Make sure the reconstructed image is the same size as the original
            img_reconstructed = cv2.resize(img_reconstructed, (img.shape[1], img.shape[0]))
            wavelet_images.append(img_reconstructed)
        logging.info('Wavelet Transform applied')
        return wavelet_images
