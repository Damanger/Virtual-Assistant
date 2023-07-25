import speech_recognition as sr
from gtts import gTTS
import os
import wikipedia
import pyjokes
import pywhatkit
import datetime
import webbrowser
import subprocess
import platform

listener = sr.Recognizer()

def talk(text):
    # Function to convert text to speech and play it
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')
    os.system('afplay output.mp3')

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            # Set the timeout for listening to 3 seconds
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice).lower()
            if 'friday' in command:
                # Remove the assistant's name from the command to improve recognition
                command = command.split('friday', 1)[-1].strip()
                print(command)
            else:
                # If the assistant's name is not mentioned, set the command to an empty string
                command = ""
    except sr.UnknownValueError:
        # If the speech is not understood, set the command to an empty string
        command = ""
    except sr.RequestError:
        # If there's a problem with the speech recognition service, set the command to an empty string
        command = ""
    except sr.WaitTimeoutError:
        # If the listening times out, set the command to an empty string
        command = ""
    return command

def run_friday():
    talk("Hello, I'm Friday")
    while True:
        talk("How can I assist you?")
        command = take_command()
        print(command)
        if command.startswith('play'):
            # Play a song on YouTube based on the user's request
            song = command.replace('play', '').strip()
            talk('playing ' + song + ' on YoutTube')
            pywhatkit.playonyt(song)
        elif 'what time is it' in command:
            # Get the current time and tell the user
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif command.startswith('who is'):
            # Get a summary of a person from Wikipedia based on the user's request
            person = command.replace('who is', '').strip()
            try:
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            except wikipedia.exceptions.PageError:
                talk(f"Sorry, I couldn't find information about {person} on Wikipedia.")
        elif 'are you single' in command:
            # Humorous response to a funny question
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            # Tell a random joke
            talk(pyjokes.get_joke())
        elif command.startswith('open'):
            app_name = command.replace('open', '').strip()
            talk(f"Opening {app_name}")
            if platform.system() == 'Darwin':  # macOS
                try:
                    subprocess.Popen(['open', '-a', app_name])
                except FileNotFoundError:
                    talk(f"Sorry, I couldn't find the app: {app_name}")
            elif platform.system() == 'Windows':
                try:
                    subprocess.Popen(['start', app_name])
                except FileNotFoundError:
                    talk(f"Sorry, I couldn't find the app: {app_name}")
            elif platform.system() == 'Linux':
                try:
                    subprocess.Popen(['xdg-open', app_name])
                except FileNotFoundError:
                    talk(f"Sorry, I couldn't find the app: {app_name}")
            else:
                talk("Sorry, opening applications is only supported on macOS, Windows, and Linux systems.")
        elif 'website' in command:
            # Open a website in the default web browser based on the user's request
            web_page = command.replace('website', '').strip()
            talk(f"Opening {web_page}")
            aux = "https://" + web_page + ".com"
            webbrowser.open(aux)
        elif command.startswith('search'):
            # Perform a Google search based on the user's request
            search_query = command.replace('search', '').strip()
            talk(f"Searching for {search_query} on Google.")
            pywhatkit.search(search_query)
        elif command.startswith('close'):
            app_name = command.replace('close', '').strip()
            talk(f"Closing {app_name}")
            if platform.system() == 'Darwin':  # macOS
                try:
                    subprocess.Popen(['osascript', '-e', f'quit app "{app_name}"'])
                except FileNotFoundError:
                    talk(f"Sorry, I couldn't find the app: {app_name}")
            elif platform.system() == 'Windows':
                try:
                    subprocess.Popen(['taskkill', '/f', '/im', app_name + '.exe'])
                except FileNotFoundError:
                    talk(f"Sorry, I couldn't find the app: {app_name}")
            elif platform.system() == 'Linux':
                try:
                    subprocess.Popen(['pkill', app_name])
                except FileNotFoundError:
                    talk(f"Sorry, I couldn't find the app: {app_name}")
            else:
                talk("Sorry, closing applications is only supported on macOS, Windows, and Linux systems.")
        elif 'turn off computer' in command:
            # Check if the command to turn off the computer is given
            talk("Are you sure you want to turn off the computer?")
            confirm_command = take_command()
            if 'yes' in confirm_command:
                talk("Shutting down the computer. Goodbye!")
                # The code below will shut down the computer, so use with caution!
                if platform.system() == 'Windows':
                    os.system("shutdown /s /t 1")
                elif platform.system() == 'Darwin' or platform.system() == 'Linux':
                    os.system("sudo shutdown -h now")
                else:
                    talk("Sorry, shutting down the computer is only supported on macOS, Windows, and Linux systems.")
                break
            else:
                talk("Cancelled the shutdown.")
        elif command == "bye":
            # End the conversation with a farewell message
            talk("Bye Master")
            break
        else:
            # If the command is not recognized, ask the user to repeat
            talk('Please say the command again')

run_friday()
