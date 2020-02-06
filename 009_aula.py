# def escrever_testo(texto):
#     arquivo = open('teste.txt', 'w')
#     arquivo.write(texto)
#     arquivo.close()
# def reescrever_testo(texto):
#     arquivo = open('teste.txt', 'a')
#     arquivo.write(texto)
#     arquivo.close()
#
# def ler_arquivo(nome_arquivo):
#     arquivo = open(nome_arquivo, 'r')
#     texto = arquivo.read()
#     print(texto)
#
# if __name__ == '__main__':
#     escrever_testo('Minha linha\n')
#     reescrever_testo('Segunda linha\n')
#     ler_arquivo('teste.txt')

def medias_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()

    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        print(aluno)
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        lista_media.append({aluno: media(lista_notas)})
        print(media(lista_notas))
    return lista_media

def arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write('Pedro, 8, 10, 2\n')
    arquivo.close()

if __name__ == '__main__':
    # arquivo('alunos.txt')
    print(medias_notas('alunos.txt'))