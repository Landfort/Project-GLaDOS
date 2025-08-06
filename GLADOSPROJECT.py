import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
import pyaudio
import wave
import random
haw1="helloandwelcome1.wav"
haw2="nevidelis.wav"
ch = 600
######################
#songs
song1="glados song1.wav"
song2="glados song2.wav"
cs1=12000
##########################
#tell about yourselve  
tay1="gladosTAY1.wav"
tay2="gladosTAY2.wav"
cht=600
########################
#okay
g1="horoshokvity.wav"
g2="onemoment.wav"
cg=400
#########################
#goodbye
gb1="lwasfunny.wav"
gb2="end.wav"
cgb=400
########################


#def talk(words):
 #   print("talk")

#print("i was ere")
#talk("Hello say something")
#print("works")

    #print(words)
    #os.system("say" + words)

#talk("Hello , ask me about something")

 #p = pyaudio.PyAudio()

#p=pyaudio.PyAudio()
#for i in range(p.get_device_count()):
 #   print(p.get_device_info_by_index(i)['name'])


#engine = pyttsx3.init()
#engine.say("Hello man")
#engine.runAndWait()
def saying(x,y):
    CHUNK = 1024
    wf = wave.open(x, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(CHUNK)
    cnt = 0
    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)
        cnt=cnt+1
        if(cnt == y):
            data = ''
    stream.stop_stream()
    stream.close()
    p.terminate()

############################## say hello
ran = random.randint(1, 2)
if (ran == 1):
    saying(haw1, ch)
elif (ran == 2):
    saying(haw2, ch)
####################################
def song():
    ran = random.randint(1, 2)
    if (ran == 1):
        saying(song1, cs1)
    elif (ran == 2):
        saying(song2, cs1)


def sabaton():
    ran = random.randint(1,3)
    if (ran == 1):
        url = 'https://www.youtube.com/watch?v=zHl2EbEsE4A'
        webbrowser.open(url)
    elif (ran == 2):
        url = 'https://www.youtube.com/watch?v=oVWEb-At8yc'
        webbrowser.open(url)
    elif (ran == 3):
        url = 'https://www.youtube.com/watch?v=xP8G-LwWNn0'
        webbrowser.open(url)




def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Hello master! Im GLaDOS, What do you want from me?")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration = 1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio).lower()
        print("You said " + task)
    except sr.UnknownValueError:
 #       talk("I dont understand")
        task = command()

    return task

def makeSomething(task):
    if 'open website' in task:
        saying(g1,cg)
        url='https://www.youtube.com/watch?v=Q_n3n819dGI'
        webbrowser.open(url)
  ############################################

    elif 'stop' in task:
        ran = random.randint(1, 2)
        if (ran == 1):
            saying(gb1, cgb)
        elif (ran == 2):
            saying(gb2, cgb)
        sys.exit()

   ##############################################
    elif 'what is your favorite song' in task:
        #      talk("Alright master")
        url2 = 'https://www.youtube.com/watch?v=qVHyl0P_P-M'
        webbrowser.open(url2)
    elif 'song' in task:
        #      talk("Alright master")
        url2 = 'https://www.youtube.com/watch?v=qVHyl0P_P-M'
        webbrowser.open(url2)
####################################################
    elif 'can you sing for us' in task:
        song()
    elif 'sing for us' in task:
        song()
#####################################################

    elif 'tell something about yourself' in task:
        saying(tay1,cht)
        saying(tay2,cht)

######################################################
    elif 'sabaton' in task:
        sabaton()
#######################################################PHOTO
    elif 'photo' in task:
        saying(g2,cg)
        url2 = 'https://vk.com/im?sel=165317369&z=photo165317369_457246515%2Fmail308420'
        webbrowser.open(url2)
############################################################
    elif 'papers' in task:
        os.system('"C:/GOG Games/PapersPlease/PapersPlease.exe"')
##############################################################
    elif 'telegram' in task:
        os.system('"C:/Windows.old/Users/Aleksandr Marinchuk/AppData/Roaming/Telegram Desktop/Telegram.exe"')
##############################################################
    elif 'kale' in task:
        os.system('"C:/CAFEDRA/servomotor4.21 чистка варнингов/servomotor4/servomotor4/MDK-ARM/servomotor4.uvprojx"')

while True:
    makeSomething(command())



