import pyttsx3
import speech_recognition as sr
import smtplib


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

            #Using google for voice recognition.
            query = r.recognize_google(audio, language='en-in')

             #User query will be printed.
            print(f"User said: {query}\n")

        except Exception as e:

            #Say that again will be printed in case of improper voice 
            print("Say that again please...")
            return "None"
    return query




def speak(audio):
    engine = pyttsx3.init('espeak')
    engine.setProperty('rate', 200)  # Adjust rate as needed (default is 200)
    engine.setProperty('volume', 1.0)  # Adjust volume as needed (default is 1.0)
    engine.say(audio)
    engine.runAndWait()   #Without this, audio will not be audible to us.




# make our AI assistant wish or greet user
def wishMe():
    speak("Hello, I am AI Assistant. What Should I do for you ?")



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('from@gmail.com', 'Password')
    server.sendmail('from@gmail.com', to, content)
    server.close()
