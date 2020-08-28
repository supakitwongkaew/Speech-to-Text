from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import  Screen
from kivymd.uix.button import MDFlatButton

class speech_to_textApp(MDApp):
    def build(self):
        screen = Screen()
        label = MDLabel(text='Speech to Text',halign='center')
        btn_flat = MDFlatButton(text='start',
                                pos_hint={'center_x':0.50,'center_y':0.4})

        screen.add_widget(btn_flat)
        screen.add_widget(label)
        return screen


speech_to_textApp().run()