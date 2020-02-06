from datetime import date, time
def workofdate():
    data_atual = date.today()
    print(data_atual)

    data_str = data_atual.strftime('%d/%m/%Y %A %B %Y')

    print(type(data_str))

def workoftime():
    horario = time(hour=15, minute=18, second=40)
    print(horario)

if __name__ == '__main__':
    workofdate()
    workoftime()
    data_atual = date.today()
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo', 'Domingo')
    print(tupla[data_atual.weekday()])