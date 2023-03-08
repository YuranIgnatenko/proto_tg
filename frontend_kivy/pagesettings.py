
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class PagesSettings():
    def get(self):
        root = BoxLayout()
        btn = Button(text="settings")
        root.add_widget(btn)
        return root