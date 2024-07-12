# AISecuritySystem
## Minimum Requirements:
- RTX 2080 Super
- Intel/AMD (atleast 4 cores, 2.4 Ghz)
- Ubuntu 20.04/Win10+/ MacOS (Not recommended
### Included Utility tools:
- Detect all avaliable opencv indexes.
-  Download yolov8 model
- Modify .env settings
AI Security system is a python program thjat uses Ultralytics to identify trigger objects, which are 
`person,fire,cat,dog,motorcycle airplane bird bus`.
You can modify  these settings with the utility tools. When a person, is detected, it runs Ultralytics to confirm that the object is an person, and then runs the image through llava. LLAVA produces an short summary of what is going on in the picture and provides the list of objects that it detected. For a person, it pauses for approx. 10 seconds by default so that it will not spam emails to the people subscribed.
## Installation:
#### Installing DLIB
To install dlib, please look below
- Windows 10: Not required, dlib is already installed
- MacOS: run `brew install cmake`
- Linux: Please view  https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf.
#### Installing main program
Now, run
	`git clone https://github.com/RA86-dev/AISecuritySystem && cd AISecuritySystem && pip install -r requirements.txt && python3 utility_tools.py`.
	This will now open a UI. Please type 2. This will open the customization tab. Please enter a email and password so that the AI can send messages to you, and fill out the form. Now, hit `CTRL+C` (`Command+C` on mac) to quit. Now, you can run python3 index.py.
``

### Configurations:
#### Face Recognition (BETA)

Face Recognition is a feature that allows the user to detect people via their faces. In order to start it, please run
`python3 utility_tools.py` in the same directory as the main file. This will open up a quick terminal-based ui.
	1. Type 2. This will open a user interface to modify the .env file.
	2.Please finish entering the form.
	 3. After that, the .env's face_recognition_flag will be set to true. Please go to the directory known_faces. Inside, please put a photo of the people going to be face_recognized. Please name the photo like `John_doe.jpg`. This will make it easier for the AI to identify the photos inside the folder.
	 4. And your done! It will provide a box saying `unkown` if it cannot identify the person in the camera. If you have any errors, please put it in the errors page on our github.
