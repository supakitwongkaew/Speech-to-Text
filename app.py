from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton
from kivymd.uix.button import MDFloatingActionButton
from kivy.core.window import Window
import speech_recognition as sr
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.menu import MDDropdownMenu, RightContent
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivymd.uix.menu import MDDropdownMenu
from googletrans import Translator
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.list import OneLineListItem
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable

# -*- coding: utf-8 -*-
from googletrans import Translator
from kivy.config import Config

Config.set('graphics', 'width', '330')
Config.set('graphics', 'height', '560')

screen_helper = """
ScreenManager:
    Screen01:
    Screen02:
    Screen03:

<Screen01>:
    name: 'main'
    FloatLayout:
        orientation: 'horizontal'
        canvas:
            Rectangle:
                source: 'TT1.png'
                size: self.size
                pos: self.pos
    BoxLayout:
        orientation: 'vertical'
    MDRectangleFlatButton
        text:"record"
        theme_text_color:"Custom"
        text_color: 1, 0, 0, 1
        pos_hint: {'center_x':0.3,'center_y':0.47}
        on_press: root.manager.current = 'rec'   
    MDRectangleFlatButton
        text:"history"
        theme_text_color:"Custom"
        text_color: 0, 1, 1, 1
        pos_hint: {'center_x':0.7,'center_y':0.47}
        on_press: root.manager.current = 'history'   


<Screen02>:
    name: 'rec'
    FloatLayout:
        orientation: 'horizontal'
        canvas:
            Rectangle:
                source: 't1.2.png'
                size: self.size
                pos: self.pos
    BoxLayout:
        orientation: 'vertical'
    Label
        id : youtext
        text:''
        halign:'center'
        font_name:"arial-unicode-ms.otf"
        pos_hint:{'center_x': 0.5, 'center_y': 0.72}
        text_size: root.width,None
        size: self.texture_size
    Label
        id : youtrantext
        text:''
        halign:'center'
        font_name:"arial-unicode-ms.otf"
        pos_hint:{'center_x': 0.5, 'center_y': 0.3}
        text_size: root.width,None
        size: self.texture_size


    MDIconButton:
        icon: "microphone"
        user_font_size: "45sp"
        pos_hint: {"center_x": .5, "center_y": .07}
        on_press: root.rec()
    MDIconButton:
        icon: "delete"
        user_font_size: "25sp"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_press: root.clear()
    MDIconButton:
        icon: "format-letter-case"
        user_font_size: "25sp"
        pos_hint: {"center_x": .9, "center_y": .17}
        on_press: root.translate()
####################################################################
    MDFlatButton:
        id: Buttontext
        text: ''
        on_release: root.show_lan_text()
        theme_text_color:"Custom"
        text_color:(0/255, 237/255, 255/255 )
        size_hint_y: None
        pos_hint: {"center_x": .25, "center_y": .5}
    MDLabel
        id:btnlanshow1
        text:'Language'
        theme_text_color:"Custom"
        text_color:(0/255, 237/255, 255/255 )
        halign:'center'
        pos_hint:{'center_x': 0.25, 'center_y': 0.5}
        font_style:'Subtitle2'

####################################################################
    MDFlatButton:
        id: Buttontexttran
        text: ''
        on_release: root.show_lan_tran()
        pos_hint: {"center_x": .75, "center_y": .5}
    MDLabel
        id:btnlanshow2
        text:'Language '
        theme_text_color:"Custom"
        text_color:(255/255, 0/255, 65/255 )
        halign:'center'
        pos_hint: {"center_x": .75, "center_y": .5}
        font_style:'Subtitle2'

    MDIconButton
        icon: "chevron-double-left"
        theme_text_color:"Custom"
        text_color:(255 / 255, 255 / 255, 255 / 255)
        pos_hint: {'center_x':0.15,'center_y':0.9}
        on_press: root.manager.current = 'main'   

<TrItemConfirm>
    on_release: root.set_icon(check)
    CheckboxLeftWidget:
        id: check
        group: "check"




<Screen03>:
    name: 'history'
    FloatLayout:
        orientation: 'horizontal'
        canvas:
            Rectangle:
                source: 'TT2.png'
                size: self.size
                pos: self.pos
    BoxLayout:
        orientation: 'vertical'

    MDIconButton
        icon: "chevron-double-left"
        theme_text_color:"Custom"
        text_color:(255 / 255, 255 / 255, 255 / 255)
        pos_hint: {'center_x':0.15,'center_y':0.9}
        on_press: root.manager.current = 'main'

    MDRectangleFlatButton
        text: "Show"
        pos_hint: {'center_x':0.5,'center_y':0.15}
        on_release : root.show_his()


    Label
        id : histext01
        text:''
        halign:'center'
        font_name:"arial-unicode-ms.otf"
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        text_size: root.width,None
        size: self.texture_size
    Label
        id : histext02
        text:''
        halign:'center'
        font_name:"arial-unicode-ms.otf"
        pos_hint:{'center_x': 0.7, 'center_y': 0.8}
        text_size: root.width,None
        size: self.texture_size

"""


