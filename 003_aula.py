# a = int(input('Primeiro valor'))
#
# b = int(input('Segundo valor'))
#
# c = int(input('Terceiro valor'))
#
# if a > b and a > c:
#     print('O maior valor é: {}'.format(a))
# elif b > a and b > c:
#     print('O maior valor é: {}'.format(b))
# else:
#     print('O maior é: {}'.format(c))

a = int(input('Entre com um valor: '))

resto = a % 2

if resto == 0:
    print('numero é par')
else:
    print('numero é impar')
