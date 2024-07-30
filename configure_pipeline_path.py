import os
CUSTOM_MODEL_NAME = 'ssd_mobnet_v2_fpnlite' 
PRETRAINED_MODEL_NAME = 'ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8'
paths = {
    'PRETRAINED_MODEL_PATH': os.path.join('Tensorflow', 'workspace','training_demo','pre-trained-models'),
    'MODEL_PATH': os.path.join('Tensorflow', 'workspace','training_demo','models',CUSTOM_MODEL_NAME)
 }
if os.name == 'nt':
    print(f"mkdir {os.path.join(paths['MODEL_PATH'])}")
    print(f"copy {os.path.join(paths['PRETRAINED_MODEL_PATH'], PRETRAINED_MODEL_NAME, 'pipeline.config')} {os.path.join(paths['MODEL_PATH'])}")

# Run ouput of both printing statement in Terminal.