class Screen01(Screen):
    pass


class Screen02(Screen):
    sm = ScreenManager()
    dialog = None
    global his_all
    his_all = []
    global num
    num = 0
    global lan1
    global lan2
    lan1 = ""
    lan2 = ""
    global his_text
    his_text = []
    global his_tran
    his_tran = []

    def __init__(self, **kwargs):
        super(Screen02, self).__init__(**kwargs)

    def rec(self):
        global num
        if lan1 == "":
            self.ids.youtext.text = ("Please select language")
        else:
            Snackbar(text="Record Done").show()
            print("Please say something")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                print("You have said")
                global word
                word = r.recognize_google(audio, None, lan1)
                print(word)
                self.ids.youtext.text = format(word)
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
                    num = num + 1
                    print(num)
                    his_text.append(word)
                    his_tran.append(result)
                    his_all.append(word)
                    his_all.append(result)
                    # his_all[str(word)] = str(result)
                    # his_text[num] = str(word)
                    # his_tran[num] = str(result)
            except sr.UnknownValueError:
                self.ids.youtext.text = ("Error")
            except sr.RequestError as e:
                self.ids.youtext.text = ("Error".format(e))

            print(his_all)
            print(his_text)
            print(his_tran)

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
    def closeDialog(self, inst):
        self.dialog.dismiss()

    def lan01(self, *a1):
        global lan1
        lan1 = "en"
        self.ids.btnlanshow1.text = "English"

    def lan02(self, *a1):
        global lan1
        lan1 = "th"
        self.ids.btnlanshow1.text = "Thai"

    def lan03(self, *a1):
        global lan1
        lan1 = "ru"
        self.ids.btnlanshow1.text = "Russia"

    def lan04(self, *a1):
        global lan1
        lan1 = "fr"
        self.ids.btnlanshow1.text = "France"

    def lan05(self, *a1):
        global lan1
        lan1 = "de"
        self.ids.btnlanshow1.text = "Germany"

    def lan06(self, *a1):
        global lan1
        lan1 = "ja"
        self.ids.btnlanshow1.text = "Japan"

    def lan07(self, *a1):
        global lan1
        lan1 = "lo"
        self.ids.btnlanshow1.text = "Lao"

    def lan08(self, *a1):
        global lan1
        lan1 = "ko"
        self.ids.btnlanshow1.text = "South-Korea"

    def lan09(self, *a1):
        global lan1
        lan1 = "es"
        self.ids.btnlanshow1.text = "Spain"

    def lan010(self, *a1):
        global lan1
        lan1 = "vi"
        self.ids.btnlanshow1.text = "Vietnam"

    def lan011(self, *a1):
        global lan1
        lan1 = "it"
        self.ids.btnlanshow1.text = "Italy"

    def lan012(self, *a1):
        global lan1
        lan1 = "pt"
        self.ids.btnlanshow1.text = "Portugal"

    def lan013(self, *a1):
        global lan1
        lan1 = "zh-CN"
        self.ids.btnlanshow1.text = "China"

    def show_lan_text(self):
        self.dialog = MDDialog(
            size_hint=(0.9, 1),
            title="",
            type="confirmation",
            items=[
                ItemConfirm(text="English", on_press=self.lan01),
                ItemConfirm(text="Thai", on_press=self.lan02),
                ItemConfirm(text="Russia", on_press=self.lan03),
                ItemConfirm(text="France", on_press=self.lan04),
                ItemConfirm(text="Germany", on_press=self.lan05),
                ItemConfirm(text="Italy", on_press=self.lan011),
                ItemConfirm(text="Protugal", on_press=self.lan012),
                ItemConfirm(text="Japan", on_press=self.lan06),
                ItemConfirm(text="South-Korea", on_press=self.lan08),
                ItemConfirm(text="Spain", on_press=self.lan09),
                ItemConfirm(text="Lao", on_press=self.lan07),
                ItemConfirm(text="Vietnam", on_press=self.lan010),
                ItemConfirm(text="China", on_press=self.lan013),

            ],
            buttons=[
                MDFlatButton(text="Back", on_release=self.closeDialog),
            ],
        )
        self.dialog.open()

    #### input translate ####
    def lan10(self, *a2):
        global lan2
        lan2 = "en"
        self.ids.btnlanshow2.text = "English"

    def lan20(self, *a2):
        global lan2
        lan2 = "th"
        self.ids.btnlanshow2.text = "Thai"

    def lan30(self, *a2):
        global lan2
        lan2 = "ru"
        self.ids.btnlanshow2.text = "Russia"

    def lan40(self, *a2):
        global lan2
        lan2 = "fr"
        self.ids.btnlanshow2.text = "France"

    def lan50(self, *a2):
        global lan2
        lan2 = "de"
        self.ids.btnlanshow2.text = "Germany"

    def lan60(self, *a2):
        global lan2
        lan2 = "ja"
        self.ids.btnlanshow2.text = "Japan"

    def lan70(self, *a2):
        global lan2
        lan2 = "lo"
        self.ids.btnlanshow2.text = "Lao"

    def lan80(self, *a2):
        global lan2
        lan2 = "ko"
        self.ids.btnlanshow2.text = "South-Korea"

    def lan90(self, *a2):
        global lan2
        lan2 = "es"
        self.ids.btnlanshow2.text = "Spain"

    def lan100(self, *a2):
        global lan2
        lan2 = "vi"
        self.ids.btnlanshow2.text = "Vietnam"

    def lan110(self, *a2):
        global lan2
        lan2 = "it"
        self.ids.btnlanshow2.text = "Italy"

    def lan120(self, *a2):
        global lan2
        lan2 = "pt"
        self.ids.btnlanshow2.text = "Portugal"

    def lan130(self, *a2):
        global lan2
        lan2 = "zh-CN"
        self.ids.btnlanshow2.text = "China"

    def show_lan_tran(self):
        self.dialog = MDDialog(
            size_hint=(0.9, 1),
            title="",
            type="confirmation",
            items=[
                ItemConfirm(text="English", on_press=self.lan10),
                ItemConfirm(text="Thai", on_press=self.lan20),
                ItemConfirm(text="Russia", on_press=self.lan30),
                ItemConfirm(text="France", on_press=self.lan40),
                ItemConfirm(text="Germany", on_press=self.lan50),
                ItemConfirm(text="Italy", on_press=self.lan110),
                ItemConfirm(text="Protugal", on_press=self.lan120),
                ItemConfirm(text="Japan", on_press=self.lan60),
                ItemConfirm(text="South-Korea", on_press=self.lan80),
                ItemConfirm(text="Spain", on_press=self.lan90),
                ItemConfirm(text="Lao", on_press=self.lan70),
                ItemConfirm(text="Vietnam", on_press=self.lan100),
                ItemConfirm(text="China", on_press=self.lan130),
            ],
            buttons=[
                MDFlatButton(text="Back", on_release=self.closeDialog),
            ],
        )
        self.dialog.open()

    pass


class ItemConfirm(OneLineAvatarIconListItem):
    divider = None
    global check_list

    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False


class IItemConfirm(OneLineAvatarIconListItem):
    pass


class Screen03(Screen):
    dialog = None

    def __init__(self, **kwargs):
        super(Screen03, self).__init__(**kwargs)

    def closeDialog(self, inst):
        self.dialog.dismiss()

    def show_his(self):
        pass

sm = ScreenManager()
sm.add_widget(Screen01(name='main'))
sm.add_widget(Screen02(name='rec'))
sm.add_widget(Screen03(name='history'))


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(screen_helper)
        return screen


if __name__ == '__main__':
    MainApp().run()
