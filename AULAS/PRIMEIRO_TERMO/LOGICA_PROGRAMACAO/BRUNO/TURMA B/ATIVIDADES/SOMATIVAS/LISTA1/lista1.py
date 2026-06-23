# 1. Perfil de Gamer: Peça o nick (nome) do jogador e o nível atual. Exiba: "O
# jogador [nick] está no nível [nível] e pronto para a partida!"

# if idade < 13:
#     print("Você é uma criança!")
# elif 13 > idade < 18:
#     print("Você é um adolescente!") 
# else:
#     print("Você é um adulto!")

# round(variavel,2)

# and ou or
# if idade == 18 or idade == 21:
#     print("Você é um jovem adulto!")

# for i in range(1, 11):
#     print(i)

# total = 0
# while True:
#     resposta = input("Deseja continuar? (s/n): ")
#     if resposta.lower() == 'n':
#         total += resposta
#         break
#     print("Continuando...")
# import time
# for a in range(6,1,-1):
#     time.sleep(1)
#     print(a)
    
# # 2. Calculadora Simples: Solicite dois números e uma operação (soma, subtração, multiplicação ou divisão). Realize a operação e exiba o resultado.
# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))    
# operacao = input("Digite a operação (soma, subtração, multiplicação ou divisão): ")
# if operacao == "soma":
#     resultado = num1 + num2
# elif operacao == "subtração":
#     resultado = num1 - num2
# elif operacao == "multiplicação":
#     resultado = num1 * num2
# elif operacao == "divisão":
#     resultado = num1 / num2

# print(f"O resultado da {operacao} é: {round(resultado, 2)}")

# lista = [];
# a = int(input("Digite um número: "))
# b = 20
# if lista > a:
#     lista += a

# 12.Monitoramento de Frota: Use um for para pedir a quilometragem de 5 veículos diferentes. Ao final, mostre qual foi a maior quilometragem registrada.
# veiculos = []
# for i in range(5):
#     km = float(input(f"Digite a quilometragem do veículo {i+1}: "))
#     veiculos.append(km)
# maior_km = max(veiculos)
# print(f"A maior quilometragem registrada é: {maior_km} km")


veiculos = []
for i in range(5):
    km = float(input(f"Digite a quilometragem do veículo {i+1}: "))
    veiculos.append(km)
maior_km = veiculos[0]
for km in veiculos:
    if km > maior_km:
        maior_km = km
print(f"A maior quilometragem registrada é: {maior_km} km")


cam = input("O caminhão fez checklist (concluido)")
mot = input("O motorista foi identificado (sim ou não)")

if cam == "concluido" and mot == "sim":
    print("Pronto pra seguir rota")


atraso = int(input("Peças com atraso"))

if atraso > atraso:
    pecas = atraso * 0.1
    print("Atraso na entrega",pecas)