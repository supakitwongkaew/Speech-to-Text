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
from kivy.properties import StringProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.list import OneLineAvatarIconListItem

# -*- coding: utf-8 -*-

Window.size = (330, 560)

language = ['th', 'en']
font = ['FC Motorway Regular.otf', 'ABeeZee-Regular.otf']

screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    
<MenuScreen>:
    name: 'menu'
    Label
        id: showlan
        text: 'show lan '
        halign: 'center'
        pos_hint: {'center_x':0.8,'center_y':0.85}

    Label
        id: speechtotext
        text: 'Speech to Text'
        halign  :'center'
        pos_hint:{'center_x': 0.3, 'center_y': 0.93} 
        font_style:'Subtitle1' 
        font_size:25
    MDLabel
        id : text
        text: 'Text' 
        theme_text_color:"Custom"
        text_color:(255 / 255, 195 / 255, 0 / 255)
        halign:'center'
        pos_hint:{'center_x': 0.17, 'center_y': 0.85}
        font_style:'Subtitle2'
        
    Label
        id : youtext
        text:'test'
        halign:'center' 
        pos_hint:{'center_x': 0.5, 'center_y': 0.78}
  
    MDRectangleFlatButton:
        id : btnrec
        text: 'Record'
        pos_hint: {'center_x':0.5,'center_y':0.15}
        on_press:  root.change()
        
    MDFlatButton:
        id : btnclear
        text: 'Clear'
        pos_hint: {'center_x':0.83,'center_y':0.20}
        on_press: root.clear()
    MDFlatButton
        id : lanchoose
        text: 'Language'
        halign:'center'
        pos_hint: {'center_x':0.15,'center_y':0.2}
        on_press: root.manager.current = 'pix'
        
<ProfileScreen>:
    name: 'pix'
    Label
        id : youtext2
        text:'test'
        halign:'center' 
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    MDFlatButton
        id : lanchoose
        text: 'Language'
        halign:'center'
        pos_hint: {'center_x':0.15,'center_y':0.2}
        on_press: root.manager.current = 'menu'
    MDFlatButton
        id : enbtn
        text: 'English'
        halign:'center'
        pos_hint: {'center_x':0.2,'center_y':0.8}
        on_press: root.enbtn()
    MDFlatButton
        id : thbtn
        text: 'Thai'
        halign:'center'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press: root.thbtn()
        
    MDFlatButton
        id : xxx
        text: 'xxx'
        halign:'center'
        pos_hint: {'center_x':0.15,'center_y':0.4}
        on_press: root.change2()
"""


class MenuScreen(Screen):
    def change(self):
        global txt
        global x
        txt = 'cheer boi'
        self.ids.youtext.text = x
        self.ids.showlan.text = x
        print(txt)

    def clear(self):
        self.ids.youtext.text = ' '

    def lanlink(self):
        global x
        self.ids.showlan.text = x

    pass

class ProfileScreen(Screen):
    def change2(self):
        global txt
        global x
        x = "sawat-dee"
        self.ids.youtext2.text = x
        print(x)

    def thbtn(self):
        global x
        x = "Thai"
        self.ids.youtext2.text = x

    def enbtn(self):
        global x
        x = "English"
        self.ids.youtext2.text = x
    pass
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='pix'))

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.theme_style = "Dark"

        screen = Builder.load_string(screen_helper)

        return screen


if __name__ == '__main__':
    MainApp().run()
