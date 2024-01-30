# GIF to Boot Animation Converter

The GIF to Boot Animation Converter is a Python-based tool designed to simplify the process of converting GIF files into boot animations for Android devices. This user-friendly tool provides a straightforward interface and commands, making it accessible for users who want to customize their device's boot animation.

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

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Copy Button Example</title>

    <!-- Include Clipboard.js library -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.8/clipboard.min.js"></script>

    <!-- Style for the copy button (optional) -->
    <style>
        .copy-button {
            cursor: pointer;
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 8px 16px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 14px;
            margin-top: 10px;
        }
    </style>
</head>
<body>

    <!-- Content to be copied -->
    <div id="copy-text">
    git clone https://github.com/soni-shashan/GIF-TO-BOOT-ANIMATION.git
    </div>

    <!-- Copy button -->
    <button class="copy-button" data-clipboard-target="#copy-text">Copy Text</button>

    <!-- Initialize Clipboard.js -->
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            var clipboard = new ClipboardJS('.copy-button');

            clipboard.on('success', function (e) {
                console.info('Text copied to clipboard:', e.text);
            });

            clipboard.on('error', function (e) {
                console.error('Unable to copy text to clipboard:', e.action);
            });
        });
    </script>

</body>
</html>



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
