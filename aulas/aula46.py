for i in range(10):
    if i == 2:
        print('i eh 2, pulando...')
        continue
    
    # if i == 8:
    #     print('i eh 8, seu else nao executara')
    #     break
    
    for j in range(1, 3):
        print(i, j)
else:
    print('For completado com sucesso')
