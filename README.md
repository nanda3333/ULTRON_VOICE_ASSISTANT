# ULTRON_VOICE_ASSISTANT
Ultron2 is a modular Python security system that uses face recognition for authentication and local command execution post-login. The system is structured to simulate an intelligent assistant capable of facial login and controlled access to system features.

 Python Module Descriptions
The core logic of Ultron2 is built in Python and is organized under the engine/ directory. Each Python module plays a specific role:

### 🧠 main.py
Acts as the central control script that integrates the authentication system and command features. It can be used to initiate the full functionality after model training and authentication are completed.

### 📁 engine/auth/sample.py
This module captures facial image data from the webcam using OpenCV. It saves images in the samples/ directory with a naming convention that includes the user ID. These images are later used for training the face recognition model.

### 🧠 engine/auth/trainer.py
Trains a Local Binary Pattern Histogram (LBPH) face recognizer on the dataset collected by sample.py. It uses OpenCV’s cv2.face.LBPHFaceRecognizer_create() and stores the model in a file (trainer.yml) for use in recognition.

### 🔐 engine/auth/recognize.py
Performs real-time face recognition using the webcam and the previously trained LBPH model. When a known face is detected, it confirms the identity and grants access to the rest of the system.

### ⚙️ engine/command.py
Contains the logic to interpret and execute system-level commands after a user is authenticated. It can trigger programs, utilities, or scripts conditionally based on predefined logic or input.

### 🧰 engine/features.py
Defines available system features that can be toggled or invoked. It typically acts as a bridge between user interaction (post-authentication) and specific command executions.

### 🛠️ engine/config.py
Stores configuration variables such as user information, ID mappings, or paths. It allows central management of settings that other modules can import and use consistently.

### 🔄 engine/db.py
Handles interaction with the SQLite database (ultron.db). This includes logging authentication events or storing user-related metadata. It uses Python’s built-in sqlite3 module.

### 🧪 engine/helper.py
Utility module containing reusable helper functions like file management, user info processing, or status formatting. It’s imported by other modules to avoid code duplication.

### 🧠 run.py
An optional alternative launcher that may be used to start the program under different test modes or isolated workflows.
