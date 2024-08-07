import os
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder
from object_detection.utils import config_util
import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
# Set paths
CUSTOM_MODEL_NAME = 'ssd_mobilenet_v2_fpnlite'
LABEL_MAP_NAME = 'label_map.pbtxt'
paths = {
    'ANNOTATION_PATH': os.path.join('TensorFlow', 'workspace', 'training_demo', 'annotations'),
    'IMAGE_PATH': os.path.join('TensorFlow', 'workspace', 'training_demo', 'images'),
    'CHECKPOINT_PATH': os.path.join('TensorFlow', 'workspace', 'training_demo', 'models', CUSTOM_MODEL_NAME)
}
files = {
    'PIPELINE_CONFIG': os.path.join('TensorFlow', 'workspace', 'training_demo', 'models', CUSTOM_MODEL_NAME, 'pipeline.config'),
    'LABELMAP': os.path.join(paths['ANNOTATION_PATH'], LABEL_MAP_NAME)
}

# Load pipeline config and build a detection model
configs = config_util.get_configs_from_pipeline_file(files['PIPELINE_CONFIG'])
detection_model = model_builder.build(model_config=configs['model'], is_training=False)

# Restore checkpoint
ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore(os.path.join(paths['CHECKPOINT_PATH'], 'ckpt-3')).expect_partial()

@tf.function
def detect_fn(image):
    image, shapes = detection_model.preprocess(image)
    prediction_dict = detection_model.predict(image, shapes)
    detections = detection_model.postprocess(prediction_dict, shapes)
    return detections

# Load and prepare the image
IMAGE_PATH = os.path.join(paths['IMAGE_PATH'], 'test', 'ok.48ed9abe-4cf8-11ef-b436-0c7a15ea0c76.jpg')
img = cv2.imread(IMAGE_PATH)
image_np = np.array(img)

# Perform detection
input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
detections = detect_fn(input_tensor)

# Process the detections
num_detections = int(detections.pop('num_detections'))
detections = {key: value[0, :num_detections].numpy() for key, value in detections.items()}
detections['num_detections'] = num_detections
detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

label_id_offset = 1
image_np_with_detections = image_np.copy()

# Visualize the detection results
viz_utils.visualize_boxes_and_labels_on_image_array(
    image_np_with_detections,
    detections['detection_boxes'],
    detections['detection_classes'] + label_id_offset,
    detections['detection_scores'],
    label_map_util.create_category_index_from_labelmap(files['LABELMAP']),
    use_normalized_coordinates=True,
    max_boxes_to_draw=3,
    min_score_thresh=.8,
    agnostic_mode=False
)

# Display the image with detections
# plt.figure(figsize=(12, 8))
plt.imshow(cv2.cvtColor(image_np_with_detections, cv2.COLOR_BGR2RGB))
plt.show()
