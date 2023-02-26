from kivymd.uix.pickers import MDDatePicker


def Teste(self, instance, date_range, value):  # ajeitar
    print('peguei a data')

def show_date_picker(self):
    date_dialog = MDDatePicker()
    date_dialog.bind(on_save=self.Teste)  # ajeitar
    date_dialog.open()
