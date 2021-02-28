from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

class Container(GridLayout):
    #назначаем нормальные свойства, импортировав ObjectProperty
    #ObjectProperty - создает ссылку на объект в питоне(почти для всех типов данных)
    text_input = ObjectProperty()
    label_widget = ObjectProperty()
    def change_text(self):
        #ставим текст у Label = тексту у TextInput
        #используя указанные нами новые свойства
        self.label_widget.text = self.text_input.text


class EventApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    EventApp().run()