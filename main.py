from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (350, 580)


class SplashScreen(Screen):
    pass

class MiniBanco(MDApp):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name="splashScreen"))

        return sm

if __name__ == "__main__":
    MiniBanco().run()
