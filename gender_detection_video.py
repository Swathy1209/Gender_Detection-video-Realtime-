import cv2
import numpy as np

# Load pre-trained models for face detection and gender classification
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Load the pre-trained gender classification model
# Use models like MobileNet or custom-trained models
gender_model = cv2.dnn.readNetFromCaffe(
    'c:/Users/swathiga/Downloads/gender_deploy (1).prototxt',
    'c:/Users/swathiga/Downloads/gender_net (1).caffemodel'
)

# List of gender classes
GENDER_LIST = ['Male', 'Female']

# Process video
video_path = "c:/Users/swathiga/Downloads/video.mp4"
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extract the face region
        face = frame[y:y+h, x:x+w]
        blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), (104.0, 117.0, 123.0), swapRB=False)
        print(f"Face shape: {face.shape}")
        print(f"Blob shape: {blob.shape}")


        # Predict gender
        gender_model.setInput(blob)
        gender_preds = gender_model.forward()
        gender = GENDER_LIST[gender_preds[0].argmax()]

        # Draw a rectangle and label around the face
        label = f"{gender}"
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    # Display the frame with predictions
    cv2.imshow('Gender Prediction', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
