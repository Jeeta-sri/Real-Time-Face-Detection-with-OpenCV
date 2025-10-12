
# Real-Time Face Detection with OpenCV

A simple Python application that uses OpenCV and a Haar Cascade classifier to perform real-time face detection from a webcam feed.

## Description

This project provides a straightforward implementation of a face detection system. It captures video from your computer's default webcam, processes each frame to identify human faces, and overlays a green rectangle on any detected faces. It's a great beginner project for anyone interested in computer vision.

## Features

  - **Real-time Detection**: Captures and processes your webcam feed live.
  - **Haar Cascade Classifier**: Uses a pre-trained, robust algorithm for object detection.
  - **Lightweight**: Minimal dependencies, requiring only Python and OpenCV.
  - **Simple & Understandable**: The code is well-commented and easy to follow.

-----

## How It Works

The script follows these main steps:

1.  **Initialize Video Capture**: Accesses the default webcam using `cv2.VideoCapture(0)`.
2.  **Load Classifier**: Loads the pre-trained `haarcascade_frontalface_default.xml` model.
3.  **Frame Processing Loop**:
      * Reads one frame at a time from the video stream.
      * Converts the color frame to grayscale, as the detection algorithm works on grayscale images.
      * The `detectMultiScale` function is called on the grayscale frame to find face coordinates (x, y, width, height).
      * A `for` loop iterates through the coordinates of any detected faces.
      * A green rectangle is drawn on the original **color** frame using these coordinates.
4.  **Display Output**: The final frame with the rectangle is displayed in a window titled "Face Detection System".
5.  **Exit**: The application quits when the user presses the 'q' key.

-----

## Requirements

  - Python 3.x
  - OpenCV (`opencv-python`)

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2.  **Install the required package:**
    It's recommended to use a virtual environment.

    ```bash
    pip install opencv-python
    ```

3.  **Ensure the Haar Cascade file is present:**
    This project requires the `haarcascade_frontalface_default.xml` file. Make sure it is in the same directory as the Python script.

-----

## Usage

To run the application, navigate to the project directory in your terminal and execute the following command:

```bash
python face_detector.py
```

A window will appear showing your webcam feed. Position your face in front of the camera, and a green box should appear around it. To stop the program, press the **'q'** key.

-----

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.