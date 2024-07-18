import unittest
from pomodoro.history import History

class TestHistory(unittest.TestCase):
    def test_initialization(self):
        history = History()
        self.assertEqual(history.filename, 'history.json')
        self.assertEqual(history.data, [])

if __name__ == '__main__':
    unittest.main()
