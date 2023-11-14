"""
peca ao usuario para digitar seu nome
peca ao usuario digitar sua idade
se nome e idade forem digitados:
    Exiba:
        seu nome e {nome}
        seu nome inverdido e {nome invertido}
        seu nome contem (ou nao) espacos
        seu nome tem {n} letras
        a primeira letra do seu nome e {letra}
        a ultima letra do seu nome e {letra}
Se nada for digitado em nome ou idade:
    exiba"desculpe, voce deixou campos vazios"
"""

nome_usuario = input('Digite seu nome: ')
idade_usuario = input('Digite sua idade: ')


if nome_usuario and idade_usuario:
    print(f'Seu nome e {nome_usuario}')
    print(f'Seu nome invertido e {nome_usuario[::-1]}')
    
    if ' ' in nome_usuario:
        print("Seu nome contem espaco")
    else:
        print("Seu nome nao contem espaco")
    
    print(f'Seu nome tem {len(nome_usuario)} letras')
    print(f'A primeira letra do seu nome e {nome_usuario[0]} ')
    print(f'A ultima letra do seu nome e {nome_usuario[-1]} ')
else:
    print('Desculpe, voce deixou campos vazios')