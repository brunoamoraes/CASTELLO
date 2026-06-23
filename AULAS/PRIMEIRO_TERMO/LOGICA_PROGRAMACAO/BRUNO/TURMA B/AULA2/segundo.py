# Condições Lógicas e Decisões
# O programa toma caminhos diferentes dependendo da condição.
# Funções de Lógicas SE e Senão
# If , elif e else
# if = Se (verdadeiro)
# elif = Continua sendo (verdadeiro)
# else = Falso

# Exemplo 1
# print("Bem-Vindo as Lógicas e Decisões")
# print("Para iniciar digite a opção desejada")
# print("Digite 1 para Filmes e 2 para Séries e para 3 Novelas")

# escolha = int(input("Digite a opção que deseja: "))

# if escolha == 1:
#     print("Você escolheu Filmes")
# elif escolha == 2:
#     print("Você escolheu Séries")
# elif escolha == 3:
#     print("Você escolheu Novelas")
# else:
#     print("Você não escolheu nenhum opção do catalogo")

# # Exemplo 2
# print("Pokémon")
# print("Escolha seu personagem")
# print("Pikachu = P")
# print("Charizard = C")
# print("Mewtwo = M")

# pokemons = input("Digite o letra do seu personagem")

# if pokemons == "P":
#     print("Você escolheu o PIKACHU")
# elif pokemons == "C":
#     print("Você escolheu o CHARIZARD")
# elif pokemons == "M":
#     print("Você escolheu o MEWTWO")
# else:
#     print("Espero você na próxima, até mais!!")

# Exemplo 3
# Valores númericos e flutuantes
print("Valores")
print("Comparações de números")

numeros = int(input("Digite um número"))

if numeros > 100:
    print("Número Alto")
elif numeros < 100:
    print("Número Baixo")
else:
    print("Escolher um valor que não temos")

