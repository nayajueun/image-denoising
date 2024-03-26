
from tools.experiment import Experiment
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s',
    handlers=[
        logging.FileHandler("debug.log"),  # Log to a file
        logging.StreamHandler()            # Log to the console
    ]
)

# Setup logging and run the experiment as previously shown.
image_dir_normal = 'images/chest_xray/val/NORMAL'
image_dir_pneumonia = 'images/chest_xray/val/PNEUMONIA'  
save_dir = 'output/chest_xray'

if __name__ == '__main__':
    experiment = Experiment(image_dir_normal, image_dir_pneumonia, save_dir)
    experiment.run()