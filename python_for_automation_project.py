"""
//Project - Python for Automation//

//libraries to be used//

pyttsx3 = python test to speech
speech_recognition = used to convert spoken words into text and work on API's
automate_wikipedia = used to automate and work with the wikipedia
webbrowser = used for to automate webbrowsers
smtplib = sending emails
os = used to work/interact with operating system
datetime = used to work with the date and time
"""

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import os

engine = pyttsx3.init('sapi5') # sapi5 drivier for voice windows OS, (# Looking alternative for MAC OS)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) #1 is voice of female, 0 is from male voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    """
    12:00 - noon
    1:00 - morning
    1:00 pm - morning / 13:00 afternooon
    18:00 - evening
    6:00 pm - will not understand that
    """

    if hour >= 0 and hour <=12:
        speak("Good Morning my dear friend")
    elif hour >=12 and hour < 18:
        speak("Good afternoon my dear friend") # we use speak for spoken
    else:
        speak("Good evening  my dear friend")
    speak("Le t me know how can I help you, What are you looking for ?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you Manish ..... ")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing your voice .....")
        query = r.recognize_google_cloud(audio, language='en-in')
        print(f"My dear friend you said : {query}\n")

    except Exception as e:
        print("Manish Say that again please ...... ")
        return "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('test123@gmail.com', 'test@123') # replace the email and password
    server.sendmail('test123@gmail.com', to, content) # replace the email
    server.close()

if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()

        if 'open wikipedia' in query:
            speak('Searching wikipedia .....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia ")
            print(results)

        if 'open notepad' in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'open paint' in query:
            npath = "C:\\Windows\\system32\\mspaint.exe"
            os.statfile(npath)

        elif 'open Youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open Great learning academy' in query:
            webbrowser.open("https://www.greatlearning.in/academy")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"My dear friend, the time is {strTime}")

        elif 'open great learning youtube channel' in query:
            webbrowser.open("https://www.youtube.com/c/GreatLearningOfficial")

        elif 'open linkedIN' in query:
            webbrowser.open("www.linkedin.com")

        elif 'email to other friend' in query:
            try:
                speak("What should I send ?")
                content = takecommand()
                to = "poonambalwada22@gmail.com"
                sendEmail(to, content)
                speak("Your email has been sent successfully")
            except Exception as e:
                print(e)
                speak("My dear friend I am unable to send the email ... \n please address the error")