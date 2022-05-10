# OpenCV_Projects
Multiple OpenCV projects that range from reading images and videos to analysing contours and detecting face, covering different aspects of Image Processing. This repository is inspired from Murtaza Hassan's the online tutorial video that can be found [here](https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=285s&ab_channel=Murtaza%27sWorkshop-RoboticsandAI).

## Summary of utilities of each file:
- `canny_edge_detection.py` : Detecting edges involving Grayscale, Blur, Canny Edge detection, Dialation, Erosion
- `face_detection.py` : Detecting faces in an image using haarcascade_frontalface_default.xml
- `read_img_vid.py` : Read images and videos from folders as well as realtime webcam
- `resize_crop_img.py` : Basics of Resizing and Cropping images
- `draw_write_img.py` : To daw shapes and impose text on images
- `stack_img.py` : Stacking Images horizontally and vertically
- `warp_image.py` : Warp an image of a card to straighten it in the output
- `shape_detection.py` : Detecting shapes by analysing contours, bounding boxes, after converting to GrayScale
- `color_identification.py` : Identify Orange color from the Lambo image(*provided in Resources Folder*) and isolate using HSV
- `color_picker.py` : To help identify HSV values of any color in an inputted image
- `Project1.py` : Webcam Color identification and draw using HSV color detection and contour detection, then use bounding boxes


## To setup:
You can use a code editor of your choice, but I personally find **PyCharm** very user friendly and easy to use.

### Steps to install **PyCharm** (Ubuntu):
1. Download the tarball .tar.gz from [Here](https://www.jetbrains.com/pycharm/download/#section=linux)
2. Extract the tarball to a directory that supports file execution.For example, if the downloaded version is 1.17.7391, you can extract it to the recommended /opt directory using the following command:
    - `sudo tar -xzf jetbrains-toolbox-1.17.7391.tar.gz -C /`
3. Switch to the bin subdirectory:
    - `cd /opt/pycharm-*/bin`
4. Run pycharm.sh from the bin subdirectory:
    - `sh pycharm.sh`

### Clone the Repository files:
1. Go to your workspace (any folder where you which to maintain this code)
2. Open terminal at that location (Right-Click -> Open in Terminal)
3. Clone the repostory by pasting the following into the opened terminal:
    - `git clone "https://github.com/PulkitRustagi/OpenCV_Projects.git"`
