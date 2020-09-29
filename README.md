## Python Car and Pedestrian Tracker

A pedestrian and car tracker using opencv-python.
 Use `pip install opencv-python` in terminal while having `Python 3.8` already installed.
 In the `carPedestrianTracking.py`, replace
 ```
    img_file = 'index.jpeg'
    video_car = cv2.VideoCapture('Tesla2.mp4')
    video_pedestrian = cv2.VideoCapture('Pedestrians.mp4')
```
with the the respective image and video files you wish to use for tracking.
NB:- Make sure you get the video location correctly, I recommend just having the video and image file
in the same directory as the `.py` file.