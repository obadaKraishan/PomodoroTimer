import unittest
from pomodoro.timer import PomodoroTimer
from pomodoro.config import Config
from pomodoro.history import History

class TestPomodoroTimer(unittest.TestCase):
    def test_initialization(self):
        config = Config(25, 5, 15, 4)
        history = History()
        timer = PomodoroTimer(config, history)
        self.assertEqual(timer.config.work, 25)
        self.assertEqual(timer.config.short_break, 5)
        self.assertEqual(timer.config.long_break, 15)
        self.assertEqual(timer.config.sessions, 4)

if __name__ == '__main__':
    unittest.main()
