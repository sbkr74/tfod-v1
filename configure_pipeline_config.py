import tensorflow as tf
import os
from object_detection.utils import config_util
from object_detection.protos import pipeline_pb2
from google.protobuf import text_format

CUSTOM_MODEL_NAME = 'ssd_mobilenet_v2_fpnlite' 
PRETRAINED_MODEL_NAME = 'ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8'
TF_RECORD_SCRIPT_NAME = 'generate_tfrecord.py'
LABEL_MAP_NAME = 'label_map.pbtxt'

paths = {
    'ANNOTATION_PATH': os.path.join('TensorFlow', 'workspace','training_demo','annotations'),
    'PRETRAINED_MODEL_PATH': os.path.join('TensorFlow', 'workspace','training_demo','pre-trained-models')
 }
files = {
    'PIPELINE_CONFIG':os.path.join('TensorFlow', 'workspace','training_demo','models', CUSTOM_MODEL_NAME, 'pipeline.config'),
    'LABELMAP': os.path.join(paths['ANNOTATION_PATH'], LABEL_MAP_NAME)
}

config_path = files['PIPELINE_CONFIG']
config = config_util.get_configs_from_pipeline_file(files['PIPELINE_CONFIG'])

# python -c "from object_detection.utils import config_util;config_path=r'TensorFlow\workspace\training_demo\models\ssd_mobnet_v2_fpnlite\pipeline.config';config = config_util.get_configs_from_pipeline_file(config_path);print(config)"

pipeline_config = pipeline_pb2.TrainEvalPipelineConfig()
with tf.io.gfile.GFile(files['PIPELINE_CONFIG'], "r") as f:                                                                                                                                                                                                                     
    proto_str = f.read()                                                                                                                                                                                                                                          
    text_format.Merge(proto_str, pipeline_config)
labels = [{'name':'hi', 'id':1}, {'name':'ok', 'id':2}, {'name':'iloveyou', 'id':3}, {'name':'peace', 'id':4}, {'name':'call', 'id':5}]
pipeline_config.model.ssd.num_classes = len(labels)
pipeline_config.train_config.batch_size = 4
pipeline_config.train_config.fine_tune_checkpoint = os.path.join(paths['PRETRAINED_MODEL_PATH'], PRETRAINED_MODEL_NAME, 'checkpoint', 'ckpt-0')
pipeline_config.train_config.fine_tune_checkpoint_type = "detection"
pipeline_config.train_input_reader.label_map_path= files['LABELMAP']
pipeline_config.train_input_reader.tf_record_input_reader.input_path[:] = [os.path.join(paths['ANNOTATION_PATH'], 'train.record')]
pipeline_config.eval_input_reader[0].label_map_path = files['LABELMAP']
pipeline_config.eval_input_reader[0].tf_record_input_reader.input_path[:] = [os.path.join(paths['ANNOTATION_PATH'], 'test.record')]

print("End of script")