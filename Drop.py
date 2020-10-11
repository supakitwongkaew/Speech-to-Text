from kivymd.app import MDApp
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
import kivy.config
kivy.config.Config.set('graphics', 'width', '325')
kivy.config.Config.set('graphics', 'height', '560')

class CustomDropDown(BoxLayout):
    pass

class DropApp(MDApp):
    def build(self):
        return CustomDropDown()

if __name__=='__main__':
    DropApp().run()