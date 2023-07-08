# Garuda‐IoT based Home Security System

Garude is an IoT-based home security system designed to ensure inhabitant safety. It incorporates face recognition using OpenCV and the face_recognition library. When an unknown face is detected, an SMS with timestamp is sent using BoltIot, and logs are stored in a database. The web interface, built with Flask and Bootstrap, allows access to the logs and supports user registration for enhanced security measures like automatic door locking.

## Getting Started

1. Clone the repository:

   - Open your terminal and navigate to the desired directory.
   - Run the command: `git clone <repository_url>`.

2. Install requirements:

   - Ensure you have Python installed on your system.
   - Navigate to the project directory in the terminal.
   - Run the command: `pip install -r requirements.txt` to install the required dependencies.

3. Set up the web interface:

   - Make sure you have XAMPP installed for the database.
   - Start Apache and MySQL in XAMPP control panel.

4. Connect an external video source:

   - Ensure you have a compatible external video source, such as a webcam, connected to your computer.
   - Begin running inference.py to enable real-time inference on the external video source.

5. Run inference:

   - Open a new terminal window.
   - Navigate to the project directory.
   - Run the command: `python inference.py`.
   - This will start running the face recognition inference on the connected video source.

6. Run the web interface:

   - In a separate terminal window, navigate to the project directory.
   - Run the command: `python app.py`.
   - This will start the Flask web server.
   - Open a web browser and go to `http://localhost:5000` to access the home screen.

7. Register and login:

   - On the home screen, use the "Register" button to register new users using the webcam.
   - Once registered, you can log in using your credentials.

8. Access logs and unlock door:

   - After logging in, you can access the logs on the web interface to review past events.
   - When an unknown person is detected, a message with the timestamp will be sent to the registered phone number.
   - The door will be locked automatically for security.
   - To unlock the door, use the "Unlock" button on the web interface.

Note: Make sure you have the necessary hardware and configurations in place for the external video source and database setup.



## Features

Features of Garuda:

- Face Recognition: Implements face recognition technology to identify known and unknown individuals.
- IoT Integration: Utilizes IoT devices like BoltIot for sending SMS alerts and controlling door locking mechanisms.
- Web Interface: Provides a user-friendly web interface for accessing logs, registering users, and unlocking doors.
- Log Storage: Stores logs of detected faces, timestamps, and security events for future reference.
- Active Security Measures: Automatically locks the door when an unknown person is detected for enhanced safety.
- External Video Source: Supports real-time inferencing on an external video source, such as a webcam.
- Database Integration: Connects with a database, such as MySQL, to store user information and system data.
- Responsive UI: Ensures a seamless user experience with a responsive and intuitive interface.
- Scalability: Designed to handle a growing number of users, devices, and security requirements.
- Customizability: Allows customization based on specific security needs and preferences.



## Screenshots

![Register](https://github.com/Guru-Prasad-2002/Garuda/assets/93508612/a8bfb7c4-e10d-46ba-88be-48e185f64b3e)
<p align="center">
  <strong>Sign Up Page</strong>
</p>

![Login](https://github.com/Guru-Prasad-2002/Garuda/assets/93508612/b971e168-af21-4860-930f-33d6173483c0)
<p align="center">
  <strong>Login Page</strong>
</p>


