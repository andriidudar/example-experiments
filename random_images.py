from time import sleep
from random import randrange, getrandbits

from comet_ml import Experiment
import os

os.environ["COMET_URL_OVERRIDE"] = "https://staging.comet.ml/clientlib/"
experiment = Experiment(
    api_key="hLkHHYMaD3qQtDT1upEGro0EV",
    project_name="heavy-loaded",
    workspace="andriidudar",
)

steps = 30

for i in range(steps):
    sleep(5)
    # -------------------- graphics
    if bool(getrandbits(1)):
        print('log nothing')
    elif bool(getrandbits(1)):
        experiment.log_image('./images/image_1.jpg', step=i)
        experiment.log_image('./images/image_2.jpg', step=i)
        experiment.log_image('./images/image_3.jpg', step=i)
    elif bool(getrandbits(1)):
        experiment.log_image('./images_random_name_1/image_1.jpg', step=i)
        experiment.log_image('./images_random_name_1/image_2.jpg', step=i)
        experiment.log_image('./images_random_name_1/image_3.jpg', step=i)
    elif bool(getrandbits(1)):
        experiment.log_image('./images_random_name_2/image_1.jpg', step=i)
        experiment.log_image('./images_random_name_2/image_2.jpg', step=i)
        experiment.log_image('./images_random_name_2/image_3.jpg', step=i)
    else:
        experiment.log_image('./images_random_name_2/image_' + str(randrange(3) + 1) + '.jpg', step=i)

experiment.end()