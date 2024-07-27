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
TensorFLow/
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
