import cv2

# Load the pre-trained Haar Cascade classifier for face detection
# Make sure the 'haarcascade_frontalface_default.xml' file is in the same directory
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize video capture from the default webcam (usually index 0)
video_capture = cv2.VideoCapture(0)

print("Starting video capture... Press 'q' to quit.")

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Convert the frame to grayscale for the face detection algorithm
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    # The detectMultiScale function returns a list of rectangles (x, y, w, h) for each detected face
    # scaleFactor: How much the image size is reduced at each image scale.
    # minNeighbors: How many neighbors each candidate rectangle should have to retain it.
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        # cv2.rectangle(image, start_point, end_point, color, thickness)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame with detected faces
    cv2.imshow('Face Detection System', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture and destroy all windows
video_capture.release()
cv2.destroyAllWindows()

print("Video capture stopped.")