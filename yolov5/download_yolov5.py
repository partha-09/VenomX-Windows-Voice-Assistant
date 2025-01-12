import cv2
import torch
import pyttsx3
import numpy as np
import speech_recognition as sr
from threading import Thread

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the properties for the speech
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)   # Volume (0.0 to 1.0)

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Initialize the recognizer
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Global flag to stop the process
stop_flag = False

def listen_for_exit():
    global stop_flag
    while not stop_flag:
        try:
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening for 'exit' command...")
                audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            if "exit" in command:
                stop_flag = True
                break
        except sr.UnknownValueError:
            pass  # Ignore unrecognized speech

# Function to perform object detection
def detect_objects(image):
    results = model(image)
    return results

# Function to draw bounding boxes on the image and record detected object names
def draw_boxes(image, results):
    labels, coords = results.xyxyn[0][:, -1].numpy(), results.xyxyn[0][:, :-1].numpy()
    n = len(labels)
    detected_objects = set()
    for i in range(n):
        row = coords[i]
        if row[4] >= 0.5:  # Confidence threshold
            x1, y1, x2, y2 = int(row[0] * image.shape[1]), int(row[1] * image.shape[0]), int(row[2] * image.shape[1]), int(row[3] * image.shape[0])
            bgr = (0, 255, 0)  # Bounding box color
            cv2.rectangle(image, (x1, y1), (x2, y2), bgr, 2)
            label = model.names[int(labels[i])]
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, bgr, 2)
            detected_objects.add(label)
    return image, detected_objects

# Function to capture and process frames from the webcam
def process_frames():
    global stop_flag

    # Open the webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    last_spoken_objects = set()  # Track last spoken objects to prevent repetition

    while not stop_flag:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Could not read frame.")
            break
        
        # Perform object detection
        results = detect_objects(frame)
        
        # Draw bounding boxes and get detected object names
        frame_with_boxes, detected_objects = draw_boxes(frame, results)
        
        # Announce detected objects
        if detected_objects != last_spoken_objects:
            if detected_objects:
                objects_str = ', '.join(detected_objects)
                print(f"I see the following objects: {objects_str}")
                engine.say(f"I see the following objects: {objects_str}")
                engine.runAndWait()
                last_spoken_objects = detected_objects.copy()
            else:
                print("I don't see any recognizable objects.")
        
        # Display the result
        cv2.imshow('Detected Objects', frame_with_boxes)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()

# Main function for interaction
def main():
    listener_thread = Thread(target=listen_for_exit)
    listener_thread.start()
    process_frames()
    listener_thread.join()

if __name__ == "__main__":
    main()
