"""
Interavel -> str, range, etc (__iter__)
Interador -> quem sabe entregar um valor por vez
Next -> me entregue o proximo valor
Iter -> me entregue o seu interador
"""



texto = ('Andre')
iterator = iter(texto)

while True:
    try:
        letra = next(iterator)
        print(letra)
    except StopIteration:
        break
    
"""
    Mesma coisa que utilizando o for
"""

# for letra in texto:
#     print(letra)
    