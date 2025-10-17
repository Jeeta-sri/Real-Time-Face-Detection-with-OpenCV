
# 🧠 Real-Time Face Detection with OpenCV

A simple Python application that uses **OpenCV** and a **Haar Cascade classifier** to perform real-time face detection from a webcam feed.



## 📘 Description

This project demonstrates a beginner-friendly implementation of a **face detection system** using computer vision techniques.  
It captures live video from your computer’s default webcam, processes each frame to identify human faces, and overlays a **green rectangle** around any detected faces.



## 🚀 Features

- **Real-time Detection** – Processes live webcam feed instantly.  
- **Haar Cascade Classifier** – Uses a pre-trained, robust algorithm for face detection.  
- **Lightweight** – Requires only Python and OpenCV.  
- **Easy to Understand** – Clean, well-commented code suitable for beginners.



## ⚙️ How It Works

1. **Initialize Video Capture:**  
   Accesses the default webcam using `cv2.VideoCapture(0)`.

2. **Load Classifier:**  
   Loads the pre-trained model `haarcascade_frontalface_default.xml`.

3. **Frame Processing Loop:**  
   - Reads one frame at a time.  
   - Converts the frame to **grayscale**.  
   - Uses `detectMultiScale()` to detect faces.  
   - Draws a **green rectangle** on the original color frame.

4. **Display Output:**  
   Shows the video feed in a window titled **"Face Detection System"**.

5. **Exit:**  
   Press the **`q`** key to quit the application.



## 🧩 Requirements

- Python 3.x  
- OpenCV (`opencv-python`)



## 🛠️ Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Jeeta-sri/Real-Time-Face-Detection-with-OpenCV
   cd Real-Time-Face-Detection-with-OpenCV
````


