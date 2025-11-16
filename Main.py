from Frontend.GUI import JarvisGUI, GraphicalUserInterface
from Backend.Model import FirstLayerDMM
from Backend.RealtimeSearchEngine import RealtimeSearchEngine
from Backend.Automation import Automation
from Backend.SpeechToText import SpeechRecognition
from Backend.Chatbot import ChatBot
from Backend.TextToSpeech import speak
from Backend.ImageGeneration import ImageGeneration
from dotenv import dotenv_values
import threading
import json
import os

env_vars = dotenv_values(".env")
Username = env_vars.get("Username", "Rishiraj")
Assistantname = env_vars.get("Assistantname", "Rinix")

class JarvisApp:
    def __init__(self):
        self.gui = None
        self.is_listening = False

    def initialize_gui(self):
        """Initialize the GUI in a separate thread"""
        self.gui = JarvisGUI(process_callback=self.process_query)
        self.gui.listen_button.clicked.connect(self.toggle_listening)
        self.gui.show()

    def toggle_listening(self):
        """Toggle listening state"""
        self.is_listening = not self.is_listening
        if self.is_listening:
            self.gui.update_status("Listening...")
            # Start listening thread
            threading.Thread(target=self.listen_and_process, daemon=True).start()
        else:
            self.gui.update_status("Ready")

    def listen_and_process(self):
        """Continuously listen for voice commands and process them while listening is enabled"""
        while self.is_listening:
            try:
                self.gui.update_status("Listening...")
                query = SpeechRecognition()

                if query:
                    self.gui.add_message(f"{Username}: {query}")
                    self.gui.update_status("Processing...")

                    # Process the query
                    response = self.process_query(query)
                    self.gui.add_message(f"{Assistantname}: {response}")
                    self.gui.update_status("Listening...")

                    # Speak the response
                    speak(response)
                else:
                    # Continue listening if no query detected
                    continue
            except Exception as e:
                self.gui.add_message(f"Error: {str(e)}")
                self.gui.update_status("Listening...")
                continue

    def process_query(self, query):
        """Process the user's query and return appropriate response"""
        try:
            # Get decision from model
            decisions = FirstLayerDMM(query)

            for decision in decisions:
                if decision.startswith("general"):
                    # General conversation
                    query_text = decision.replace("general ", "")
                    return ChatBot(query_text)

                elif decision.startswith("realtime"):
                    # Real-time search
                    query_text = decision.replace("realtime ", "")
                    return RealtimeSearchEngine(query_text)

                elif "generate image" in decision:
                    # Image generation
                    prompt = decision.replace("generate image ", "")
                    return ImageGeneration(prompt)

                elif any(keyword in decision for keyword in ["open", "close", "play", "search", "camera", "photo"]):
                    # Automation tasks
                    Automation([decision])
                    return f"Executed: {decision}"

            return "I'm not sure how to handle that request."

        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"

def main():
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    jarvis = JarvisApp()
    jarvis.initialize_gui()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
