# 💻 Rinix AI Assistant

A desktop AI assistant built with Python, PyQt5, voice recognition, text-to-speech, web automation, and AI-powered chat. It provides a graphical interface for voice and typed commands, including search, media playback, app automation, and placeholder image generation.

## 🚀 What this project includes

- A modern PyQt5 GUI interface with dark theme, typed command input, voice controls, and a fullscreen voice-only quick-chat popup.
- Voice command support using `SpeechRecognition`.
- Text-to-speech output using `edge-tts` and `pygame`.
- AI chat responses via the `groq` client.
- Real-time web search summarization using Google search and BeautifulSoup.
- Automation support for opening/closing apps, searching web, playing YouTube, and camera capture.
- A spot for image generation integration using a prompt-based API.

## 🛠️ Installation

1. Clone the repository.
2. Open a terminal in the project root directory.
3. Create a Python virtual environment:
   - PowerShell: `python -m venv myenv`
   - Command Prompt: `python -m venv myenv`
4. Activate the virtual environment:
   - PowerShell: `myenv\Scripts\Activate.ps1`
   - Command Prompt: `myenv\Scripts\activate.bat`
5. Upgrade pip and install dependencies:
   - `python -m pip install --upgrade pip`
   - `pip install -r requirements.txt`

## 💬 Quick Chat Popup

If you want a compact chat window, click the **Quick Chat** button in the main app.
The quick chat window opens as a smaller pop-up and supports typed commands just like the main interface.
You can also use voice by clicking the "Voice" button inside the popup.

## ⚙️ Configuration

- Copy or create a `.env` file in the project root if you want to customize:
  - `Username` — name displayed for the user.
  - `Assistantname` — assistant name shown in the UI.
  - `GROQ_API_KEY` — API key used by the AI chatbot.

Example `.env`:

```env
Username=YourName
Assistantname=Rinix
GROQ_API_KEY=your_api_key_here
```

## ▶️ Running the assistant

From the project root with the virtual environment active:

```powershell
python Main.py
```

## 💡 Notes

- `requirements.txt` is the single source of dependency installation.
- For Python 3.14, `pygame-ce` is used instead of `pygame`.
- The image generation feature is currently a placeholder and can be integrated with an API such as DALL·E.
- Some automation features depend on third-party packages such as `AppOpener`, `pywhatkit`, and `googlesearch-python`.

## 📌 Helpful commands

- Install dependencies: `pip install -r requirements.txt`
- Run the app: `python Main.py`
- Update the env file: edit `.env`

## 🤝 Contributing

Feel free to add more automation commands, improve the assistant's decision model, or integrate actual image generation and AI services.

## 👨‍💻 Author

### Rishiraj

* **Gmail:** rishirajrjs6@gmail.com  
* **GitHub:** [@RishirajDeveloper](https://github.com/RishirajDeveloper)
* [@PORTFOLIO](https://rishiraj-singh.vercel.app/)
