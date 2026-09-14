# AI Auto Reply Bot 🤖

A Python-based AI auto-reply bot that reads chat conversations, uses **Google Gemini** to generate natural replies, and automates the typing process using **PyAutoGUI** and the system clipboard.

The project is built with a modular structure, keeping Gemini AI, clipboard handling, mouse automation, and chat processing in separate files.

---

## ✨ Features

* 🤖 Google Gemini AI integration
* 💬 Generates natural conversational replies
* 📋 Reads chat text using the clipboard
* 🖱️ Mouse and keyboard automation with PyAutoGUI
* ⌨️ Automatically clicks the message box
* 📎 Pastes generated replies
* 📤 Sends replies automatically
* 🧩 Modular Python architecture
* ⚡ Simple and lightweight design

---

## 🏗️ Project Structure

```text
AI-Auto-Reply-Bot/
│
├── main.py
├── config.py
├── gemini_module.py
├── clipboard_module.py
├── chat_module.py
├── mouse_module.py
├── get_coordinates.py
│
└── requirements.txt
```

---

## 🔄 How It Works

The bot follows this basic workflow:

```text
             💬 Chat Conversation
                     │
                     ▼
               Mouse Selection
                     │
                     ▼
              Copy to Clipboard
                     │
                     ▼
             clipboard_module.py
                     │
                     ▼
               chat_module.py
                     │
                     ▼
              Gemini AI
                     │
                     ▼
              Generated Reply
                     │
                     ▼
             Copy Reply
                     │
                     ▼
             Message Box
                     │
                     ▼
                 Paste
                     │
                     ▼
                  Send
```

---

## 🧩 Modules

### `main.py`

The main entry point of the application.

It starts the bot and continuously runs the reply-generation process.

---

### `config.py`

Stores configuration values such as the Gemini API key and model name.

Example:

```python
API_KEY = "YOUR_GEMINI_API_KEY"

GEMINI_MODEL = "gemini-3.8-flash"
```

---

### `gemini_module.py`

Handles communication with Google Gemini.

It receives the copied chat history and asks Gemini to generate a short, natural reply.

The AI prompt is designed to:

* Match the conversation's tone
* Keep replies conversational
* Avoid unnecessary explanations
* Return only the message that should be sent

---

### `clipboard_module.py`

Handles clipboard operations.

It provides functions for:

* Reading copied chat text
* Copying generated replies

---

### `chat_module.py`

Coordinates the main reply workflow.

It:

1. Selects the chat
2. Copies the conversation
3. Reads the clipboard
4. Sends the conversation to Gemini
5. Receives the generated reply
6. Copies the reply
7. Clicks the message box
8. Pastes the reply
9. Sends the message

---

### `mouse_module.py`

Handles PyAutoGUI mouse and keyboard automation.

It contains coordinates for:

```python
BROWSER_ICON
CHAT_START
CHAT_END
MESSAGE_BOX
```

These coordinates are specific to the screen layout being automated and may need to be adjusted on another computer or screen resolution.

---

### `get_coordinates.py`

A small utility for finding mouse coordinates.

Run:

```bash
python get_coordinates.py
```

Move the mouse around the screen to identify the required X and Y coordinates.

---

---

## 🛠️ Requirements

* Python 3.x
* Windows
* Google Gemini API key
* Internet connection
* A chat interface that can be controlled using mouse and keyboard input

### Python Packages

```text
google-genai
pyautogui
pyperclip
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Auto-Reply-Bot.git
```

Enter the project directory:

```bash
cd AI-Auto-Reply-Bot
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Gemini API Key

This project uses Google Gemini to generate replies.

Add your own Gemini API key to the configuration.

Example:

```python
API_KEY = "YOUR_GEMINI_API_KEY"
```

---

## 📍 Setting Mouse Coordinates

The bot uses PyAutoGUI coordinates to interact with the chat interface.

Edit:

```text
mouse_module.py
```

and set:

```python
BROWSER_ICON = (X, Y)

CHAT_START = (X, Y)

CHAT_END = (X, Y)

MESSAGE_BOX = (X, Y)
```

The coordinates depend on your screen resolution and the position of the chat interface.

Use:

```bash
python get_coordinates.py
```

to find your coordinates.

---

---

## ▶️ Running the Bot

After configuring your Gemini API key and mouse coordinates:

```bash
python main.py
```

The bot will:

```text
Read chat
   ↓
Copy conversation
   ↓
Send conversation to Gemini
   ↓
Generate reply
   ↓
Copy reply
   ↓
Click message box
   ↓
Paste reply
   ↓
Send
```

---

## ⚠️ Important Notes

This project relies on **screen coordinates** for automation.

Therefore, changing any of the following may require updating the coordinates:

* Screen resolution
* Display scaling
* Browser window position
* Browser zoom
* Chat interface layout

The bot is intended primarily as a **personal automation and programming project**.

Use automation responsibly and make sure it complies with the rules of the platform or chat service you use it with.

---

## 🚀 Future Improvements

Possible future improvements include:

* 🎯 More reliable chat detection
* 🧠 Conversation context management
* 🔄 Better handling of new messages
* ⏱️ Improved timing and retry logic
* 🛡️ Safer API-key management
* 🖥️ Configuration through a GUI
* 📱 Support for different chat platforms
* 🔧 More robust automation without fixed coordinates

---

## 📚 Technologies Used

| Technology     | Purpose                       |
| -------------- | ----------------------------- |
| Python         | Core programming language     |
| Google Gemini  | AI reply generation           |
| `google-genai` | Gemini API integration        |
| PyAutoGUI      | Mouse and keyboard automation |
| Pyperclip      | Clipboard operations          |

---

## 📄 License

This project is available for personal learning, experimentation, and development.

---

## 👨‍💻 Author

**Akhilesh Sharma**

Built with Python and Google Gemini.

---

⭐ If you find this project interesting, feel free to star the repository!
