import os
from ultralytics import YOLO
import cv2
def detect_camera_ids(): 
    openCvVidCapIds = []

    for i in range(-1000,100):
        try:
            cap = cv2.VideoCapture(i)
            if cap is not None and cap.isOpened():
                openCvVidCapIds.append(i)

        except:
            pass
    
    print(str(openCvVidCapIds))
    return str(openCvVidCapIds)
def customize_settings():
    print('customising settings...')
    email_password = input('Email Password:')
    email=input('Email:')
    model = input('Ultralytics YOLO Model:')
    message_subject = input('Message Subject: ')
    detect_person_delay = input('Detected person delay: ')
    print('READ more in README.')
    enable = input('Enable Face Recognition (BETA): y/n').lower()
    if enable == "y" or enable == "yes":
        flag_face_rcg = True
        if not os.path.isdir('known_faces'):
            os.mkdir('known_faces')
    else:
        flag_face_rcg = False
    with open('.env','w') as env:
        env.write(f'''
email_password={email_password}
email={email}
model={model}
message_subject={message_subject}
detect_person_delay={detect_person_delay}

face_recognition_flag={flag_face_rcg}
''')
        env.close()
    print('Verified and confirmed.')
def download_model(model_name):
    model = YOLO(model_name)
    print('Installed!')
print('''
Utility Tools:
      1. Detect Camera Feed Indexes
      2. Customize settings
      3. Download Model
      4. Quit()



''')
if __name__ == "__main__":
    while True:
        i = input('>>>')
        if int(i) == 1:
            detect_camera_ids()
        elif int(i) == 2:
            customize_settings()
        elif int(i) == 3:
            model = input('Model name:')
            download_model(model)
        elif int(i) == 4:
            exit(401)
