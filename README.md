# tfod-v1
Object Detection using TensorFlow2

## Using this link
https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html#verify-your-installation


# Creating Environment
### Create Conda Environment(Isolated)
    conda create --prefix ./tfod python=3.9

### Activate Environment
    conda activate ./tfod


# Tensor Flow installation
### pip installation
    pip install --ignore-installed --upgrade tensorflow==2.5.0

### Verification
`CPU`

    python -c "import tensorflow as tf;
    print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

<img src = "repo_files\verify.jpg">

`GPU`

    python -c "import tensorflow as tf; 
    print(list(tf.config.experimental.list_physical_devices('GPU')));"

<img src = "repo_files\verify_gpu.jpg">

# Downloading TensorFlow Garden Model
#### 1. Create `TensorFLow` directory.
#### 2. GIT clone `TensorFlow Models Repository` inside TensorFlow folder.
```
TensorFLow/
    |-----Models/
            |----community
            |----docs
            |----Official
            |----research
            |---- ...
``` 
**Protoc files to current directory**  
`CMD`  

    for /f %i in ('dir /b "C:\Program Files\Google Protobuf\include\google\protobuf\*.proto"') do protoc ""C:\Program Files\Google Protobuf\include\google\protobuf\%i" --python_out=.

### Protobuf Installation
**Download protoc-27.2-win64.zip**
https://github.com/protocolbuffers/protobuf/releases/tag/v27.2

**Setup Env Path for Protoc**
```
Step1: 
Step2:
```

`Navigate`
```cmd
cd Tensorflow\models\research\
```
**Either use cmd or shell**  
This command generates Python code from `.proto` files located in the `object_detection/protos` directory using the `protoc` compiler. The generated Python files are saved in the current directory.

`CMD`
```cmd
for /f %i in ('dir /b object_detection\protos\*.proto') do protoc object_detection\protos\%i --python_out=.
```
`Powershell`
```sh
Get-ChildItem object_detection/protos/*.proto | foreach {protoc "object_detection/protos/$($_.Name)" --python_out=.}
```
# Coco API installation
Run the following command to install `pycocotools` with Windows support.

```sh
pip install cython
pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
```

Note that, according to the package’s instructions, Visual C++ 2015 build tools must be installed and on your path. If they are not, make sure to install them from <a href ="https://go.microsoft.com/fwlink/?LinkId=691126">here</a>.

# Install Tensorflow Object Detection API

```sh
# From within TensorFlow/models/research/
cp object_detection/packages/tf2/setup.py .
python -m pip install .
```

# Verify the Model Installation
```sh
# From within TensorFlow/models/research/
python object_detection/builders/model_builder_tf2_test.py
```