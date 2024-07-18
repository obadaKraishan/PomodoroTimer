import unittest
from pomodoro.config import Config

class TestConfig(unittest.TestCase):
    def test_initialization(self):
        config = Config(25, 5, 15, 4)
        self.assertEqual(config.work, 25)
        self.assertEqual(config.short_break, 5)
        self.assertEqual(config.long_break, 15)
        self.assertEqual(config.sessions, 4)

if __name__ == '__main__':
    unittest.main()
