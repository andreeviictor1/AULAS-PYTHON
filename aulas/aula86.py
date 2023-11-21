x = 1

def escopo():
    global x  # Indica que você está referenciando a variável global x
    x = 10
    
    def outra_funcao():
        global x  # Se você quiser modificar x globalmente aqui, descomente esta linha
        x = 15
        y = 2
        print(x, y)
    
    outra_funcao()
    # print(x)

print(x)
escopo()
print(x)