import matplotlib.pyplot as plt

class Visualizer:
    @staticmethod
    def visualize_comparisons(original, nlm, wavelet):
        fig, axs = plt.subplots(nrows=len(original), ncols=3, figsize=(15, 5*len(original)))
        for i in range(len(original)):
            axs[i, 0].imshow(original[i], cmap='gray')
            axs[i, 0].set_title('Original')
            axs[i, 1].imshow(nlm[i], cmap='gray')
            axs[i, 1].set_title('NLM')
            axs[i, 2].imshow(wavelet[i], cmap='gray')
            axs[i, 2].set_title('Wavelet')
            for ax in axs[i, :]:
                ax.axis('off')
        plt.show()
