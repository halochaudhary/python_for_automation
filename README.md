# python_for_automation
Python for automation project - Skill --> Speech recognition and Sending emails via speech


## Python Package Installation Guide

This guide provides the steps to install the necessary Python packages for text-to-speech, speech recognition, and Wikipedia API access.

## Prerequisites

Ensure you have Python and pip installed on your system. You can check this by running the following commands:

```bash
python --version
pip --version
```

## Installation Steps

### 1. Install pyttsx3

`pyttsx3` is a text-to-speech conversion library in Python.

```bash
pip install pyttsx3
```

### 2. Install SpeechRecognition

`SpeechRecognition` is a library that helps with performing speech recognition.

```bash
pip install SpeechRecognition
```

### 3. Install Wikipedia

The `wikipedia` library provides a simple Python wrapper for the Wikipedia API.

```bash
pip install wikipedia
```

## Verification

After installation, you can verify that the packages are installed correctly by importing them in a Python shell:

```python
import pyttsx3
import speech_recognition as sr
import wikipedia
```

If there are no errors, the installation was successful!

## Troubleshooting

If you encounter issues during installation, ensure that your Python and pip versions are up-to-date. Additionally, refer to the official documentation for each package:

- [pyttsx3 Documentation](https://pyttsx3.readthedocs.io/)
- [SpeechRecognition Documentation](https://pypi.org/project/SpeechRecognition/)
- [Wikipedia Documentation](https://pypi.org/project/wikipedia/)
