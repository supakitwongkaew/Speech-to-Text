import speech_recognition as sr
from googletrans import Translator
import time

language = ['af','sq','am','ar','hy','az','eu','be','bn','bs','bg','ca','ceb','ny','zh-cn','zh-tw','co','hr','cs','da',
            'nl','en','eo','et','tl','fi','fr','fy','gl','ka','de','el','gu','ht','ha','haw','iw','hi','hmn','hu',
            'is','ig','id','ga','it','ja','jw','kn','kk','km','ku','ky','lo','la','lv','lt','lb','mk','mg','ms'
            'ml','mt','mi','mr','mn','my','ne','no','ps','fa','pl','pt','pa','ro','ru','gd','sr','st','sn','sd',
            'si','sk','sl','so','sm','es','su','sw','sv','tg','ta','te','th','tr','uk','ur','uz','vi','cy','xh',
            'yi','yo','zu','fil','he''ko',]
lanchoose = []
textlist = []
tranlist = []

start_time = time.time()
seconds = 30

lan = str(input('choose language '))
lanchoose.append(lan)
def main():
    while True:

        speech_to_text()
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time > seconds:
            print("Time out")
            print(textlist)

            checktranslate()
            exit()
def speech_to_text():
    #while True:
        #lan = str(input('choose language '))
        #lanchoose.append(lan)
        if lan in language:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Please say something")
                audio = r.listen(source)
                print("Recognizing Now .... ")
                # recognize speech using google
                try:
                    print ("You have said" )
                    word = r.recognize_google(audio,None,lan)
                    textlist.append(word)
                    print(word)
                    print("Audio Recorded Successfully \n ")
                except Exception as e:
                    print("Error ")
                # write audio
                #with open("recorded.wav", "wb") as f:
                    #f.write(audio.get_wav_data())
        #elif lan == 'esc':
             #break

        else:
            exit()

def translate():
    src = lanchoose[0]
    dest = str(input('traget language '))
    translator = Translator()
    word = textlist[0]
    result = translator.translate(word, src= src, dest=dest)

    print(result.src)  # The source language
    print(result.origin)  # Original text, that is 'Mitä sinä teet' in our example
    print(result.dest)  # Destination language, which is set to English (en)
    print(result.text)  # Translated text, that will be 'what are you doing?' in our case

    tranlist.append(result)

def checktranslate():
    print('Translate Word Y/N')
    a = input('')
    if a == "Y" or "y":
        translate()
    elif a == "N" or "n":
         exit()
    else:
        exit()

main()
