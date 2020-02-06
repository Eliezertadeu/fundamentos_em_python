# conjunto = {1,2,3,4}
# conjunto.add(5)
# conjunto.discard(1)
# print(conjunto)

# conjunto = {1,2,3,4,5,8}
# conjunto2 = {6,7,8,9}
# conjuntoUniao = conjunto.union(conjunto2)
# print(conjuntoUniao)
#
# conjuntoInterseccao = conjunto.intersection(conjunto2);
# print(conjuntoInterseccao)
#
# conjuntoDif = conjunto.difference(conjunto2)
# conjuntoDif2 = conjunto2.difference(conjunto)
# print(conjuntoDif)
# print(conjuntoDif2)
#
# conjunto_diff_simetric = conjunto.symmetric_difference(conjunto2);
# print(conjunto_diff_simetric)

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,6,7}
conjunto_subset = conjunto_a.issubset(conjunto_b);
print(conjunto_subset)

conjunto_superset = conjunto_a.issuperset(conjunto_b)

print(conjunto_superset)

lista = ['cachorro', 'cachorro', 'gato', 'gato' ]
conjunto_animais = set(lista)
print(conjunto_animais)