### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome
try:
    nome = input('Digite seu nome: ')

    if len(nome) == 0:
        raise ValueError('Um nome deve ser digitado')
        exit()
    elif any(char.isdigit() for char in nome):
        raise ValueError('O nome contem numeros, isso não é permitido')
        exit()
    else:
        print('Nome valido: ', nome)
except ValueError as e:
    print(e)
    exit()
# 2) Solicita ao usuário que digite o valor do seu salário


# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?