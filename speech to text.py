import speech_recognition as sr
r = sr.Recognizer()
th,en = "th","en"

lan = input("choose languages ")


if lan == th:
    print("talk")
    with sr.Microphone() as source:
        while True:
            audio = r.listen(source)
            try:
                print('You said : '+r.recognize_google(audio, None,'th'))
            except:
                print('ไม่สามารถแปลงได้!')
elif lan == en:
    print("talk")
    with sr.Microphone() as source:
        while True:
            audio = r.listen(source)
            try:
                print('You said : '+r.recognize_google(audio, None,'en'))
            except:
                print('Error!')
else:
    print("No languages")