import logging

class Logger:
    def __init__(self, filename='pomodoro.log'):
        logging.basicConfig(filename=filename, level=logging.INFO)

    def log(self, message):
        logging.info(message)
