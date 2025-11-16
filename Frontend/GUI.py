import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QFrame, QLineEdit, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QFont, QPalette, QColor, QPixmap, QIcon, QMovie
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
Assistantname = env_vars.get("Assistantname", "Rinix")


class JarvisGUI(QWidget):
    def __init__(self, process_callback=None):
        super().__init__()
        self.process_callback = process_callback
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Rinix AI Assistant')
        self.setGeometry(100, 100, 800, 600)

        # Set dark theme with gradient background
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(30, 30, 30))
        palette.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(palette)
        self.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c2c2c, stop:1 #1a1a1a);")

        layout = QVBoxLayout()

        # Logo/Animation
        self.logo_label = QLabel()
        graphics_path = os.path.join(os.path.dirname(__file__), 'Graphics', 'Rinix.gif')
        if os.path.exists(graphics_path):
            self.movie = QMovie(graphics_path)
            self.logo_label.setMovie(self.movie)
            self.movie.start()
        else:
            # Fallback to static image
            static_path = os.path.join(os.path.dirname(__file__), 'Graphics', 'Jarvis.png')
            if os.path.exists(static_path):
                pixmap = QPixmap(static_path)
                self.logo_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
        self.logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.logo_label)

        # Title
        title = QLabel('RINIX AI ASSISTANT')
        title.setFont(QFont('Arial', 24, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #00ff00; margin: 10px;")
        layout.addWidget(title)

        # Status display
        self.status_label = QLabel('Status: Ready')
        self.status_label.setFont(QFont('Arial', 14))
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: #ffff00; margin: 5px;")
        layout.addWidget(self.status_label)

        # Chat display
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QFont('Arial', 12))
        self.chat_display.setStyleSheet("background-color: #2d2d2d; color: white; border: 2px solid #555; border-radius: 10px; padding: 5px;")
        layout.addWidget(self.chat_display)

        # Input field
        self.input_field = QLineEdit()
        self.input_field.setFont(QFont('Arial', 12))
        self.input_field.setStyleSheet("background-color: #3d3d3d; color: white; border: 2px solid #555; border-radius: 10px; padding: 5px;")
        self.input_field.setPlaceholderText("Type your command here...")
        self.input_field.returnPressed.connect(self.send_message)
        layout.addWidget(self.input_field)

        # Button layout
        button_layout = QHBoxLayout()

        # Home button
        self.home_button = QPushButton()
        self.home_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
            }
            QPushButton:hover {
                background-color: #555;
                border-radius: 5px;
            }
        """)
        home_path = os.path.join(os.path.dirname(__file__), 'Graphics', 'Home.png')
        if os.path.exists(home_path):
            self.home_button.setIcon(QIcon(home_path))
            self.home_button.setIconSize(self.home_button.sizeHint() * 0.8)
        self.home_button.setToolTip('Go to Home')
        self.home_button.clicked.connect(self.go_home)
        button_layout.addWidget(self.home_button)

        # Settings button
        self.settings_button = QPushButton()
        self.settings_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
            }
            QPushButton:hover {
                background-color: #555;
                border-radius: 5px;
            }
        """)
        setting_path = os.path.join(os.path.dirname(__file__), 'Graphics', 'Setting.png')
        if os.path.exists(setting_path):
            self.settings_button.setIcon(QIcon(setting_path))
            self.settings_button.setIconSize(self.settings_button.sizeHint() * 0.8)
        self.settings_button.setToolTip('Open Settings')
        self.settings_button.clicked.connect(self.open_settings)
        button_layout.addWidget(self.settings_button)

        button_layout.addStretch()

        self.listen_button = QPushButton('Start Listening')
        self.listen_button.setFont(QFont('Arial', 14))
        self.listen_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border-radius: 10px;
                border: 2px solid #4CAF50;
            }
            QPushButton:hover {
                background-color: #45a049;
                border: 2px solid #45a049;
            }
            QPushButton:pressed {
                background-color: #3e8e41;
            }
        """)
        # Add icon to listen button
        mic_on_path = os.path.join(os.path.dirname(__file__), 'Graphics', 'MIc_on.png')
        if os.path.exists(mic_on_path):
            self.listen_button.setIcon(QIcon(mic_on_path))
            self.listen_button.setIconSize(self.listen_button.sizeHint() * 0.5)
        self.listen_button.setToolTip('Click to start/stop voice listening')
        self.listen_button.clicked.connect(self.toggle_listening)
        button_layout.addWidget(self.listen_button)

        self.clear_button = QPushButton('Clear Chat')
        self.clear_button.setFont(QFont('Arial', 14))
        self.clear_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                padding: 10px;
                border-radius: 10px;
                border: 2px solid #f44336;
            }
            QPushButton:hover {
                background-color: #da190b;
                border: 2px solid #da190b;
            }
            QPushButton:pressed {
                background-color: #b71c1c;
            }
        """)
        # Add icon to clear button
        close_path = os.path.join(os.path.dirname(__file__), 'Graphics', 'Close.png')
        if os.path.exists(close_path):
            self.clear_button.setIcon(QIcon(close_path))
            self.clear_button.setIconSize(self.clear_button.sizeHint() * 0.5)
        self.clear_button.setToolTip('Clear the chat history')
        self.clear_button.clicked.connect(self.clear_chat)
        button_layout.addWidget(self.clear_button)

        layout.addLayout(button_layout)

        # Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)

        # Instructions
        instructions = QLabel('Commands: "open [app]", "play [song]", "search [query]", "take photo", etc.')
        instructions.setFont(QFont('Arial', 10))
        instructions.setAlignment(Qt.AlignCenter)
        instructions.setStyleSheet("color: #aaa;")
        layout.addWidget(instructions)

        self.setLayout(layout)
        self.is_listening = False

    def toggle_listening(self):
        self.is_listening = not self.is_listening
        if self.is_listening:
            self.listen_button.setText('Stop Listening')
            self.listen_button.setStyleSheet("""
                QPushButton {
                    background-color: #f44336;
                    color: white;
                    padding: 10px;
                    border-radius: 10px;
                    border: 2px solid #f44336;
                }
                QPushButton:hover {
                    background-color: #da190b;
                    border: 2px solid #da190b;
                }
                QPushButton:pressed {
                    background-color: #b71c1c;
                }
            """)
            # Change icon to mic_off
            mic_off_path = os.path.join(os.path.dirname(__file__), 'Graphics', 'Mic_off.png')
            if os.path.exists(mic_off_path):
                self.listen_button.setIcon(QIcon(mic_off_path))
            self.status_label.setText('Status: Listening...')
        else:
            self.listen_button.setText('Start Listening')
            self.listen_button.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px;
                    border-radius: 10px;
                    border: 2px solid #4CAF50;
                }
                QPushButton:hover {
                    background-color: #45a049;
                    border: 2px solid #45a049;
                }
                QPushButton:pressed {
                    background-color: #3e8e41;
                }
            """)
            # Change icon back to mic_on
            mic_on_path = os.path.join(os.path.dirname(__file__), 'Graphics', 'MIc_on.png')
            if os.path.exists(mic_on_path):
                self.listen_button.setIcon(QIcon(mic_on_path))
            self.status_label.setText('Status: Ready')

    def update_status(self, status):
        self.status_label.setText(f'Status: {status}')

    def add_message(self, message):
        from datetime import datetime
        timestamp = datetime.now().strftime('%H:%M:%S')
        formatted_message = f"[{timestamp}] {message}"
        self.chat_display.append(formatted_message)
        # Auto-scroll to bottom
        cursor = self.chat_display.textCursor()
        cursor.movePosition(cursor.End)
        self.chat_display.setTextCursor(cursor)

    def clear_chat(self):
        self.chat_display.clear()

    def send_message(self):
        message = self.input_field.text().strip()
        if message:
            self.add_message(f"You: {message}")
            self.input_field.clear()
            # Process the message using the callback if available
            if self.process_callback:
                try:
                    response = self.process_callback(message)
                    self.add_message(f"{Assistantname}: {response}")
                except Exception as e:
                    self.add_message(f"Error: {str(e)}")
            else:
                # Fallback: just echo back
                self.add_message(f"Rinix: Processing '{message}'")

    def go_home(self):
        self.add_message("Rinix: Going to Home screen")

    def open_settings(self):
        self.add_message("Rinix: Opening Settings")


def GraphicalUserInterface():
    app = QApplication(sys.argv)
    gui = JarvisGUI()
    gui.show()
    sys.exit(app.exec_())
