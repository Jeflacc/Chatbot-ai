from urllib.request import urlopen
import json
import re
import pyttsx3
import speech_recognition

print("start chatting")

def loop():

   main()

def main():
    speaker = pyttsx3.init()
    
    msg = ""

    url = "http://api.brainshop.ai/get?bid=[bid]key=[brainshop key]uid=[001]&msg=[Msg]"  

    
    recognizer = speech_recognition.Recognizer()  


    with speech_recognition.Microphone() as mic:

        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)

        vc = recognizer.recognize_google(audio)
        vc = vc.lower()

        print(vc)
            






    msg = vc
    msg = re.sub(r"\s+", '%20', msg)
    new_s = re.sub('Msg', msg, url, count=1, flags=1)
    
    response = urlopen(new_s)

    data_json = json.loads(response.read())

    print(data_json["cnt"])

    url = "http://api.brainshop.ai/get?bid=163895&key=ABQ0CBtuso2xytlX&uid=[001]&msg=[Msg]"
    voices = speaker.getProperty('voices')
    speaker = pyttsx3.init()
    speaker.setProperty('voice', voices[1].id)
    speaker.say(data_json["cnt"])
    speaker.runAndWait()

    loop()

main()




