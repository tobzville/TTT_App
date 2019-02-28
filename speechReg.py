from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')

#listen for commands
def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("I am ready for your next command")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said: " + command + "/n")

        #loop back to continue listening for commands

    except sr.UnknownValueError:
        assistant(myCommand())

        return command

#if statements for executing the commands
def assistant(command):
    if 'open Reddit python' in command:
        chrome_path = ''
        url = 'https://www.reddit.com/r/python'
        webbrowser.get(chrome_path).open(url)

    if 'what\'s up' in command:
    talkToMe('Chilling bro')

    if 'email' in command:
        talkToMe('Who is the recipient')
        recipient = myCommand()

        if 'Tobe' in recipient:
            talkToMe('What should I say')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('tobzville@gmail.com', 'timezone01')

            #send message
            mail.sendmail('PERSON NAME', 'emailaddress@whatever.com', content)

            #close connection
            mail.close()

            talkToMe('email sent')

talkToMe('I am ready for your command')

while True:
    assistant(myCommand())
