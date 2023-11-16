import random

num_cpfs_a_gerar = 20

for _ in range(num_cpfs_a_gerar):
    nove_digitos = ''.join([str(random.randint(0, 9)) for _ in range(9)])

    contador_regressivo_1 = 10
    resultado_digito_1 = 0

    # Calcula o primeiro dígito verificador
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11
    resultado_digito_2 = 0

    # Calcula o segundo dígito verificador
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    # Gera o CPF completo
    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    print(cpf_gerado_pelo_calculo)
