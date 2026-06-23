# Lógicas e Decisões
# Se condição verdadeira
# Se condição ainda verdadeira porém com criterios
# Senao condição falsa
# if elif e else
# Sinais de > < =


# Exemplo 1
# print("Verificar idade")
# idade = int(input("Digite sua idade "))

# if idade >= 18:
#     print("Você é maior de idade")
# elif idade >= 16:
#     print("Você não é de maior porém pode votar")
# else:
#     print("Você não é de maior")

# Exemplo 2
# Valores
print("Checar valores")
valor = int(input("Digite um valor"))

if valor > 100:
    print("Valores acima de 100")
    print("O valor é", valor + 1)
    
else:
    print("Valores abaixo de 100")
    print("O valor é", valor - 1)

# Exemplo 3
# Criar um algoritmo que permita escolher a opção que deseja
print("Menu de Opção")
print("Escolha uma das opções")
print("Filmes F e Séries S e X para Sair")

escolha = input("Digite uma opção")

if escolha == "F":
    print("Você escolheu Filmes")
elif escolha == "S":
    print("Você escolheu Séries")
else:
    print("Você saiu do programa")

# Exercício 1
# Criar um algoritmo para realizar a locação de filmes ou séries seguir o modelo anterior. Ao escolher a opção você deverá perguntar o nome do cliente do filme ou série e quantidade que deseja assim como o valor de aluguel
# Para filmes R$ 5,00 e para séries R$ 10,00


