string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'e', 'legal'


salas = [
    #0             1
    ['Maria', 'Helena'], #0
    #  0
    ['Elaine'], #1
    # 0         1         2 
    ['Joao', 'Andre', 'Eduarda']
]


# a, b, *_, ap, u = lista
# print(a,b, ap)

# for nome in lista:
#     print(nome, end = ' ', sep = ' ')


# print(*lista)

print(*salas, sep ='\n')