from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (350, 600)

class SplashScreen(Screen):
    pass

class Home(Screen):
    def chama(self):
        print("ola")


class Transferir(Screen):
    pass

class Depositar(Screen):
    pass

class MiniBanco(MDApp):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name="splashScreen"))
        sm.add_widget(Home(name="home"))
        sm.add_widget(Transferir(name="transferir"))
        sm.add_widget(Depositar(name="depositar"))

        return sm

if __name__ == "__main__":
    MiniBanco().run()

"""
Tasks for back-end:

create a function to generate the excel file
create a function to verificate if there is already an excel file on the directory
create a function to save data into the excel file
create a function to go through all the file´s data and show it on the recycler view(component)
create a function to open the excel file

 
"""