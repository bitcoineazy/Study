from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        boxlay = BoxLayout()
        button1 = Button(text='Hello')
        button2 = Button(text='World')
        boxlay.add_widget(button1)
        boxlay.add_widget(button2)
        return boxlay

if __name__ == '__main__':
    MyApp().run()