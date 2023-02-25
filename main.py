import openpyxl
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from os.path import exists

Window.size = (350, 600)

class SplashScreen(Screen):
    pass

class Home(Screen):

    def on_enter(self, *args): # ao gera a tela, a função é executada
        if not exists('Data\dados_base.xlsx'):
            print("Vou criar o arquivo")
            dataBase = openpyxl.Workbook()
            dataBase_sheet = dataBase['Sheet']
            dataBase_sheet.append(['Valor', 'Data', 'Para', 'Desc', 'Saldo'])

            # deixando em negrito os headers da tabela
            bold = openpyxl.styles.Font(bold=True)
            for row in dataBase_sheet["A1:E1"]:
                for cell in row:
                    cell.font = bold

            dataBase.save('Data\dados_base.xlsx')
            dataBase.close()
        else:
            print("O arquivo já foi criado")



"""
book_base = openpyxl.Workbook()  # creating the excel file we'll be using
book_base_sheet = book_base['Sheet'] #selecting our sheet
book_base_sheet.append(['Data', 'Tanque', 'Leitura']) # adding to our sheet data (each word before the comma is a column)
book_base.save('dados_base.xlsx') # saving and giving the file a name
book_base.close() # closing our workbook


ft = Font(bold=True)
>>> for row in ws["A1:C1"]:
...     for cell in row:
...         cell.font = ft
"""


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

create a function to generate the excel file DONE
create a function to verify if there is already an excel file on the directory DONE
create a function to save data into the excel file
create a function to go through all the file´s data and show it on the recycler view(component)
create a function to open the excel file

 
"""