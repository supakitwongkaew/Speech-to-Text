
import speech_recognition as sr

language = ['af','sq','am','ar','hy',
            'az','eu','be','bn','bs',
            'bg','ca','ceb','ny','zh-cn',
            'zh-tw','co','hr','cs','da',
            'nl','en','eo','et','tl',
            'fi','fr','fy','gl','ka',
            'de','el','gu','ht','ha',
            'haw','iw','hi','hmn','hu',
            'is','ig','id','ga','it',
            'ja','jw','kn','kk','km',
            'ku','ky','lo','la','lv',
            'lt','lb','mk','mg','ms'
            'ml','mt','mi','mr','mn',
            'my','ne','no','ps','fa',
            'pl','pt','pa','ro','ru',
            'gd','sr','st','sn','sd',
            'si','sk','sl','so','sm',
            'es','su','sw','sv','tg',
            'ta','te','th','tr','uk',
            'ur','uz','vi','cy','xh',
            'yi','yo','zu','fil','he'
            'ko',]

def main():
    while True:
        lan = str(input('choose language '))
        if lan in language:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Please say something")
                audio = r.listen(source)
                print("Recognizing Now .... ")
                # recognize speech using google
                try:
                    print("You have said \n" + r.recognize_google(audio,None,lan))
                    print("Audio Recorded Successfully \n ")
                except Exception as e:
                    print("Error :  " + str(e))
                # write audio
                with open("recorded.wav", "wb") as f:
                    f.write(audio.get_wav_data())
        elif lan == 'esc':
            break
        else:
            print('No language')

if __name__ == "__main__":
    main()
