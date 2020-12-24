'''Чтобы создать файл разметки .kv нужно убрать последние
три буквы класса (например MyApp(App) > my.kv)
'''


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Container(BoxLayout):#boxlayout по умолчанию использует горизонтальную ориентацию
    pass


class MyApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    MyApp().run()