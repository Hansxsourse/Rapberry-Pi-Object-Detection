# Elec1601-proj-object-detection

## Legacy Opencv Pingpong Detection

### Introduction
It contributed a circle detection method on Raspberry Pi by using Hough circle detection, done by OpenCV

### User Guild

#### Step 1 Plug webcam to usb port( doesn't support official raspberry pi cam yet)
hint: Remember plug usb2.0 cam to usb 2.0 port, it will cause bugs if connect to usb3.0 port

#### Step 2 install releted packages
```bash
pip3 install opencv-python
pip3 install numpy
```

#### Step 3 Run `det.py`
```bash
python3 det.py
```
It will print the `r` of the first circle in the webcam if circle exist, or print `bad` if doesn't exist.

And return `high` to GPIO port `2` if the circle's r is greater than a value

Only works with 1 circle yet(as we only need to carry one ball object in our presentation)

### Feture
do some de-noisy methods for the input source

optimizations

add auto run script to environment 

## Deep Learning Pingpong Object Detection

### Introduction

This is a deep learning based way to detect the object pinpong and caculate the estimate distance by bounding box area.

### Requirement
`Tensorflow 1.14.0`

`Tensorflow Object Detection API`

### Making Dataset for training model

Refer [this repo](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10) to make sure you have collect your own data and annatated them, also generate correct TF Record file and label maps. Or just use my example dataset upload in the folder `data` or just use files in `training` folder.

### Training Faster-RCNN Model

