import time
from utils.notifier import Notifier
from utils.logger import Logger

class PomodoroTimer:
    def __init__(self, config, history, update_callback=None, sound_path=None, task=None):
        """
        Initialize the PomodoroTimer with the given configuration and dependencies.

        :param config: An instance of the Config class containing timer settings.
        :param history: An instance of the History class to log completed sessions.
        :param update_callback: A callback function to update the GUI with the remaining time.
        :param sound_path: Path to a custom sound file for notifications.
        :param task: The task description for the current Pomodoro session.
        """
        self.config = config
        self.history = history
        self.notifier = Notifier(sound_path)
        self.logger = Logger()
        self.update_callback = update_callback
        self.paused = False
        self.task = task

    def start(self):
        """
        Start the Pomodoro timer, alternating between work sessions and breaks.
        """
        for _ in range(self.config.sessions):
            if self._start_session() == 'break':
                break
            if self._start_break(self.config.short_break) == 'break':
                break
        if not self.paused:
            self._start_break(self.config.long_break)
        self.history.save()

    def _start_session(self):
        """
        Start a work session and log it to history.

        :return: 'break' if the timer is paused, otherwise None.
        """
        self.logger.log("Starting work session.")
        self.history.add_session({"task": self.task, "duration": self.config.work})
        return self._countdown(self.config.work * 60, "Work session completed!")

    def _start_break(self, break_length):
        """
        Start a break session.

        :param break_length: Length of the break in minutes.
        :return: 'break' if the timer is paused, otherwise None.
        """
        self.logger.log("Starting break.")
        return self._countdown(break_length * 60, "Break time over!")

    def _countdown(self, seconds, message):
        """
        Countdown for the specified number of seconds, updating the GUI and notifying the user when done.

        :param seconds: The number of seconds for the countdown.
        :param message: The notification message to be displayed when the countdown ends.
        :return: 'break' if the timer is paused, otherwise None.
        """
        while seconds:
            if self.paused:
                return 'break'
            if self.update_callback:
                self.update_callback(seconds)
            mins, secs = divmod(seconds, 60)
            time.sleep(1)
            seconds -= 1
        self.notifier.notify(message)

    def pause(self):
        """
        Pause the Pomodoro timer.
        """
        self.paused = True
        self.logger.log("Timer paused.")
