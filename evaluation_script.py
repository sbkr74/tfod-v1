import os

CUSTOM_MODEL_NAME = 'ssd_mobilenet_v2_fpnlite'
paths = {
    'APIMODEL_PATH': os.path.join('Tensorflow','models'),
    'CHECKPOINT_PATH': os.path.join('Tensorflow', 'workspace','training_demo','models',CUSTOM_MODEL_NAME)
}
files = {
    'PIPELINE_CONFIG':os.path.join('TensorFlow', 'workspace','training_demo','models', CUSTOM_MODEL_NAME, 'pipeline.config')
}

TRAINING_SCRIPT = os.path.join(paths['APIMODEL_PATH'], 'research', 'object_detection', 'model_main_tf2.py')
command = "python {} --model_dir={} --pipeline_config_path={} --checkpoint_dir={}".format(TRAINING_SCRIPT, paths['CHECKPOINT_PATH'],files['PIPELINE_CONFIG'], paths['CHECKPOINT_PATH'])

print(command)