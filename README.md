
# ⏰ Pomodoro Timer

A robust and flexible Pomodoro Timer to help users with time management. This application includes a graphical user interface for easier interaction and customizable features.

## 🌟 Features

- Customizable session lengths for work and breaks 🕒
- Break reminders with optional sound notifications 🔔
- History of completed sessions 📜
- Task management for each Pomodoro session 📝
- Session statistics 📊

## 🛠️ Technologies Used

- **Frontend**: Tkinter (Python standard library)
- **Backend**: Python
- **Libraries**: `click`, `pygame`, `pync`

## 📝 Setup Instructions

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/obadaKraishan/PomodoroTimer.git
cd PomodoroTimer
```

### 2. Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scriptsctivate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Start the Pomodoro Timer application by running the following command:

```bash
python main.py
```

## 📂 Project Structure

```
pomodoro_timer/
│
├── README.md                      # Project documentation
├── requirements.txt               # List of dependencies
├── setup.py                       # Setup configuration
├── main.py                        # Main entry point for the application
│
├── pomodoro/
│   ├── __init__.py
│   ├── config.py                  # Configuration settings for the timer
│   ├── history.py                 # Logic for handling session history
│   ├── timer.py                   # Core timer functionality
│   ├── gui.py                     # Graphical User Interface logic
│
├── tests/
│   ├── __init__.py
│   ├── test_config.py             # Tests for configuration settings
│   ├── test_history.py            # Tests for session history
│   ├── test_timer.py              # Tests for timer functionality
│
└── utils/
    ├── __init__.py
    ├── logger.py                  # Logging functionality
    ├── notifier.py                # Notification functionality
    └── alarm_sound.mp3            # Default alarm sound (if any)
```

## 🎨 Customization

### 1. Update GUI Elements

Customize the GUI elements in `gui.py` to fit your needs.

### 2. Modify Timer Parameters

Modify the timer parameters in `config.py` or use the GUI to change the input and output paths, as well as the theme.

## 📄 License

This project is developed by Obada Kraishan. If you have any questions or need further information, feel free to contact me at obada.kraishan@gmail.com.

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Contributors

- [Obada Kraishan](https://github.com/obadaKraishan)
