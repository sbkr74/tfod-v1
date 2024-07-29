import os
PRETRAINED_MODEL_URL = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz'
PRETRAINED_MODEL_PATH = os.path.join('TensorFlow','workspace','training_demo','pre-trained-models')
PRETRAINED_MODEL_NAME = "ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8"

print(f"cd {PRETRAINED_MODEL_PATH}")
print(f"wget.download({PRETRAINED_MODEL_URL})")
print(f"cd {PRETRAINED_MODEL_PATH} && tar -zxvf {PRETRAINED_MODEL_NAME+'.tar.gz'}")

# In Terminal 
'''
python -c "import wget;wget.download('http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz')"
'''