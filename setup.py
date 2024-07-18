from setuptools import setup, find_packages

setup(
    name='pomodoro_timer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'plyer',
        'pygame',
    ],
    entry_points={
        'console_scripts': [
            'pomodoro = main:main',
        ],
    },
)
