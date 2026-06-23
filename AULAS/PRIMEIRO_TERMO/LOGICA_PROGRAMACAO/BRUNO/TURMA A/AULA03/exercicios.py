# Exercício 1
# Criar um algoritmo para realizar a locação de filmes ou séries seguir o modelo anterior. Ao escolher a opção você deverá perguntar o nome do cliente do filme ou série e quantidade que deseja assim como o valor de aluguel
# Para filmes R$ 5,00 e para séries R$ 10,00

# print("Menu de Opção")
# print("Escolha uma das opções")
# print("Filmes F e Séries S e X para Sair")

# escolha = input("Digite uma opção ")

# if escolha == "F":
#     print("Você está na sessão Filmes")
#     nome = input("Digite seu nome")
#     filmes = input("Qual filme deseja? ")
#     qtde = int(input("Qual quantidade deseja"))
#     valor = 5
#     total = qtde * valor
#     # print("Parabéns pela sua locação de filmes", nome, "E seu filme foi:", filmes, "A quantidade foi", qtde, "E sua locação custou", valor )
#     print("Parabéns pela locação:", nome)
#     print("O filme que escolheu foi:", filmes)
#     print("Quantidade de vezes que pode assistir:", qtde)
#     print("O valor da locação foi de:", valor)
#     print("O total da sua locação foi:", total)

# elif escolha == "S":
#     print("Você está na sessão Séries")
# else:
#     print("Você saiu do programa")

# Exercicio 2
# Loja de Comidas e Doces
# Criar um algoritmo para compra de produtos
# 1 - Comida
# 2 - Bebida
# 3 - Doces
# Ao escolher as opções cada um terá um valor de porcentagem, comida = 10%, bebida = 5%, Doces 2%
# calcular porcentagem valor / 100 ou valor * valor / 100
print("Bem-Vindo a nossa loja de conveniências")
print("Temos Comida, Bebida e Doce")
print("Digite a opção que deseja para iniciar")
print("Comida - Digite 1")
print("Bebida - Digite 2")
print("Doce - Digite 3")

opcao = int(input("Digite sua opção"))
if opcao == 1:
    print("Você está em Comida ")
    print("Temos PF , À la Carte")
    comida = input("O que deseja? ")
    valor = float(input("Digite o valor da comida "))
    desconto = valor * 10 / 100
    total = valor - desconto
    print("Sua compra total foi de: ", total)

# Exercício 3
# Calculadora com operadores
# Sua calculadora deverá perguntar qual operador ele deseja e calcular os valores desejados. # operador + - / *

print("Calculadora com operadores")
print("")

# Exercicio 4
# Calculo de Notas
# Nossas atividades são por base de calculo em somativa 1 e somativa 2, no final temos um média.
# Acima ou igual a 50 o aluno será aprovado caso contrario reprovado
# O programa deverá perguntar o nome , as notas e apresentar o resultado final do aluno

# Exercicio 5
# Criar um algoritmo para calcular uma viagem de carro, ônibus e avião
# Viagens de carro: Deve ser feito um abastecimento e deve cobrar o valor do pedagio
# Ônibus: Deve ser cobrado o valor da passagem e o valor do seguro de 3,88
# Avião: Cobrar o valor da viagem e valor de taxa de embarque 55,20