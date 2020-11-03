# Elec1601-proj-object-detection

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

