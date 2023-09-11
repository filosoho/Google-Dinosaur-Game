# Google-Dinosaur-Game
Play the Google Dinosaur Game automatically using Python and Selenium WebDriver.

# Introduction

This project allows you to automate and play the popular Google Dinosaur Game found in the Google Chrome browser. The game is a simple side-scrolling runner where a dinosaur runs across the screen, and you need to jump over obstacles.  

This repository provides a Python script that uses Selenium WebDriver to control the game and make the dinosaur jump automatically. You can use this script to enjoy the game without any manual input.  

## Features

- Automated gameplay of the Google Dinosaur Game.
- Randomized jumping to make gameplay more interesting.
- Adjustable jump frequency and game speed.
- Graceful handling of WebDriver errors and window closures.

## Prerequisites

Before you can run the script, ensure you have the following dependencies installed:

- Python 3.x
- Selenium WebDriver for Chrome: [Download ChromeDriver](https://sites.google.com/chromium.org/driver/)

## Getting Started

Install the required Python libraries:

~~~
pip install selenium
~~~

Place the downloaded ChromeDriver executable in the same directory as the script or provide its path in the script.

Run the script:

~~~
dinosaurgame.py
~~~

Enjoy the automated gameplay!

# Customization

You can customize the gameplay by adjusting the following parameters in the dinosaurgame.py script:

JUMP_THRESHOLD: The probability of jumping (0.2 by default).
SLEEP_TIME: Adjust the sleep time to control the game's speed (0.1 seconds by default).

# Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and test thoroughly.
Create a pull request with a clear description of your changes.

# License
Feel free to use and modify the code as per your requirements.

# Acknowledgments
The Google Dinosaur Game is a fun project by Google.
Selenium is an open-source tool for automating web browsers.

