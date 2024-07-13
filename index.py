import face_recognition
if not __name__ == "__main__":
    print('Please do not import libraries.')
    quit()
import os
import cv2
import numpy as np
from ultralytics import YOLO
import random
from deepface import DeepFace

import ollama
import base64
import time
import json as js
import numpy as np
import yagmail
from dotenv import load_dotenv
import yagmail.oauth2  # Add this import
from time import asctime
from os import getenv
import time
import readline as rl
import mpmath
from deepface import DeepFace
from urllib.parse import quote
known_faces_dir = 'known_faces'

load_dotenv()
zr=quote(time.asctime())
# Open a log file
logs = open(f'logs{quote(zr)}.txt', 'w')
logs.write('-|ed')
dm = open(f'logs{quote(zr)}.txt', 'a')

def write_logs(text):
    dm.write(str(text))
    return True


def get_camera_url():
    return int(input('Camera Index:'))
             
emails = []
for i in range(int(input('What is the number of emails to send to?'))):
    email = input(f'Email #{i + 1}:')
    emails.append(email)
write_logs(f"Emails: {emails}")
def load_known_faces():
    known_faces = []
    for filename in os.listdir('known_faces'):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            image_path = f'known_faces/{filename}'
            known_faces.append((image_path, filename.split('.')[0]))  # Tuple of (path, name)
    return known_faces

known_faces = load_known_faces()
def send_email(subject, body, image_path, receiver):
    sender_email = os.getenv('email')
    sender_password = os.getenv('email_password')
    receiver_email = receiver
    
    if not all([sender_email, sender_password]):
        print("Error: Missing environment variables for email configuration.")
        return
    
    try:
        yag = yagmail.SMTP(user=sender_email, password=sender_password)
        
        yag.send(
            to=receiver_email,
            subject=subject,
            contents=[body, yagmail.inline(image_path)]
        )
        print("Email sent successfully.")
        write_logs(f'Sent email sucessfully to {receiver}')
    except yagmail.error.YagAddressError as e:
        print(f"Error with email address: {str(e)}")

known_face_encodings = [

]
known_face_names = [

]
def get_camera_url():
    return int(input('Camera Index:'))
emails = []
number_of_emails = input('Number of emails that are going to be sent to:')
for i in range(int(number_of_emails)):
    email = input(f'Email #{i + 1}: ')
    emails.append(str(email))
    
write_logs(f"Emails: {emails}")

def send_email(subject, body, image_path, receiver):
    sender_email = os.getenv('email')
    sender_password = os.getenv('email_password')
    receiver_email = receiver
    
    if not all([sender_email, sender_password]):
        print("Error: Missing environment variables for email configuration.")
        return
    
    try:
        yag = yagmail.SMTP(user=sender_email, password=sender_password)
        
        yag.send(
            to=receiver_email,
            subject=subject,
            contents=[body, yagmail.inline(image_path)]
        )
        print("Email sent successfully.")
        write_logs(f'Sent email sucessfully to {receiver}')
    except yagmail.error.YagAddressError as e:
        print(f"Error with email address: {str(e)}")
    except yagmail.error.YagConnectionClosed as e:
        print(f"Connection closed unexpectedly: {str(e)}")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

def process_frame_with_llava(frame):
    image_path = 'image.png'
    cv2.imwrite(image_path, frame)
    _, buffer = cv2.imencode('.jpg', frame)
    img_str = base64.b64encode(buffer).decode('utf-8')
    try:
        response = ollama.generate(model='llava', 
                                   prompt='You are AI Security. When an person is detected, (it does not provide a name. The name is unkown always,due to the program not being able to identify people.). The image below has either an image of a person, a car, or a fire. Your goal is to provide people with a brief (under 100 words ) description of what is going on through a camera. Good luck!', 
                                   images=[img_str])
        return response['response'], image_path
    except Exception as e:
        return f"Error processing image with Llava: {str(e)}", None

