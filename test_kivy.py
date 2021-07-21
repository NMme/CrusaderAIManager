import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooser
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    file_pth = StringProperty()

    def show_load_list(self):
        content = LoadDialog(load=self.load_list, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load a file list", content=content, size_hint=(1, 1))
        self._popup.open()

    def load_list(self, path, filename):
        self.file_pth = path
        self._popup.dismiss()

    def dismiss_popup(self):
        self._popup.dismiss()


class LoadDialogApp(App):
    pass


if __name__ == '__main__':
    LoadDialogApp().run()
