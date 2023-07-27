To run this code on macOS, Linux, and Windows, you need to have the following software and libraries installed:

1. Python: Make sure you have Python installed on your system. You can download the latest version of Python from the official website: https://www.python.org/downloads/

2. Required Python packages: Install the required Python packages using pip. Open a terminal or command prompt and run the following commands:

```bash
pip install speechrecognition
pip install gtts
pip install wikipedia-api
pip install pyjokes
pip install pywhatkit
pip install openai
```

3. OpenAI API Key: Before running the code, you need to get an API key from OpenAI. Visit the OpenAI website (https://openai.com) and sign up to get your API key. Replace `'YOUR_OPENAI_API_KEY'` in the code with your actual API key.

Once you have Python and the required packages installed and the API key ready, you can save the code to a file (e.g., `friday.py`) and run it from the terminal or command prompt using the following command:

```bash
python friday.py
```

Please note that this code uses platform-specific commands (`subprocess.Popen()`) to open and close applications and turn off the computer. Make sure to use these features responsibly and test them carefully on your system before regular usage. The shutdown command, in particular, should be used with caution as it can shut down the computer immediately without further confirmation.
