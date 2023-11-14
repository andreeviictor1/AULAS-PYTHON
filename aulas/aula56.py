"""
split e join com list e str 
split - divide uma str
join - une uma str
"""

frase = 'olha so que, coisa interessante'
lista_palavra = frase.split(', ')

for i, frase in enumerate(lista_palavra):
    print(lista_palavra[i].lstrip())
    

print(lista_palavra)


frases_unidas = '-'.join(lista_palavra)
print(frases_unidas)