import os
import subprocess
import datetime
import wikipedia
import webbrowser
# import smtplib
from assistant_utils import takeCommand, speak, wishMe, sendEmail

''' 
pyttsx3 --> help us to convert text to speech 
datetime --> to provide the current date and time to the AI 
wikipedia --> for the wikipedia searches
webbrowser --> to open any website 
smtplib --> smple mail transfer protocol allows us to send emails 
'''






if __name__ == "__main__":
    wishMe()
    while True:

        #Converting user query into lower case
        query = takeCommand().lower()

        #if wikipedia found in the query then this block will be executed
        if 'wikipedia' in query:  
            speak('Searching on Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        #if open youtube found in the query then this block will be executed
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        

        #if open google found in the query then this block will be executed
        elif 'open google' in query:
            webbrowser.open("google.com")

        #if play music found in the query then this block will be executed
        elif 'play music' in query:
            music_dir = '/home/umang.rathi/Music'
            songs = os.listdir(music_dir)
            if songs:
                subprocess.Popen(['xdg-open', os.path.join(music_dir, songs[0])])
            else:
                print("No music found in the specified directory.")

            # print(songs)    
            # os.startfile(os.path.join(music_dir, songs[0]))


        #if time found in the query then this block will be executed
        elif 'time' in query:
            now = datetime.datetime.now()
            strTime = now.strftime("%H hours %M minutes %S seconds")
            speak(f"Sir, the time is {strTime}")


        #if open vs code found in the query then this block will be executed
        elif 'open vs code' in query:
            codePath = "/snap/bin/code"
            # os.startfile(codePath)
            subprocess.Popen([codePath])


        #if send email found in the query then this block will be executed
        elif 'send email' in query:
            try:
                speak("What should I send?")
                content = takeCommand()
                to = "to@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email") 

        elif 'exit' in query:
            break
