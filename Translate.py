from googletrans import Translator
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])

text1 = "subscribe my channel"

text2 = "สัปตะไคร่ช่องฉัน"

text3 = "kanalıma abone ol"



translator = Translator()


print("Translate English to th : ", translator.translate(text1, src='en', dest='th'))

print("Translate En to Tur : ", translator.translate(text1, src='en', dest='tr'))