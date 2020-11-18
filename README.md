# Raspberry Pi Object Detection

![Robot Overview](https://github.com/Hansxsourse/Elec1601-proj-object-detection/blob/main/image/photo_2020-11-18_23-01-44.jpg)

## Reference
[Tutorial to set up TensorFlow Object Detection API on the Raspberry Pi](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi#6-detect-objects)

[How To Train an Object Detection Classifier for Multiple Objects Using TensorFlow (GPU) on Windows 10](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10)

[TypeError: export_inference_graph() got an unexpected keyword argument 'use_side_inputs' #8711](https://github.com/tensorflow/models/issues/8711)

[DeepPiCar](https://github.com/dctian/DeepPiCar)

[TensorFlow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection)

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

### Training Faster-RCNN-Inception_V2 Model Using Trained Weights

#### Configs

Go to folder `models/research/object_detection/samples/configs` to copy file `faster_rcnn_inception_v2_pets.config` to folder `object_detection/training/`. Then edit configs for number of class to your own data classes, also config the path of data and label maps. Important to modify the training steps, it is enough for me to train my data for 2000 steps, which you can decide by your self to avoid overfitting and underfitting depends on your data and etc.

#### Training

In some version of tensorflow object detection api, the `train.py` file has been changed, so please copy `train.py` from folder `legacy` to your working path.

```bash
python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_v2_pets.config
```
![Training log](https://github.com/Hansxsourse/Elec1601-proj-object-detection/blob/main/image/Training_Progress.png)


After training process done, we need to generate inference graph `.pb` file from the training out put. 

```bash
python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/faster_rcnn_inception_v2_pets.config --trained_checkpoint_prefix training/model.ckpt-XXXX --output_directory inference_graph
```

It might not working in the latest api file, refer to [this issue post](https://github.com/tensorflow/models/issues/8711#issuecomment-647141998), we can download old version of `export_inference_graph.py` or use `export_old.py` in my repo by:

```bash
python export_old.py --input_type image_tensor --pipeline_config_path training/faster_rcnn_inception_v2_pets.config --checkpoint_path training/model.ckpt-XXXX(THE BEST STEP NUMBER) --inference_graph_path output_inference_graph.pb
```

WELL DONE FOR MODELING!!!

#### Tips: Try to Avoid Overfit

I tried both low epoch and high epoch number, because the super small size of my pingpong dataset and we do not build a strong metric, it will be easily overfit!!! Like the picture below, it recognize my Google Home mini speaker as a pingpong.

![Overfit](https://github.com/Hansxsourse/Elec1601-proj-object-detection/blob/main/image/Screenshot%20from%202020-11-09%2001-07-46.png)


### Inference by Webcam on Raspberry Pi

####  Sending Video FLow to Server
VLC is a good tool to send the flow with bandwidth efficiency. But when we using ffmpeg to encode the video on raspberry pi and decode on server, it caused a significant latency. So what I finally choose is the package `motion`, which is a tool with much much lower latency.

BTW, if your raspberry pi and server network environment do not have a public ip address, I suggest using `frp` by config clints both on raspberry pi and server, also config a cloud server with server `frp` like `Google Cloud`. Btw again, `ngrok` is a easier way to get, but you do need worry about the bandwidth.

#### Start Inference and Get the Feedback by GPIOs
Easily run `python3 rpi.py` after the server's `Object_detection_picamera.py` is running. They should communicate the feedback by a python socket using a independent port.

As my seeting, pin `5` for Raspberry Pi 4th Gen will returen a high signal when detected a pingpong, pin `6` will return another higgh signal when the distance is suitable to pick up the ball. Then we can connet these two pin to the rebot controller like arduino to control the pick up arm using server motor. 



## Author

[Lehan Yang](https://www.xsourse.cc/), The University of Sydney
