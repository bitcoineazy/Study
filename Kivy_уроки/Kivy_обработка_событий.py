from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class Container(GridLayout):
    pass


class EventApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    EventApp().run()