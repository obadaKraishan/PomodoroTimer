import tkinter as tk
from tkinter import messagebox, filedialog
from pomodoro.timer import PomodoroTimer
from pomodoro.config import Config
from pomodoro.history import History
from threading import Thread

class PomodoroApp:
    def __init__(self, master):
        """
        Initialize the PomodoroApp with the given master widget.

        :param master: The root window of the Tkinter application.
        """
        self.master = master
        self.master.title("Pomodoro Timer")

        # Variables to hold user input for work, short break, long break, and sessions durations
        self.work_var = tk.IntVar(value=25)
        self.short_break_var = tk.IntVar(value=5)
        self.long_break_var = tk.IntVar(value=15)
        self.sessions_var = tk.IntVar(value=4)
        self.sound_path = None
        self.running = False

        # Initialize the history of sessions
        self.history = History()

        # Create and place input fields and labels in the GUI
        tk.Label(master, text="Work (min)").grid(row=0, column=0)
        tk.Entry(master, textvariable=self.work_var).grid(row=0, column=1)

        tk.Label(master, text="Short Break (min)").grid(row=1, column=0)
        tk.Entry(master, textvariable=self.short_break_var).grid(row=1, column=1)

        tk.Label(master, text="Long Break (min)").grid(row=2, column=0)
        tk.Entry(master, textvariable=self.long_break_var).grid(row=2, column=1)

        tk.Label(master, text="Sessions").grid(row=3, column=0)
        tk.Entry(master, textvariable=self.sessions_var).grid(row=3, column=1)

        tk.Label(master, text="Task").grid(row=4, column=0)
        self.task_var = tk.StringVar()
        tk.Entry(master, textvariable=self.task_var).grid(row=4, column=1)

        # Label to display the timer countdown
        self.timer_label = tk.Label(master, text="00:00", font=("Helvetica", 48))
        self.timer_label.grid(row=5, column=0, columnspan=2)

        # Start button to begin the Pomodoro timer
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.grid(row=6, column=0, columnspan=2)

        # Pause button to pause the Pomodoro timer
        self.pause_button = tk.Button(master, text="Pause", command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.grid(row=7, column=0, columnspan=2)

        # Button to choose a custom sound for notifications
        self.sound_button = tk.Button(master, text="Choose Sound", command=self.choose_sound)
        self.sound_button.grid(row=8, column=0, columnspan=2)

        # Button to show statistics of completed sessions
        self.stats_button = tk.Button(master, text="Show Stats", command=self.show_stats)
        self.stats_button.grid(row=9, column=0, columnspan=2)

    def start_timer(self):
        """
        Start the Pomodoro timer using the user-provided configuration.
        """
        if self.running:
            return
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)

        # Create the configuration and start the Pomodoro timer in a new thread
        config = Config(self.work_var.get(), self.short_break_var.get(), self.long_break_var.get(), self.sessions_var.get())
        self.timer = PomodoroTimer(config, self.history, self.update_timer, self.sound_path, self.task_var.get())
        self.timer_thread = Thread(target=self.timer.start)
        self.timer_thread.start()

    def pause_timer(self):
        """
        Pause the Pomodoro timer.
        """
        if not self.running:
            return
        self.running = False
        self.timer.pause()
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)

    def update_timer(self, time_remaining):
        """
        Update the timer label with the remaining time.

        :param time_remaining: The remaining time in seconds.
        """
        mins, secs = divmod(time_remaining, 60)
        self.timer_label.config(text=f"{mins:02d}:{secs:02d}")
        if time_remaining == 0:
            self.running = False
            self.start_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
            messagebox.showinfo("Pomodoro Timer", "Time's up!")

    def choose_sound(self):
        """
        Open a file dialog to choose a custom sound file for notifications.
        """
        self.sound_path = filedialog.askopenfilename(title="Choose Sound File", filetypes=[("MP3 files", "*.mp3"), ("All files", "*.*")])

    def show_stats(self):
        """
        Show the statistics of completed Pomodoro sessions.
        """
        total_sessions = len(self.history.data)
        total_time = sum(session['duration'] for session in self.history.data)
        stats_message = f"Total Sessions: {total_sessions}\nTotal Time: {total_time} minutes"
        messagebox.showinfo("Pomodoro Stats", stats_message)
