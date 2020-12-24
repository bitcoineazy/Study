from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class FloatPosing(FloatLayout):
    pass


class FloatApp(App):
    def build(self):
        return FloatPosing()


if __name__ == '__main__':
    FloatApp().run()