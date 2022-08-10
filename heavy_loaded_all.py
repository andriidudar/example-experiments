from time import sleep
from random import randrange, random

import numpy as numpy
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

# -------------------- confusion matrix
desired_output = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
 ]

actual_output = [
    [0.1, 0.5, 0.4],
    [0.2, 0.2, 0.3],
    [0.7, 0.4, 0.5],
    [0.3, 0.8, 0.3],
    [0.0, 0.5, 0.3],
    [0.1, 0.5, 0.5],
 ]

experiment.log_confusion_matrix(desired_output, actual_output)

# -------------------- graph definition
experiment.set_model_graph('0 -> ' + str(randrange(3)) + ' -> ' + str(randrange(5)) + ' -> 6')

# -------------------- HTML
experiment.log_html('<a href="www.comet.ml"> I love Comet.ml </a>')

# -------------------- 3D Histogram
for i in range(steps):
    experiment.log_histogram_3d(numpy.array([randrange(5), randrange(5), randrange(5)]), step=i)

# -------------------- graphics
for i in range(steps):
    experiment.log_image('./images/image_' + str(randrange(7) + 1) + '.png', step=i)
    experiment.log_image('./images/image_' + str(randrange(7) + 1) + '.png', step=i)
    experiment.log_image('./images/image_' + str(randrange(7) + 1) + '.png', step=i)
    experiment.log_image('./images/image_' + str(randrange(7) + 1) + '.png', step=i)
    experiment.log_image('./images/image_' + str(randrange(7) + 1) + '.png', step=i)

# -------------------- audio
experiment.log_audio('./audios/zero/0ab3b47d_nohash_0.wav', file_name='zero')
experiment.log_audio('./audios/one/0a7c2a8d_nohash_0.wav', file_name='one')
experiment.log_audio('./audios/two/0a7c2a8d_nohash_0.wav', file_name='two')
experiment.log_audio('./audios/three/0a9f9af7_nohash_0.wav', file_name='three')
experiment.log_audio('./audios/four/0a9f9af7_nohash_0.wav', file_name='four')
experiment.log_audio('./audios/five/0a9f9af7_nohash_0.wav', file_name='five')
experiment.log_audio('./audios/six/0a7c2a8d_nohash_0.wav', file_name='six')
experiment.log_audio('./audios/seven/0a0b46ae_nohash_0.wav', file_name='seven')
experiment.log_audio('./audios/eight/0a9f9af7_nohash_0.wav', file_name='eight')
experiment.log_audio('./audios/nine/0a7c2a8d_nohash_0.wav', file_name='nine')

# -------------------- text
for i in range(steps):
    experiment.log_text('random text' + str(random()), step=i)

# -------------------- metrix
for i in range(steps):
    for j in range(metrics):
        sleep(0.005)
        experiment.log_metric("metric_" + str(j), min(max(i + randrange(20), 0), 100), step=i)

# -------------------- params

for i in range(params):
    sleep(0.005)
    experiment.log_parameter('param_' + str(i), 'random_value_' + str(randrange(10)))



experiment.end()