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