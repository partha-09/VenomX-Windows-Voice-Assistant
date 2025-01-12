### VTU Final Year Project:VenomX: AI-Powered Voice Assistant for Windows
VenomX is a cutting-edge voice assistant built for Windows, utilizing AI technologies to perform a variety of tasks based on voice commands. 
It integrates NLP for task execution, real-time object detection using YOLO,and provides multiple utilities like system control, automation,
and entertainment. The project is designed to demonstrate the power of voice interaction on Windows systems.
---
### 🌟 Key Features
1. Voice Interaction: Listens to and processes user commands via voice input using a microphone. Responds using text-to-speech (TTS) with customizable voices and rates.
2. Greeting System: Greets the user based on the time of day (morning, afternoon, evening). Provides friendly and conversational responses to user greetings and queries.
3. File Management: Performs basic file operations (open, create, rename, delete files). Manages directories and organizes files systematically (partially implemented).
4. Web Automation: Searches on Google, YouTube, and Wikipedia. Opens specific websites like Gmail, Facebook, Instagram, and Twitter. Automates web browser actions (open/close tabs, navigate pages, bookmark management).
5. Application Management: Opens or closes common applications like Notepad, Calculator, VLC Media Player, etc. Locks the computer, restarts, or shuts it down on command. Supports toggling system settings like Wi-Fi and Bluetooth.
6. Object Detection (Computer Vision): Uses OpenCV for camera-based operations. Detects and captures photos using the system's webcam. Placeholder for further object detection tasks (ready for future AI/ML integrations).
7. Task Scheduling: Allows users to create, display, and clear daily tasks. Maintains task lists in a text file for easy tracking.
8. Fun and Entertainment: Plays local music or streams songs from YouTube. Flips a coin and plays games like Rock-Paper-Scissors. Tells jokes, fun facts, inspirational quotes, and bedtime stories.
9. Device and System Control: Adjusts volume, brightness, and other system settings. Manages playback in media players (play, pause, mute/unmute). Takes screenshots and saves them with unique names. Sets alarms and reminds users of important events.
10. System Monitoring: Reports battery status, CPU usage, and other system details. Displays public IP address and network connectivity status.
11. Automation Tools: Sends emails via Gmail SMTP. Automates WhatsApp messages, voice calls, and video calls (partially implemented). Opens system utilities like Task Manager, Control Panel, and File Explorer.
12. Location and Maps: Tracks the user's location using IP-based geolocation. Searches specific locations on Google Maps.
13. Dictionary and Translation: Provides word definitions and translations. Suggests closely related words if the user input is unclear.
14. Object and Task Recognition (Advanced Capabilities): Supports clipboard-based text-to-speech conversion. Future-ready for advanced AI tasks like object detection and data processing.
15. Error Handling: Provides friendly responses for invalid or unrecognized commands. Offers alternatives or retry options for failed tasks.
16. Chatbot Mode : Uses HuggingChat for AI-powered conversational assistance. Designed to handle questions beyond the pre-coded responses.
17. File Operations and Database Integration: Manages SQLite databases for storing user-related information (e.g., tasks, contacts). Reads and writes data to/from external files for persistent storage.
18.  Alerts users about system activities like updates, alarms, or scheduled tasks.
19. Customization and Extensibility: Fully modular design, allowing easy addition of new features (e.g., ML models). Flexible and adaptable code for future scaling.
20. News and Weather Updates: Retrieves the latest news headlines by category (business, health, sports, etc.) using News API. Provides weather forecasts for any location via OpenWeatherMap API.
---
### 🛠️ Tech Stack
- **Backend**: Python
- **AI/ML**: YOLOv5 (Object Detection), NLP (Natural Language Processing)
- **Libraries**:  
  - **SpeechRecognition** (for voice recognition)
  - **pyttsx3** (for text-to-speech conversion)
  - **OpenCV** (for webcam-based object detection)
  - **YOLOv5** (for real-time object detection)
  - **HuggingFace Transformers** (for NLP-based tasks)
  - **SQLite** (for storing contacts and user-related data)
  - **Requests** (for retrieving weather, news, etc. via APIs)
- **IDE**: Visual Studio Code or PyCharm
- **APIs**:  
  - OpenWeatherMap (for weather updates)
  - News API (for news updates)
  - Gmail API (for sending emails)  
  - WhatsApp API (for sending messages)
  --- 
### 🚀How to Run

### 1. Clone the Repository
First, clone the repository to your local machine using the following command:


git clone https://github.com/partha-09/VenomX-Windows-Voice-Assistant.git


### 2. Install Dependencies
Ensure that you have Python installed on your machine. Then, install the required dependencies by running:




### 3. Configure the Database
VenomX uses an SQLite database (`venomx.db`) to store contacts for WhatsApp messaging functionality.

- Open the `venomx.db` file located in the repository folder.
- Add and configure the contacts for WhatsApp (or any other messaging system you're using) as per your requirements. You can use a SQLite browser or any other method to edit the database.

### 4. Run the Project
To run VenomX, navigate to the folder where the repository is cloned and execute the main script `VenomX.py`. This will launch the voice assistant.


python VenomX.py


### 5. Start Using the Assistant
Once the script is running, speak the desired commands, and VenomX will help you with various tasks, such as object detection, messaging, and system control. Simply follow the prompts and enjoy the full experience of VenomX.

---

### Project Structure

- **VenomX.py**: This is the main file that runs the voice assistant. It listens for voice commands, processes them, and calls the appropriate functions for tasks like messaging, object detection, etc.
- **venomx.db**: The SQLite database that stores WhatsApp contacts and other relevant information.
- **requirements.txt**: A file that lists all the Python libraries required to run VenomX. You can install them by running the `pip install -r requirements.txt` command.

📌 **Topics**
- python-project
- ai-voice-assistant
- yolo-object-detection
- speech-recognition
- voice-command-assistant
- real-time-detection
---
🏆 **Recognition**
1. **First Prize** at the **College-Level Project Exhibition** at Hirasugar Institute of Technology.
2. **Best Project of the Year 2024** at the ** Annual State-Level Project Exhibition**,held in Kalaburagi in August 2024 by the Karnataka State Council for Science and Technology.
  - **KSCST CERTIFICATE**
   ![image alt](https://github.com/partha-09/VenomX-Windows-Voice-Assistant/blob/3d5c4baf9e20254ef2c30a73fa5f77c05b2553f2/KSCST.jpg)
---
### 📬 Contact:

For any queries:

- **Name**: Siddappa Godi
- **Email**: [siddapp2godi@gmail.com](mailto:siddapp2godi@gmail.com)
- **Phone**: +91 6363504679
- **LinkedIn**: [https://www.linkedin.com/in/siddappagodi/](https://www.linkedin.com/in/siddappagodi/)

---
## ⭐ Contribute

I welcome contributions to improve this project! If you find this project helpful or see any areas for enhancement, feel free to:

- **Fork** this repository.
- **Submit a Pull Request** with improvements or new features.
- **Open an Issue** if you encounter any bugs or have suggestions for better functionality.

Your contributions are greatly appreciated and will help make this project even better. Don't hesitate to reach out for any queries or collaboration ideas!

