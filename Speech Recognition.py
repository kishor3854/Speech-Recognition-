import webbrowser as wb
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
from googlesearch import search

def ola(name):
	speak("Hold on "+name+" , I will redirect you to the ola.")
	wb.open("www.olacabs.com")

def pay(name):
	speak("Hold on "+name+" , I will redirect you to the paytm.")
	wb.open("www.paytm.com")

def instagram(name):
 	speak("Hold on "+name+" , I will redirect you to the instagram.")
 	wb.open("www.instagram.com")

def facebook(name):
	speak("Hold on "+name+" , I will redirect you to the facebook.")
	wb.open("www.facebook.com")

def youtube(name):
	speak("Hold on "+name+" , I'm opening Youtube for you.")
	wb.open("www.youtube.com")

def gmail(name):
	speak("just a minute "+name+", bring you to the Gmail.")
	wb.open("www.gmail.com")

def locations(name):
	data = data.split(" ")
	locations = data[2]
	speak("Hold on "+name+" , I will show you where " + location + " is.")
	wb.open("https://www.google.nl/maps/place/" + location + "/&amp")

def search(data,name):
	speak("wait for a while "+name+" ,I will search for you.")
	wb.open("https://www.google.co.in/?gfe_rd=cr&ei=V7DXWJuQNarT8gfb-42QBw&gws_rd=ssl#newwindow=1&safe=active&q="+data+"&*")

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("audio.mp3")


def recordAudio():
    r = sr.Recognizer()
	#r.recognize_google(audio)
    with sr.Microphone() as source:audio = r.listen(source)

    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def PA(data,name):
	print(data)
	if "I would like to use paytm" in data:
		pay(name)

        if "I would like to use instagram" in data:
		instagram(name)

	if "what is your name" in data:
		speak("Jarvis")

	if "how are you" in data:
		speak("I am fine and you ?")

	if "what time is it?" in data:
		speak(ctime())

	if "where is" in data:
		locations(name)

	if "I would like to use Facebook" in data:
		facebook(name)

	if "I would like to hear some music" in data:
		youtube(name)

	if "check my mail" in data:
		gmail(name)

	if "search for" in data:
		search(data,name)

	if "booking taxi" in data:
		ola(data,name)


	if "goodbye" in data:
		speak("Good bye ! ,"+name+" ,take care!!")
		exit()



speak("what's Your name sir:")
name=input()
speak("Hi "+name+"!!! what can I do for you?")

while 1:
    print("Speak. . .")
    data = recordAudio()
    print ("Processing. . .")
    PA(data,name)
