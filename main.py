import openpyxl
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from os.path import exists
from kivymd.uix.pickers import MDDatePicker
import functions
from kivy.utils import get_color_from_hex

Window.size = (350, 600)

class SplashScreen(Screen):
    pass

class Home(Screen):

    def on_pre_enter(self, *args): # ao gera a tela, a função é executada

        #verifica se já há um arquivo de dados salvo
        if not exists('Data\dados_base.xlsx'):
            print("Vou criar o arquivo")
            dataBase = openpyxl.Workbook()
            dataBase_sheet = dataBase['Sheet']
            dataBase_sheet.append(['Valor', 'Data', 'Para', 'Desc'])
            dataBase.create_sheet("Saldo")
            dataBase_saldo = dataBase["Saldo"]
            dataBase_saldo.append(['Saldo'])
            dataBase_saldo.append([0])

            # deixando em negrito os headers da tabela
            bold = openpyxl.styles.Font(bold=True)  # guardamos o estilo em uma variável
            for row in dataBase_sheet["A1:E1"]: # adicionamos esse estilo para cada célula
                for cell in row:
                    cell.font = bold
            dataBase_saldo['A1'].font = bold

            # Atualiza o valor do saldo na home screen

            linha = dataBase_saldo.max_row # pega a última linha /célula com valor
            print(linha)
            self.ids.saldo.text = 'R$ ' + str(dataBase_saldo[f'A{linha}'].value)

            dataBase.save('Data\dados_base.xlsx')
            dataBase.close()
        else:
            # Atualiza o valor do saldo na home screen
            print("O arquivo já foi criado")
            dataBase = openpyxl.load_workbook('Data\dados_base.xlsx')
            dataBase_saldo = dataBase["Saldo"]
            linha = dataBase_saldo.max_row  # pega a última linha /célula com valor
            print(linha)
            self.ids.saldo.text = 'R$ ' + str(dataBase_saldo[f'A{linha}'].value)



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


#editando a planilha base
            edit_base = openpyxl.load_workbook('dados_base.xlsx')
            edit_base_sheet = edit_base['Sheet']
            edit_base_sheet.append([self.date_read, self.termo_tanque, self.valor_read])
            edit_base.save('dados_base.xlsx')
            edit_base.close()

"""


class Transferir(Screen):

    # acessando id de um componente da tela:  self.ids.(nome do id).text(Se o text não for colocado, será apenas o endereço e não o valor do componente)

    def SaveInfo(self):
        dataBase = openpyxl.load_workbook('Data\dados_base.xlsx')
        dataBase_sheet = dataBase['Sheet']
        dataBase_saldo = dataBase['Saldo']

        valor = int(self.ids.valor.text)
        print(valor)
        para = str(self.ids.para.text)
        data = str(self.ids.data.text)
        desc = str(self.ids.desc.text)

        linha = dataBase_saldo.max_row
        saldo = dataBase_saldo[f'A{linha}'].value      # saldo mais recente
        if(saldo < valor):
            print('Não tem dinheiro')
        else:
            saldo_atual = (saldo - valor) # gambiarra temporária - não sei porque está diminuindo 2 do saldo atual
            print(saldo_atual)
            dataBase_saldo.append([saldo_atual])

        dataBase_sheet.append([valor, para, data, desc])
        dataBase.save('Data\dados_base.xlsx')
        dataBase.close()

    def Teste(self, instance, date_range, value):  # ajeitar
        self.date = str(value) # get the date
        print(self.date)
        self.ids.data.text = self.date  # shows it in text

    def show_date_picker(self):
        # estilando o date picker
        date_dialog = MDDatePicker(title="Selecione uma data", primary_color= get_color_from_hex("#002171"),
        accent_color= get_color_from_hex("#FFFFFF"),
        selector_color= get_color_from_hex("#5472D3"),
        text_toolbar_color= get_color_from_hex("#FFFFFF"),
        text_weekday_color= get_color_from_hex("#002171"),
        text_current_color= get_color_from_hex("#FFFFF"),
        text_button_color= get_color_from_hex("#002171"))
        date_dialog.bind(on_save=self.Teste)  # ajeitar
        date_dialog.open()

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
update the balance DONE
create a function to save data into the excel file
create a function to go through all the file´s data and show it on the recycler view(component)
create a function to open the excel file

 
"""