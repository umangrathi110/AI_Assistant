# text to speech library 
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import subprocess

''' 
pyttsx3 --> help us to convert text to speech 
datetime --> to provide the current date and time to the AI 
wikipedia --> for the wikipedia searches
webbrowser --> to open any website 
smtplib --> smple mail transfer protocol allows us to send emails 
'''






# this function will return the string output by taking microphone input from the user
def takeCommand():

    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            print(f"User said: {query}\n")  #User query will be printed.

        except Exception as e:
            # print(e)    
            print("Say that again please...")   #Say that again will be printed in case of improper voice 
            return "None" #None string will be returned
        
    return query

 


 

def speak(audio):
    subprocess.call(['espeak', audio])
    # engine.say(audio) 
    engine.runAndWait()  #Without this, audio will not be audible to us.



# make our AI assistant wish or greet user according to time of pc 
def wishMe():
    speak("Hello, I am AI Assistant. What Should I do for you ?")



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('umang.rathi@impressico.com', 'Rumang@2900')
    server.sendmail('umang.rathi@impressico.com', to, content)
    server.close()


engine = pyttsx3.init('espeak')    # Speech API helps in synthesis and recognition of voice 

voices= engine.getProperty('voices')    #getting details of current voice

engine.setProperty('rate', 150)  # Adjust rate as needed (default is 200)

engine.setProperty('voice', voices[1].id)    #voice[0].id => Male voice voice[1].id => female voice

engine.setProperty('volume', 1.0)  # Adjust volume as needed (default is 1.0)



if __name__ == "__main__":
    
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query


        #if wikipedia found in the query then this block will be executed
        if 'wikipedia' in query:  
            speak('Searching on Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)


        # if opoen youtube found in the query then this block will be executed
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        # if open google found in the query then this block will be executed
        elif 'open google' in query:
            webbrowser.open("google.com")


        #if play music found in the query then this block will be executed
        elif 'play music' in query:
            music_dir = '/home/umang.rathi/Music'
            songs = os.listdir(music_dir)
            if songs: # Play the first song using mpv
                subprocess.Popen(['xdg-open', os.path.join(music_dir, songs[0])])
            else:
                print("No music found in the specified directory.")
                
            # print(songs)    
            # os.startfile(os.path.join(music_dir, songs[0]))


        #if the time found in the query then this block will be executed
        elif 'the time' in query:
            now = datetime.datetime.now()
            strTime = now.strftime("%H hours %M minutes %S seconds")
            speak(f"Sir, the time is {strTime}")



        #if open code found in the query then this block will be executed
        elif 'open vs code' in query:
            codePath = "/snap/bin/code"
            # os.startfile(codePath)
            subprocess.Popen([codePath])


        #if email found in the query then this block will be executed
        elif 'send email' in query:
            try:
                speak("What should I send?")
                content = takeCommand()
                to = "umangrathi110@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email") 

        elif 'exit' in query:
            break





 