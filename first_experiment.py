from time import sleep
import math
from comet_ml import Experiment
import os
os.environ["COMET_URL_OVERRIDE"] = "https://staging.comet.ml/clientlib/"
experiment = Experiment(
    api_key="hLkHHYMaD3qQtDT1upEGro0EV",
    project_name="general",
    workspace="andriidudar",
)

for i in range(20):
    experiment.log_metric("metric_test", i, step=i)
    sleep(1)
    experiment.log_metric("metricA", i, step=i)
    experiment.log_metric("metricB", 1/(i+1), step=i)
    experiment.log_metric("metricC", math.sin(i / 100.), step=i)

test_info = {"test_name": "Mara", "test_email": "xxxx"}
experiment.log_parameter('test_name', test_info["test_name"])
experiment.end()