
lista = [1, 10]
try:
    x=1
    div = 10 / 1
    n = lista[1]

except ZeroDivisionError:
    print("Erro meu bom")
except IndexError:
    print("Erro meu bom 2")
except BaseException as ex:
    print(ex)
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('close')