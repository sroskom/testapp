from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.storage.jsonstore import JsonStore
import os.path
import sys
import testapp_constants as AppCnst

class RootWidget(Carousel):
    def getUserDataDir(self, *args):
        return App.get_running_app().user_data_dir
    
    def printException(self, expt, *args):
        print(expt)
        exptStr = (str(expt[0])+'\n'+str(expt[1])+'\n'+str(expt[2]))
        self.ids.lblexp.text = exptStr
        self.load_slide(self.ids.debugslide)
        
    def getSaveFilePath(self, *args):
        savefilepath = ''
        try:
            savefilepath = os.path.join(self.getUserDataDir(),'testapp_savefile.txt')
        except:
            self.printException(sys.exc_info())
        return savefilepath
    
    def incrementCount(self, *args):
        try:
            cntText = self.ids.cnt.text
            self.ids.cnt.text = str(int(cntText)+1)
            store = JsonStore(self.getSaveFilePath())
            store['p1'] = {'count':self.ids.cnt.text,'test':'testdata'}
        except:
            self.printException(sys.exc_info())
        
    def getCount(self, *args):
        cntText = '0'
        try:
            store = JsonStore(self.getSaveFilePath())
            if store.exists('p1'):
                cntText = str(store['p1']['count'])
        except:
            self.printException(sys.exc_info())
        return cntText

    def setScatterImage(self, *args):
        codeInp = self.ids.codeInp.text.strip()
        if codeInp in AppCnst.CODES:
            self.ids.scatterimg.source = AppCnst.CODES[codeInp]
        self.load_slide(self.ids.scatterslide)
    
class TempApp(App):
    def on_pause(self, *args):
        return True
    def build(self, *args):
        return RootWidget()

if __name__ == '__main__':
    TempApp().run()