def attempt_connection(url, max_attempts=5, delay=2):
    for attempt in range(max_attempts):
        print(f"Connection attempt {attempt + 1}/{max_attempts}")
        if isinstance(url, str) and url.startswith("rtsp://"):
            cap = cv2.VideoCapture(url)
        else:
            cap = cv2.VideoCapture(url)
            write_logs('Finsihed creating cap for videoCapture')
        
        if not cap.isOpened():
            print(f"Failed to open camera. Error code: {cap.get(cv2.CAP_PROP_BACKEND)}")
            cap.release()
            dm.write(f'Failed to open camera. Error code: {cap.get(cv2.CAP_PROP_BACKEND)}')
            time.sleep(delay)
            continue
        
        ret, frame = cap.read()
        if not ret:
            print(f"Failed to read frame. Error code: {cap.get(cv2.CAP_PROP_POS_FRAMES)}")
            cap.release()
            time.sleep(delay)
            continue
        
        print("Successfully connected and read a frame.")
        return cap
    
    print("Failed to connect after maximum attempts.")
    return None

camera_url = get_camera_url()
print(f"Attempting to connect to: {camera_url}")



model = YOLO(getenv('model'))
write_logs(f"Choose model {getenv('model')}")
cap = attempt_connection(camera_url)

if cap is None:
    print("Could not connect to the camera. Please check your camera settings and try again.")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame. Attempting to reconnect...")
        cap.release()
        cap = attempt_connection(camera_url)
        if cap is None:
            print("Reconnection failed. Exiting...")
            break
        continue

    activate_ollava = False
    results = model(frame)
    dm.write('Generated model...')
    fai = False
    # Face recognition
    
    # Existing YOLO detection code
    for result in results:
        boxes = result.boxes.cpu().numpy()
        for box in boxes:
            class_id = int(box.cls[0])
            class_name = result.names[class_id]
            x1, y1, x2, y2 = box.xyxy[0].astype(int)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{class_name} - {box.conf[0]:.2f}% ",
                        (x1, y1 - 10), cv2.FONT_HERSHEY_TRIPLEX, 0.9, (255, 0, 0), 2)

    items = []
    for result in results:
        boxes = result.boxes.cpu().numpy()
        for box in boxes:
            class_id = int(box.cls[0])
            class_name = result.names[class_id]
            if class_name in ['person', 'fire', 'cat', 'dog', 'motorcycle', 'airplane', 'bird', 'bus']:
                activate_ollava = True
                items.append(class_name)
                if class_name == 'person':
                    fai = True
                    dm.write('\n Detected a person!')
                    if getenv('face_recognition_flag') == True:
                        cv2.imwrite("temp.jpg",frame)
                        face_recognition_store_info = ""
                        print('AI Face Recognition Activated')
                        for filename in os.listdir(known_faces_dir):
                            if filename.endswith((".jpg",".jpeg",".png")):
                                known_face_path = os.path.join(known_faces_dir,filename)
                                try:
                                    # Try to perform face detection
                                    result = DeepFace.verify("temp.jpg",known_face_path,enforce_detection=False)
                                    if result['verified']:
                                        print('detected a person!')
                                        print(f"Match found: {filename}")
                                        print(f"Similarity score: {result['distance']}")
                                        print(f"Threshold: {result['threshold']}")
                                        print(f"Model: {result['model']}")
                                        print(f"Detector backend: {result['detector_backend']}")
                                        print("-------------------------")
                                        face_recognition_store_info += f"Match Found: {filename} \n"
                                        face_recognition_store_info += f"Similiarity Score: {result['distance']} \n"
                                        
                                    else:
                                        print('Did not detect a face in the known library.')
                                except Exception as e:
                                    print(f"Error in face recognition for {filename}:{str(e)}")
                        os.remove('temp.jpg')
                    

    if activate_ollava:
        llava_description, image_path = process_frame_with_llava(frame)
        print("Llava description:", llava_description)
        edx = f"{llava_description} \n Items that the AI Detected: {', '.join(items)}"
        if image_path:
            for email in emails:
                send_email(getenv('message_subject'), edx, image_path, email)
 
        if fai:
            dm.write(f'\n Sleeping for {getenv("detect_person_delay")}')
            time.sleep(float(getenv('detect_person_delay')))

    cv2.imshow('Camera Feed', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
