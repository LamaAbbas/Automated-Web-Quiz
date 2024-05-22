# Automated-Web-Quiz
## Developed by Lama Abbas
This Python script runs an automated web scraper that navigates the homepage of the Wizard101 website to complete the daily allowance of trivia quizzes without human intervention. The program mainly leverages the Selenium library to parse through the quizzes, and detects reCAPTCHAs for the user to complete.

The program is still a work-in-progress to iron out the wrinkles as well as finish the transition to JSON integration, increased efficiency, and heightened coding conventions.

In the future I am hoping to containerize the script into a small application containing all of its dependencies, and build a Chrome extension with a GUI for reCAPTCHA completion confirmation.

## How to use
As the script is not containerized there are a few installtions needed before the script can be compiled and ran.

First, the web scraper operates on Google Chrome, and ```chromedriver.exe``` is required. Download the latest stable release from [this site](https://developer.chrome.com/docs/chromedriver/downloads).

If you haven't already, install ```python3```, you can get started [here](https://www.python.org/downloads/). Additionally, you will need ```pip```:

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
Then:
```bash
python get-pip.py
```

Once ```pip``` is installed, you can now proceed installing the following:
```bash
pip install selenium
pip install python-dotenv
```

