# Training Custom Object Detector
## Using following Link To Tutor (Model Training)
https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html

### Here are few steps we consider To train own object detector

1. Organise workspace 
2. Prepare Annotate Dataset
3. Generate `tf_records` from such datasets
4. Configure simple training pipeline
5. Train the model
6. Export resulting model

## 1. Preparing Workspace
#### Follow below structure 
```
TensorFlow/
    |-----addons/
            |----labelImg/
    |-----models/
            |----community/
            |----docs/
            |----Official/
            |----research/
            |---- ...
    |-----workspace/
            |----training_demo/
``` 
`CMD`
```sh
# From within TensorFlow/
mkdir addons\labelImg

mkdir workspace\training_demo
```
The `training_demo` directory will contain all files related to model training.
It is advisable to create a separate training folder each time we wish to train on a different dataset.

```
training_demo/
    |-----annotations/
    |-----exported-models/
    |-----images/
        |----test/
        |----train/
    |-----models/
    |-----pre-trained-models/
``` 
```sh
# from within TensorFlow/Workspace/training_demo/

mkdir annotations exported-models "images/test" "images/train" models pre-trained-models
```

## 2. Preparing Dataset

### 2.1. Install labelImg for Annotations  
<b>Using pip installation</b>
```sh
pip install labelImg
```

#### Using Source code
To download the package you can either use Git to clone the <a href = "https://github.com/HumanSignal/labelImg">labelImg repo</a> inside the TensorFlow\addons folder, or you can simply download it as a <a href="https://github.com/tzutalin/labelImg/archive/master.zip">ZIP</a> and extract it’s contents inside the TensorFlow\addons folder. To keep things consistent, in the latter case you will have to rename the extracted folder `labelImg-master` to `labelImg`.   

<b>for windows</b>
```
TensorFlow/
    |-----addons/
            |----labelImg/
    |-----models/
            |----community/
            |----docs/
            |---- ...
    |-----workspace/
            |----training_demo/
```
```sh
# from within TensorFlow/addons/labelImg
pyrcc4 -o libs/resources.py resources.qrc
For pyqt5, pyrcc5 -o libs/resources.py resources.qrc

python labelImg.py
python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

<b>Windows + Anoconda</b>
```sh
# from within TensorFlow/addons/labelImg
conda install pyqt=5
conda install -c anaconda lxml
pyrcc5 -o libs/resources.py resources.qrc
python labelImg.py
python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

### 2.2. Annotate Images
Annotate Images
Once you have collected all the images to be used to test your model (ideally more than 100 per class), place them inside the folder training_demo/images.

Open a new Terminal window.

Next go ahead and start labelImg, pointing it to your training_demo/images folder.

If you installed labelImg Using PIP (Recommended):
```
labelImg <PATH_TO_TF>/TensorFlow/workspace/training_demo/images
```
Othewise, 
```cmd
cd into Tensorflow/addons/labelImg and run:
```
```sh 
# From within Tensorflow/addons/labelImg
python labelImg.py ../../workspace/training_demo/images
```
A File Explorer Dialog windows should open, which points to the training_demo/images folder.

Press the “Select Folder” button, to start annotating your images.

Once open, you should see a window similar to the one below:

<img src="..\repo_files\labelImg.jpg">

once you annotate all your images, a set of new *.xml files, one for each image, should be generated inside your training_demo/images folder.

### 2.3. Partition Dataset
<p>Once you have finished annotating your image dataset, it is a general convention to use only part of it for training, and the rest is used for evaluation purposes.
</p>

Typically, the ratio is` 9:1, i.e. 90%` of the images are used for training and the rest `10%` is maintained for testing, but you can chose whatever ratio suits your needs.

Once you have decided how you will be splitting your dataset, copy all training images, together with their corresponding `*.xml` files, and place them inside the `training_demo/images/train` folder. Similarly, copy all testing images, with their `*.xml` files, and paste them inside `training_demo/images/test`.

### 2.4. Create a Label Map
TensorFlow requires a label map, which namely maps each of the used labels to an integer values. This label map is used both by the training and detection processes.

