from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from googletrans import Translator
import speech_recognition as sr
from kivy.config import Config
Config.set('graphics', 'resizable', True)
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')


class StartScreen(FloatLayout):
    global lan1
    global lan2
    lan1 = ""
    lan2 = ""
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
    def rec(self):
        if lan1 == "":
            self.ids.youtext.text = ("Please select language")
        else:
            # GUI Blocking Audio Capture
            print("Please say something")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                print("You have said")
                global word
                #global y
                word = r.recognize_google(audio, None, lan1)
                #print(showlan)
                print(word)
                # textlist.append(word)
                # self.output=(word)
                # self.youtext.text = self.word.text
                self.ids.youtext.text = format(word)
                if lan1 == "":
                    self.ids.youtrantext.text = "No word to Translate"
                elif lan2 == "":
                    self.ids.youtrantext.text = "Please select language"
                else:
                    src = lan1
                    # dest = showxlan
                    dest = lan2
                    translator = Translator()
                    result = translator.translate(word, src=src, dest=dest)
                    result = result.text
                    self.ids.youtrantext.text = result
                # self.output=("Audio Recorded Successfully \n ")
                # self.output=("Audio Recorded Successfully \n ")
            except sr.UnknownValueError:
                self.ids.youtext.text= ("Error")
            except sr.RequestError as e:
                self.ids.youtext.text = ("Error".format(e))

    def translate(self):
        if lan1 == "":
            self.ids.youtrantext.text = "No word to Translate"
        elif lan2 == "":
            self.ids.youtrantext.text = "Please select language"
        else:
            src = lan1
            dest = lan2
            translator = Translator()
            result = translator.translate(word, src=src, dest=dest)
            result = result.text
            self.ids.youtrantext.text = result

    def clear(self):
        self.ids.youtext.text = ' '
        self.ids.youtrantext.text = ' '
#### input language ####
    def lan01(self):
        global lan1
        lan1 = "en"
        self.ids.btnlanshow1.text = "English"
    def lan02(self):
        global lan1
        lan1 = "th"
        self.ids.btnlanshow1.text = "Thai"
    def lan03(self):
        global lan1
        lan1 = "ru"
        self.ids.btnlanshow1.text = "Russia"
    def lan04(self):
        global lan1
        lan1 = "fr"
        self.ids.btnlanshow1.text = "France"
    def lan05(self):
        global lan1
        lan1 = "de"
        self.ids.btnlanshow1.text = "Germany"
#### input translate ####
    def lan10(self):
        global lan2
        lan2 = "en"
        self.ids.btnlanshow2.text = "English"
    def lan20(self):
        global lan2
        lan2 = "th"
        self.ids.btnlanshow2.text = "Thai"
    def lan30(self):
        global lan2
        lan2 = "ru"
        self.ids.btnlanshow2.text = "Russia"
    def lan40(self):
        global lan2
        lan2 = "fr"
        self.ids.btnlanshow2.text = "France"
    def lan50(self):
        global lan2
        lan2 = "de"
        self.ids.btnlanshow2.text = "Germany"

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.theme_style = "Dark"
        return StartScreen()

if __name__=='__main__':
    MainApp().run()