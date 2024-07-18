import pync
import pygame

class Notifier:
    def __init__(self, sound_path=None):
        pygame.mixer.init()
        self.sound_path = sound_path

    def notify(self, message):
        pync.Notifier.notify(message, title="Pomodoro Timer")
        if self.sound_path:
            pygame.mixer.music.load(self.sound_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
