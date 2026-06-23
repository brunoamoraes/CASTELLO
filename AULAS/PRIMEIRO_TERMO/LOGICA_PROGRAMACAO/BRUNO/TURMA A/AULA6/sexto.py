# # Foco: print, input, operações matemáticas e f-strings
# # 1. Registro de Veículo: Peça o modelo do veículo e a placa.
# # ○ Exiba: "Veículo [Modelo] de placa [Placa] registrado no sistema. Boa viagem!"
# print("Registro de Veículo")
# modelo = input("Qual é o modelo do veículo?...")
# placa = input("Qual é a placa do veículo?...")
# print(f"Veículo {modelo} de placa {placa} registrado no sistema. Boa viagem!")

# # 2. Cálculo de Autonomia: Peça a capacidade do tanque de combustível (em litros) e o consumo médio do caminhão (km/l).
# # ○ Calcule e exiba a distância total que o veículo pode percorrer com o tanque cheio.
# print("Cálculo de Autonomia")
# tanque = float(input("Qual é a capacidade de seu tanque em Litros"))
# consumo = float(input("Digite o consumo médio por caminhão em Km/L"))
# total = tanque / consumo
# print(f"Seu caminhão pode percorrer {total:.2f} em Km/l")
# print("Seu caminhão pode percorrer", round(total,2), "em Km/l")

# # 3. Conversor de Moeda (Frete Internacional): O sistema lê o valor de um frete em Dólar (USD). Converta para Real (BRL) considerando a taxa de $1,00~USD \approx 5,00~BRL$ e exiba com duas casas decimais.
# print("Conversor de Moeda (Frete Internacional)")
# valor_reais = float(input("Qual é o valor em Reais que será convertido?..."))
# taxa_dolar = float(input("Qual é o valor da taxa em dolar em Reais?..."))
# total = valor_reais / taxa_dolar
# print(f"O valor total convertido é... {total:.2f}")

# # 4. Média de Entrega: Peça o tempo de entrega (em horas) de 3 rotas diferentes realizadas por um motorista. ○ Exiba a média aritmética simples do tempo dessas entregas.
# print("Média de Entrega")
# tempo1 = int(input("Qual foi o tempo para concluir a rota 1 em horas"))
# tempo2 = int(input("Qual foi o tempo para concluir a rota 2 em horas"))
# tempo3 = int(input("Qual foi o tempo para concluir a rota 3 em horas"))
# media = (tempo1 + tempo2 + tempo3) / 3
# print(f"A média {media:.2f} de tempo das entregas ")

# Foco: if, elif, else e operadores lógicos
# 5. Monitor de Carga: Peça o peso atual de um caminhão em toneladas.
# ○ Abaixo de 10t: "Carga Leve".
# ○ Entre 10t e 25t: "Carga padrão".
# ○ Acima de 25t: "ALERTA: Excesso de Peso!".
# print("Monitor de Carga")
# peso = float(input("Qual é o peso atual do seu caminhão?... "))

# if peso < 10:
#     print("Carga Leve")
# elif peso <= 25:
#     print("Carga padrão")
# else:
#     print("ALERTA: Excesso de Peso!")

# # 6. Classificador de Destino: O usuário insere o código da carga. Se começar com "N", exiba "Região Norte". Se começar com "S", "Região Sul". Para qualquer outro, "Região Internacional".
# print("Classificador de Destino")
# print("Regiões = N - Região Norte , S - Região Sul , Qualquer Outra - Internacional")
# regiao = input("Inserir o código da Região: ").lower()
# if regiao == "N".upper() or regiao == "n".lower():
#     print("Região Norte")
# elif regiao == "S":
#     print("Região Sul")
# else:
#     print("Região Internacional")

# # 7. Liberação de Saída: O caminhão só pode sair se o checklist == "concluído" E o motorista_identificado == "sim". Peça esses dois inputs e informe se o veículo está autorizado a iniciar a rota.
# print("Liberação de Saída")
# checklist = input("O checklist foi concluído? [Concluído ou Não Concluído]")
# motorista = input("O motorista foi identificado? [Sim ou Não]")
# if checklist == "Concluído" and motorista == "Sim":
#     print("Veículo autorizado a iniciar a rota.")
# else: 
#     print("Veículo NÃO autorizado a iniciar a rota. Verificar checklist e identificação do motorista.")

