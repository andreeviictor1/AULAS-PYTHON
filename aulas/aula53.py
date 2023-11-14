lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')

lista_enumerada = list(enumerate(lista))


for item in lista_enumerada:
    print(item)
print(lista_enumerada)


for item in enumerate(lista):
    indice, nome = item 
    print(indice, nome)