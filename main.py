from kivy.app import App

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.storage.jsonstore import JsonStore

class CustomWidget(Widget):
    def invest(self, *args):
        bank = self.ids.bnk.text
        count = self.ids.cnt.text
        self.ids.bnk.text = str(int(bank)+int(count))
        self.ids.cnt.text = '0'
        store = JsonStore('db.json')
        store['p1'] = {'bank':self.ids.bnk.text}
        print store['p1']
    def getBank(self, *args):
        store = JsonStore('db.json')
        if store.exists('p1'):
            return str(store['p1']['bank'])
        else:
            store['p1'] = {'bank':'0'}
            return '0'

class TempApp(App):
    def on_pause(self):
        return True
    def build(self, *args):
        return CustomWidget()

if __name__ == '__main__':
    TempApp().run()