Below is example of label map so you can distinguish.
```
item {
    id: 1
    name: 'hi'
}

item {
    id: 2
    name: 'call'
}
...
```

Label map files have the extention .pbtxt and should be placed inside the `training_demo/annotations` folder.

`Code for Label Mapping`  
- refer to <a href="https://github.com/sbkr74/tfod-v1/blob/main/label_map_script.py">Label mapping</a> scripts.

## 3. Create TensorFlow Records
Now that we have generated our annotations and split our dataset into the desired training and testing subsets, it is time to convert our annotations into the so called `TFRecord` format.

### Convert *.xml to *.record

To do this we can use a <a href="https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/_downloads/da4babe668a8afb093cc7776d7e630f3/generate_tfrecord.py">script</a> that iterates through all *.xml files in the `training_demo/images/train` and `training_demo/images/test` folders, and generates a `*.record` file for each of the two. 

```
TensorFlow/
├─ addons/ (Optional)
│  └─ labelImg/
├─ models/
│  ├─ community/
│  ├─ official/
│  ├─ orbit/
│  ├─ research/
│  └─ ...
├─ scripts/
│  └─ preprocessing/
└─ workspace/
   └─ training_demo/
```
Downloaded <a href="https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/_downloads/da4babe668a8afb093cc7776d7e630f3/generate_tfrecord.py">Script</a> should be save inside `TensorFlow/scripts/preprocessing`

**Install the pandas package:**
```sh
conda install pandas # Anaconda
                     # or
pip install pandas   # pip
```
**Finally, cd into `TensorFlow/scripts/preprocessing` and run:**

```sh
# Create train data:
python generate_tfrecord.py -x [PATH_TO_IMAGES_FOLDER]/train -l [PATH_TO_ANNOTATIONS_FOLDER]/label_map.pbtxt -o [PATH_TO_ANNOTATIONS_FOLDER]/train.record

# Create test data:
python generate_tfrecord.py -x [PATH_TO_IMAGES_FOLDER]/test -l [PATH_TO_ANNOTATIONS_FOLDER]/label_map.pbtxt -o [PATH_TO_ANNOTATIONS_FOLDER]/test.record
```

`For Reference`  
- refer to <a href="[tf_record_generation.py](https://github.com/sbkr74/tfod-v1/blob/main/tf_record_generation.py)">tf_records</a> script.


## 4. Download and configure Pre-trained Model
### 4.1. Download and extract
To begin with, we need to download the latest pre-trained network for the model we wish to use. This can be done by simply clicking on the name of the desired model in the table found in <a href ="https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md">TensorFlow 2 Detection Model Zoo</a>. Clicking on the name of your model should initiate a download for a `*.tar.gz` file.

Once the `*.tar.gz` file has been downloaded, open it using a decompression program of your choice `(e.g. 7zip, WinZIP, etc.)`. Next, open the `*.tar` folder that you see when the compressed folder is opened, and extract its contents inside the folder `training_demo/pre-trained-models`. Since we downloaded the `SSD Mobilenet v2 fpnlite 320x320 model`, our training_demo directory should now look as follows:

```
training_demo/
├─ ...
├─ pre-trained-models/
│  └─ ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/
│     ├─ checkpoint/
│     ├─ saved_model/
│     └─ pipeline.config
└─ ...
```
<b>Refer to <a href="https://github.com/sbkr74/tfod-v1/blob/main/pre-trained-model.py">code</a> for downloading and unzipping</b>

### 4.2. Configure Training pipeline
Now that we have downloaded and extracted our pre-trained model, let’s create a directory for our training job. Under the `training_demo/models` create a new directory named `ssd_mobilenet_v2_fpnlite` and copy the `training_demo/pre-trained-models/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/pipeline.config` file inside the newly created directory. Our `training_demo/models` directory should now look like this.
```
training_demo/
├─ ...
├─ models/
│  └─ ssd_mobilenet_v2_fpnlite/
│     └─ pipeline.config
└─ ...
```