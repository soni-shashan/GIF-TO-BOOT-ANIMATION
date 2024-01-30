# Project Name

Brief description or tagline about your project.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Introduction

This Python-based tool allows users to convert GIF files into boot animations for Android devices. It simplifies the process by providing a user-friendly interface and straightforward commands.

## Features

Clone Repository:


git clone https://github.com/soni-shashan/GIF-TO-BOOT-ANIMATION.git


Installation of Requirements:


cd GIF-TO-BOOT-ANIMATION
pip install -r requirements.txt


Create Executable File:


pip install pyinstaller


pyinstaller --noconfirm --onefile --windowed --icon "%cd%/loading.ico" --name "GIF TO BOOT ANIMATION" --add-data "%cd%/create_boot_animation.py;." --add-data "%cd%/gifextract.py;." --add-data "%cd%/loading.ico;." --add-data "C:/Users/shash/AppData/Roaming/Python/Python312/site-packages/customtkinter;customtkinter/"  "%cd%/boot_to_gif.py"



## Usage

1.Clone the repository using the provided git clone command.


2.Navigate to the project directory.


3.Install required libraries using pip.


4.Use Pyinstaller to create an executable file for easy execution.

## Requirements

1.Git


2.Python 3.12


3.Pip


4.Pyinstaller

## Contributions

Contributions are welcome! If you have suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## Acknowledgments

Special thanks to soni-shashan for creating the original repository.

---
**Note:** Replace paths and details according to your specific Python version and environment.