# # 8. Cálculo de Atrasos: Peça o total de entregas agendadas e o total de entregas realizadas com atraso. ○ Se o índice de atraso for maior que 10% do total, exiba "Necessário Otimizar
# # Rotas", caso contrário, "Logística Eficiente".
# print("Cálculo de Atrasos")
# total_entregas = int(input("Total de Entregas Agendadas:..."))
# total_atrasos = int(input("Total de Entregas em Atrasos:..."))
# if total_atrasos > total_entregas * 0.1:
#     print("Necessário otimizar rotas")
# else: 
#     print("Logística Eficiente")

# # 9. Validação de Calibragem: Um pneu de carga deve ter pressão entre 100 PSI e 110 PSI. Peça a medida e diga se está dentro do padrão, acima ou abaixo do recomendado.
# print("Validação de Calibragem")
# pressao = float(input("Digite a pressão do pneu em PSI:..."))
# if 100 <= pressao <= 110:
#     print("Dentro do padrão")
# elif pressao < 100:
#     print("Abaixo do recomendado")
# else: 
#     print("Acima do recomendado")

# 10.Contagem de Embarque: Use um for para fazer uma contagem regressiva de 5 até 1 para o fechamento do portão de embarque e finalize com "Portão Trancado!".
# print("Contagem de Embarque")
# import time
# for contagem in range(5,0,-1):
#     time.sleep(1)
#     print(contagem)
# print("Portão Trancado")

# 11. Somatório de Fretes (Acumulador): Use um while para pedir o valor do frete de vários pedidos.
# ○ O loop para quando o usuário digitar 0. No fim, mostre o faturamento total acumulado.
print("Somatório de Frete (Acumulador)")
total = 0
while True:
    valor = float(input("Valor do Frete: "))
    if valor == 0:
        break  
    total += valor
    print(f"Total acumulado {total} do Frete")
print("Fim do cálculo de fretes.")

print("Somatório de Frete (Acumulador) - Versão 2")
faturamento_total = 0
valor_frete = -1
while valor_frete != 0:
    valor_frete = float(input("Valor do Frete ou 0 para encerrar"))
    faturamento_total += valor_frete
    print(f"Faturamento acumulado: R$ {faturamento_total}")
print("Cálculo executado com sucesso")

print("Somatório de Frete (Acumulador) - Versão 3")
b = 0
while True:
    t = int(input("Valor Frete..."))
    c = input("Quer continuar s/n")
    b += t
    if c == "s":
        continue
    else:
        break
print(f"Faturamento total{b}acumulado")

# 12.Monitoramento de Frota: Use um for para pedir a quilometragem de 5 veículos diferentes. ○ Ao final, mostre qual foi a maior quilometragem registrada.
print("Monitoramento de Frota")
maior_km = 0
for frota in range(1, 6):
    km = float(input(f"Digite a quilometragem do veículo {frota}: "))
    if km > maior_km:
        maior_km = km
print(f"A maior quilometragem registrada é: {maior_km} km.")

# 13.Sistema de Rastreio: Crie um while que peça o código de acesso do rastreador ("track99").○ Enquanto o usuário errar, diga "Acesso Negado". Ele tem 3 tentativas. Se esgotar, exiba "Rastreamento Bloqueado".
print("Sistema de Rastreio")
codigo_correto = "track99"
tentativas = 0
max_tentivas = 3
while tentativas < max_tentivas:
    codigo_input = input("Código de acesso para o rastreador: :)")
    if codigo_input == codigo_correto:
        print("Acesso permitido. Iniciando rastreamento...")
        break
    else:
        tentativas += 1
        print("Acesso negado")
        if tentativas < max_tentivas:
            print(f"Tentativas restantes: {max_tentivas-tentativas}")
else:
    print("Rastreamento Bloqueado")