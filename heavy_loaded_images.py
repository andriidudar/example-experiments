from time import sleep
from random import randrange
import math
from comet_ml import Experiment
import os
os.environ["COMET_URL_OVERRIDE"] = "https://staging.comet.ml/clientlib/"
experiment = Experiment(
    api_key="hLkHHYMaD3qQtDT1upEGro0EV",
    project_name="heavy-loaded",
    workspace="andriidudar",
)

experiment.set_model_graph('0-> 2-> 3-> 4', overwrite=False)
experiment.log_image('./images/image_1.png')
experiment.log_image('./images/image_2.png')
experiment.log_image('./images/image_3.png')
experiment.log_image('./images/image_4.png')

for i in range(50):
    for j in range(10):
        sleep(0.005)
        experiment.log_metric("metric_" + str(j), min(max(i + randrange(20), 0), 100), step=i)

for i in range(10):
    sleep(0.005)
    experiment.log_parameter('param_' + str(i), 'random_value_' + str(randrange(10)))



experiment.end()