import os
import cv2
from deepface import DeepFace

# Directory containing known faces
known_faces_dir = 'known_faces'

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    # Save the current frame as a temporary file
    cv2.imwrite("temp.jpg", frame)

    # Iterate through known faces
    for filename in os.listdir(known_faces_dir):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            known_face_path = os.path.join(known_faces_dir, filename)
            
            try:
                # Perform face verification
                result = DeepFace.verify("temp.jpg", known_face_path, enforce_detection=False)
                
                # Check the resultkk
                if result['verified']:
                    print(f"Match found: {filename}")
                    print(f"Similarity score: {result['distance']}")
                    print(f"Threshold: {result['threshold']}")
                    print(f"Model: {result['model']}")
                    print(f"Detector backend: {result['detector_backend']}")
                    print("-------------------------")

            except Exception as e:
                print(f"Error in face verification for {filename}: {str(e)}")

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture and destroy windows
cap.release()
cv2.destroyAllWindows()

# Remove the temporary file
os.remove("temp.jpg")
