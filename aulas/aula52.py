# Tipo tupla - uma lista mutavel

nomes = ['Maria', 'Helena', 'Luiz']
# nomes[1] = 'Andre'
# _, _, nome, *resto = nomes
# print(nome)
# print(nomes)

nomes = tuple(nomes)
print(nomes)


lista = [10, 20, 30, 40]
lista.remove(20)
print(lista)
lista.pop(0)
print(lista)