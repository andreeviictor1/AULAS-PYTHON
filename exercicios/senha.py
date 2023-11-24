import re

usuarios = {}

while True:
    print("Bem-vindo ao sistema!")

    if not usuarios:
        print("Não há usuários cadastrados. Vamos criar uma conta!")
        username = input("Digite o nome do seu usuário: ")
        senhauser = input("Digite sua senha: ")
        senhaconfirmacao = input("Confirme a sua senha: ")

        if senhaconfirmacao == senhauser and len(senhaconfirmacao) >= 5 and any(char.isupper() for char in senhaconfirmacao) and re.search("[!@#$%^&*(),.?\":{}|<>]", senhaconfirmacao):
            print("Conta criada com sucesso!")
            usuarios[username] = senhaconfirmacao
        else:
            print("Senha não atende aos critérios. Por favor, tente novamente.")
    else:
        # Verificar se o usuário já possui uma conta
        opcao = input("Você já possui uma conta? (s/n): ").lower()

        if opcao == 's':
            # Entrar com usuário existente
            username = input("Digite o nome do seu usuário: ")
            senha = input("Digite sua senha: ")

            # Verificar se o usuário e senha correspondem
            if username in usuarios and usuarios[username] == senha:
                print(f"Bem-vindo de volta, {username}!")
            else:
                print("Usuário ou senha incorretos. Tente novamente.")
        elif opcao == 'n':
            # Criar uma nova conta
            username = input("Digite o nome do seu usuário: ")
            senhauser = input("Digite sua senha: ")
            senhaconfirmacao = input("Confirme a sua senha: ")

            if senhaconfirmacao == senhauser and len(senhaconfirmacao) >= 5 and any(char.isupper() for char in senhaconfirmacao) and re.search("[!@#$%^&*(),.?\":{}|<>]", senhaconfirmacao):
                print("Conta criada com sucesso!")
                usuarios[username] = senhaconfirmacao
            else:
                print("Senha não atende aos critérios. Por favor, tente novamente.")
        else:
            print("Opção inválida. Por favor, escolha 's' para entrar ou 'n' para criar uma conta.")

    # Verificar se o usuário deseja continuar
    continuar = input("Deseja continuar? (s/n): ").lower()
    if continuar != 's':
        break  # Sai do loop principal se o usuário não deseja continuar

# Restante do seu código aqui...

print("Usuários cadastrados:")
for user, senha in usuarios.items():
    print(f"Usuário: {user}, Senha: {senha}")