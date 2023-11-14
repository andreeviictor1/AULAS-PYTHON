"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.

- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.


- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.


- Se a letra digitada estiver na
palavra secreta; exiba a letra;


- Se a letra digitada não estiver
na palavra secreta; exiba *.

Faça a contagem de tentativas do seu
usuário.
"""
def jogo_adivinhacao(palavra_secreta):
    palavra_adivinhada = ['*'] * len(palavra_secreta)
    tentativas = 0
    letras_utilizadas = []

    while '*' in palavra_adivinhada:
        tentativa = input("\nDigite uma letra: ").lower()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        if tentativa in letras_utilizadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_utilizadas.append(tentativa)

        if tentativa in palavra_secreta:
            print("A letra está na palavra secreta!")
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == tentativa:
                    palavra_adivinhada[i] = tentativa
        else:
            print("A letra não está na palavra secreta.")
        
        tentativas += 1
        print('Palavra: ', ''.join(palavra_adivinhada))
        print('Letras utilizadas: ', ', '.join(letras_utilizadas))
    
    print(f"\nParabéns! Você adivinhou a palavra '{palavra_secreta}' em {tentativas} tentativas.")

# Palavra secreta (pode ser alterada)
palavra_secreta = "python"

# Iniciar o jogo
jogo_adivinhacao(palavra_secreta)
