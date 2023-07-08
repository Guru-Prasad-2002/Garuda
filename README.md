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

![Login_Page](https://user-images.githubusercontent.com/93508612/217592255-cb885414-3277-42cf-afa6-83d12e3eef3a.png)
<p align="center">
  <strong>Login Page</strong>
</p>

![Tables](https://user-images.githubusercontent.com/93508612/217592292-8bfd2677-a0fe-4772-97fa-32ee5a535f6f.png)
<p align="center">
  <strong>Tables</strong>
</p>

![Create](https://user-images.githubusercontent.com/93508612/217592228-8c0a8c27-d8b5-437d-9706-494603658bec.png)
<p align="center">
  <strong>Create</strong>
</p>

![Cars_Table](https://user-images.githubusercontent.com/93508612/217592211-0678693a-87d6-462d-8e67-ba57021c25a6.png)
<p align="center">
  <strong>Cars</strong>
</p>

![Showroom_Table](https://user-images.githubusercontent.com/93508612/217592290-0dac3abe-22f2-4700-a78f-a36309c6452c.png)
<p align="center">
  <strong>Showroom</strong>
</p>

![Managers_table](https://user-images.githubusercontent.com/93508612/217592260-2bd72372-75f5-4644-9eca-f3991e35eb0f.png)
<p align="center">
  <strong>Managers</strong>
</p>

![Sales_Table](https://user-images.githubusercontent.com/93508612/217592281-4968ef98-e4de-467f-9f1a-c623f27b2c28.png)
<p align="center">
  <strong>Sales</strong>
</p>

![Customer_table](https://user-images.githubusercontent.com/93508612/217592231-a6792184-f856-4fa9-8976-d86868b74664.png)
<p align="center">
  <strong>Customers</strong>
</p>

![Sell](https://user-images.githubusercontent.com/93508612/217592286-b7afa843-655a-4cf6-9c04-f7a064684fb7.jpg)
<p align="center">
  <strong>Sell</strong>
</p>

![Info_Page](https://user-images.githubusercontent.com/93508612/217592247-7ed86a6c-772a-4e1b-8ac6-79c247b730de.jpg)
<p align="center">
  <strong>Info Page</strong>
</p>

![Queries](https://user-images.githubusercontent.com/93508612/217592276-52d2adb6-ab5d-4cf1-9ec0-84df42ab8865.jpg)
<p align="center">
  <strong>Queries</strong>
</p>

![Queries2](https://user-images.githubusercontent.com/93508612/217592279-cbe1973a-ce15-4005-bd35-171fcea6f091.jpg)
<p align="center">
  <strong>Queries_2</strong>
</p>

![Cars_With_Most_Sales](https://user-images.githubusercontent.com/93508612/217592224-fb27310c-6f87-44a5-8e64-9b5e791b4355.png)
<p align="center">
  <strong>Cars With Most Sales</strong>
</p>

![Least_Expensive_Cars](https://user-images.githubusercontent.com/93508612/217592249-4527e750-f3d6-4b01-8e3a-1e5b899c9fe7.png)
<p align="center">
  <strong>Least Expensive Cars</strong>
</p>

![Most_Expensive_Cars](https://user-images.githubusercontent.com/93508612/217592269-840602f3-6ece-455d-a8b5-6c4a451892f7.png)
<p align="center">
  <strong>Most Expensive Cars</strong>
</p>

![Managers_with_salary_greater_than](https://user-images.githubusercontent.com/93508612/217592262-7bd6ce21-72e9-4a3b-8184-6a13e0ca0020.png)
<p align="center">
  <strong>Managers with salary greater than</strong>
</p>

![Most_Regular_Customers](https://user-images.githubusercontent.com/93508612/217592274-238ab8b7-8de0-417c-a880-ff9f47f46ec5.png)
<p align="center">
  <strong>Most Regular Customers</strong>
</p>


