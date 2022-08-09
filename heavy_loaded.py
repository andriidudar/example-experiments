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

for i in range(50):
    for j in range(1000):
        sleep(0.1)
        experiment.log_metric("metric_" + str(j), i + randrange(10), step=i)
        
    
for i in range(1000):
    sleep(0.1)
    experiment.log_parameter('param' + str(i), 'random_value_' + str(randrange(10)))


experiment.end()