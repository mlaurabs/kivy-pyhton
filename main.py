from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (350, 600)


class SplashScreen(Screen):
    pass

class Home(Screen):
    def chama(self):
        print("ola")

class MiniBanco(MDApp):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name="splashScreen"))
        sm.add_widget(Home(name="home"))
        return sm

if __name__ == "__main__":
    MiniBanco().run()
