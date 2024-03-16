import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained RPS classification model
model = load_model('rps_model.h5')

# Define classes
classes = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}

# Initialize camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Preprocess frame
    resized_frame = cv2.resize(frame, (150, 150))
    normalized_frame = resized_frame / 255.0
    input_frame = np.expand_dims(normalized_frame, axis=0)
    
    # Make prediction
    prediction = model.predict(input_frame)
    predicted_class = np.argmax(prediction)
    gesture_text = classes[predicted_class]
    
    # Display result on frame
    cv2.putText(frame, gesture_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display frame
    cv2.imshow('Rock Paper Scissors Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
