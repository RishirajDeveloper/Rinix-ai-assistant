import os
import subprocess
import pywhatkit as kit
import time
from googlesearch import search
import webbrowser
import AppOpener

try:
    import cv2
except ImportError:
    cv2 = None

def Automation(commands):
    """
    Executes automation tasks based on the given commands.
    """
    for command in commands:
        if "open" in command:
            app_name = command.replace("open ", "").strip()
            try:
                AppOpener.open(app_name, match_closest=True)
                print(f"Opened {app_name}")
            except Exception as e:
                print(f"Could not open {app_name}: {e}")

        elif "close" in command:
            app_name = command.replace("close ", "").strip()
            try:
                AppOpener.close(app_name, match_closest=True)
                print(f"Closed {app_name}")
            except Exception as e:
                print(f"Could not close {app_name}: {e}")

        elif "play" in command:
            song = command.replace("play ", "").strip()
            kit.playonyt(song)
            print(f"Playing {song} on YouTube")

        elif "search" in command:
            query = command.replace("search ", "").strip()
            if "google" in command:
                kit.search(query)
            elif "youtube" in command:
                kit.playonyt(query)
            else:
                # General web search
                for result in search(query, num_results=5):
                    print(result)

        elif "camera" in command or "photo" in command:
            take_photos()

        elif "generate image" in command or "generate" in command:
            # This would require an image generation API
            print("Image generation feature not implemented yet. Please use an external service.")

def take_photos(num_photos=5):
    """
    Opens camera and takes specified number of photos.
    """
    if cv2 is None:
        print("OpenCV not available. Cannot take photos.")
        return

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open camera")
        return

    photo_count = 0
    while photo_count < num_photos:
        ret, frame = cap.read()
        if ret:
            filename = f"Data/photo_{photo_count + 1}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Took photo {photo_count + 1}")
            photo_count += 1
            time.sleep(1)  # Wait 1 second between photos
        else:
            print("Failed to capture photo")
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"Took {photo_count} photos")
