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

steps = 10
params = 10
metrics = 10

experiment.set_model_graph('0-> 2-> 3-> 4', overwrite=False)


for i in range(steps):
    experiment.log_image('./images/image_' + str(randrange(8)) + '.png', step=i)
    experiment.log_image('./images/image_' + str(randrange(8)) + '.png', step=i)
    experiment.log_image('./images/image_' + str(randrange(8)) + '.png', step=i)
    experiment.log_image('./images/image_' + str(randrange(8)) + '.png', step=i)
    experiment.log_image('./images/image_' + str(randrange(8)) + '.png', step=i)


experiment.log_audio('./audio/zero/0ab3b47d_nohash_0.wav', file_name='zero')
experiment.log_audio('./audio/one/0a7c2a8d_nohash_0.wav', file_name='one')
experiment.log_audio('./audio/two/0a7c2a8d_nohash_0.wav', file_name='two')
experiment.log_audio('./audio/three/0a9f9af7_nohash_0.wav', file_name='three')
experiment.log_audio('./audio/four/0a9f9af7_nohash_0.wav', file_name='four')
experiment.log_audio('./audio/five/0a9f9af7_nohash_0.wav', file_name='five')
experiment.log_audio('./audio/six/0a7c2a8d_nohash_0.wav', file_name='six')
experiment.log_audio('./audio/seven/0a0b46ae_nohash_0.wav', file_name='seven')
experiment.log_audio('./audio/eight/0a9f9af7_nohash_0.wav', file_name='eight')
experiment.log_audio('./audio/nine/0a7c2a8d_nohash_0.wav', file_name='nine')


for i in range(steps):
    for j in range(metrics):
        sleep(0.005)
        experiment.log_metric("metric_" + str(j), min(max(i + randrange(20), 0), 100), step=i)

for i in range(params):
    sleep(0.005)
    experiment.log_parameter('param_' + str(i), 'random_value_' + str(randrange(10)))



experiment.end()