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
