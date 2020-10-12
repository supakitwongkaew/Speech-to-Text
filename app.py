from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import speech_recognition as sr
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
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
        text:"History"
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
        theme_text_color:"Custom"
        text_color:(255 / 255, 255 / 255, 255 / 255)
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_release : root.on_start()


    Label
        id : histext01
        text:''
        halign:'center'
        font_name:"arial-unicode-ms.otf"
        pos_hint:{'center_x': 0.5, 'center_y': 0.53}
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
                    if num > 10:
                        if num % 10 == 1:
                            his_all[0] = word
                            his_all[1] = result
                            num = num + 1
                        elif num % 10 == 2:
                            his_all[2] = word
                            his_all[3] = result
                            num = num + 1
                        elif num % 10 == 3:
                            his_all[4] = word
                            his_all[5] = result
                            num = num + 1
                        elif num % 10 == 4:
                            his_all[6] = word
                            his_all[7] = result
                            num = num + 1
                        elif num % 10 == 5:
                            his_all[8] = word
                            his_all[9] = result
                            num = num + 1
                        elif num % 10 == 6:
                            his_all[10] = word
                            his_all[11] = result
                            num = num + 1
                        elif num % 10 == 7:
                            his_all[12] = word
                            his_all[13] = result
                            num = num + 1
                        elif num % 10 == 8:
                            his_all[14] = word
                            his_all[15] = result
                            num = num + 1
                        elif num % 10 == 9:
                            his_all[16] = word
                            his_all[17] = result
                            num = num + 1
                        elif num % 10 == 0:
                            his_all[18] = word
                            his_all[19] = result
                            num = num + 1
                    elif num > 20:
                        num = 10
                    else:
                        num = num + 1
                        print(num)
                        his_all.append(word)
                        his_all.append(result)
            except sr.UnknownValueError:
                self.ids.youtext.text = ("Error")
            except sr.RequestError as e:
                self.ids.youtext.text = ("Error".format(e))
            print(his_all)
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
    global his_all

    def __init__(self, **kwargs):
        super(Screen03, self).__init__(**kwargs)

    def closeDialog(self, inst):
        self.dialog.dismiss()

    def hisshow01(self, *a3):
        global his_all
        if len(his_all) == 0:
            self.ids.histext01.text = "No History"
        else:
            ty = ("You word" + "\n" + (his_all[0]) + "\n" + "-----------------------------------------------------"
                  + "\n" + "You Translate" + "\n" + (his_all[1]))
            self.ids.histext01.text = (ty)

    def hisshow02(self, *a3):
        global his_all
        if len(his_all) <= 2:
            self.ids.histext01.text = "No History"
        else:
            ty = ("You word" + "\n" + (his_all[2]) + "\n" + "-----------------------------------------------------"
                  + "\n" + "You Translate" + "\n" + (his_all[3]))
            self.ids.histext01.text = (ty)

    def hisshow03(self, *a3):
        global his_all
        if len(his_all) <= 4:
            self.ids.histext01.text = "No History"
        else:
            ty = ("You word" + "\n" + (his_all[4]) + "\n" + "-----------------------------------------------------"
                  + "\n" + "You Translate" + "\n" + (his_all[5]))
            self.ids.histext01.text = (ty)

    def hisshow04(self, *a3):
        global his_all
        if len(his_all) <= 6:
            self.ids.histext01.text = "No History"
        else:
            ty = ("You word" + "\n" + (his_all[6]) + "\n" + "-----------------------------------------------------"
                  + "\n" + "You Translate" + "\n" + (his_all[7]))
            self.ids.histext01.text = (ty)

    def hisshow05(self, *a3):
        global his_all
        if len(his_all) <= 8:
            self.ids.histext01.text = "No History"
        else:
            ty = ("You word" + "\n" + (his_all[8]) + "\n" + "-----------------------------------------------------"
                  + "\n" + "You Translate" + "\n" + (his_all[9]))
            self.ids.histext01.text = (ty)

    def hisshow06(self, *a3):
        global his_all
        if len(his_all) <= 10:
            self.ids.histext01.text = "No History"
        else:
            ty = ("You word" + "\n" + (his_all[10]) + "\n" + "-----------------------------------------------------"
                  + "\n" + "You Translate" + "\n" + (his_all[11]))
            self.ids.histext01.text = (ty)

    def hisshow07(self, *a3):
        global his_all
        if len(his_all) <= 12:
            self.ids.histext01.text = "No History"
        else:
            ty = ("You word" + "\n" + (his_all[12]) + "\n" + "-----------------------------------------------------"
                  + "\n" + "You Translate" + "\n" + (his_all[13]))
            self.ids.histext01.text = (ty)

    def hisshow08(self, *a3):
        global his_all
        if len(his_all) <= 14:
            self.ids.histext01.text = "No History"
        else:
            ty = ("You word" + "\n" + (his_all[14]) + "\n" + "-----------------------------------------------------"
                  + "\n" + "You Translate" + "\n" + (his_all[15]))
            self.ids.histext01.text = (ty)

    def hisshow09(self, *a3):
        global his_all
        if len(his_all) <= 16:
            self.ids.histext01.text = "No History"
        else:
            ty = ("You word" + "\n" + (his_all[16]) + "\n" + "-----------------------------------------------------"
                  + "\n" + "You Translate" + "\n" + (his_all[17]))
            self.ids.histext01.text = (ty)

    def hisshow010(self, *a3):
        global his_all
        if len(his_all) <= 18:
            self.ids.histext01.text = "No History"
        else:
            ty = ("You word" + "\n" + (his_all[18]) + "\n" + "-----------------------------------------------------"
                  + "\n" + "You Translate" + "\n" + (his_all[19]))
            self.ids.histext01.text = (ty)

    def on_start(self):
        self.dialog = MDDialog(
            size_hint=(0.9, 1),
            title="History",
            type="confirmation",
            items=[
                IItemConfirm(text="01", on_press=self.hisshow01),
                IItemConfirm(text="02", on_press=self.hisshow02),
                IItemConfirm(text="03", on_press=self.hisshow03),
                IItemConfirm(text="04", on_press=self.hisshow04),
                IItemConfirm(text="05", on_press=self.hisshow05),
                IItemConfirm(text="06", on_press=self.hisshow06),
                IItemConfirm(text="07", on_press=self.hisshow07),
                IItemConfirm(text="08", on_press=self.hisshow08),
                IItemConfirm(text="09", on_press=self.hisshow09),
                IItemConfirm(text="10", on_press=self.hisshow010),
                IItemConfirm(text=" "),
            ],
            buttons=[
                MDFlatButton(text="Back", on_release=self.closeDialog),
            ],
        )
        self.dialog.open()

    pass


sm = ScreenManager()
sm.add_widget(Screen01(name='main'))
sm.add_widget(Screen02(name='rec'))
sm.add_widget(Screen03(name='history'))


class Speech_to_TextApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(screen_helper)
        return screen


if __name__ == '__main__':
    Speech_to_TextApp().run()
