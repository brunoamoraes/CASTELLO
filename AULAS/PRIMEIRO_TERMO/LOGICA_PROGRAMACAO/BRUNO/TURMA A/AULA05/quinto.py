# Revisão de conteúdo:
# print = "Função de saída de dados para o console"
# input = "Função de entrada de dados do usuário via teclado"
# if = "Estrutura de decisão para executar código condicionalmente"
#     elif = "Combinação de else + if para verificar múltiplas condições"
#     else = "Parte opcional de um if que executa código quando a condição do if é falsa"
# for = "Laço de repetição para iterar sobre uma sequência de elementos"
# while = "Laço de repetição para executar código enquanto uma condição for verdadeira".
# operadores matemáticos: +, -, *, /, //, %, **
# operadores de comparação: ==, !=, >, <, >=, <=
# variavel = "Exemplo de variável para armazenar dados"
# print(variavel)

# # Exemplo 1: com print e input
# nome = input("Digite seu nome: ")
# print(f"Olá, {nome}! Bem-vindo à aula de Python para Desenvolvimento de Sistemas!")

# # Exemplo 2: com if, elif e else
# nota = float(input("Digite a nota do aluno: "))
# if nota >= 7:
#     print("Aluno aprovado!")
# elif nota >= 5:
#     print("Aluno em recuperação.")
# else:
#     print("Aluno reprovado.")

# Exemplo 3: com for
# materiais = ["metal", "plastico", "vidro"]
# for material in materiais:
#     print(f"Processando material: {material}.")
#     print(f"Material {material} processado com sucesso!")
# print("Fim do processamento de materiais.")

# 2. O Laço while (Repetições Indeterminadas)
# Use o while quando você não sabe quando vai parar. Ele depende de uma condição (como um sensor de segurança ou um botão de emergência).
# Exemplo: Monitor de Temperatura (Loop Infinito Controlado)
# Repete enquanto a temperatura estiver segura
import time
temperatura = 25
while temperatura < 40:
    print(f"Temperatura atual: {temperatura}°C. Sistema operando...")
    time.sleep(1)
    temperatura += 3  # Simulando o aquecimento da máquina
print("ALERTA! Temperatura atingiu o limite. Desligando motor...")

# Lista de temperaturas lidas pelo sensor por minuto
leituras = [70, 75, 82, 98, 110, 85, 80]
for temp in leituras:
    while temp > 100:
        print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência.")
        break  # O loop para aqui e NÃO lê os próximos valores (85 e 80)
    print(f"Temperatura está em {temp}°C. Operação normal.")
print("Sistema desligado. Aguardando manutenção.")

# Produção de peças com controle de material usando continue
materiais = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
for peca in materiais:
    if peca != "metal":
        print(f"Aviso: Peça de {peca} detectada. Desviando para descarte...")
        continue  # Pula o restante do código abaixo e vai para a próxima peça    
    # Este código só roda se a peça for de metal
    print(f"Processando peça de {peca}. Furando e polindo...")
print("Fim do lote de produção.")

# Exercicio 1
# Tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5 (simulando uma falha de sensor específica no item 5).
for sensor in range(1,11):
      if sensor == 5:
        print(f"Sensor nº{sensor}com falha")
      print(f"Sensor {sensor} sem falha")
      continue
print("Fim! :)")

# Exercício 2
# Simule um semáforo com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa para cada cor. Use o continue para pular a cor amarela (simulando um semáforo com defeito que não acende a luz amarela).
# import time
# cores = ["verde", "amarelo", "vermelho"]
# for cor in cores:
#     if cor == "amarelo":
#         print(f"Semáforo com defeito, pulando a cor {cor}...")
#         continue  # Pula a cor amarela
#     print(f"Semáforo na cor {cor}. Parando por 3 segundos...")
#     time.sleep(3)  # Simula a pausa para cada cor
# print("Fim do ciclo do semáforo.")

# # Exercício 3 - Soma de Cargas de Energia (for)
# # Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo em kWh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica.
total_consumo = 0
for maquina in range(1, 6):
    consumo = float(input(f"Digite o consumo em kWh da máquina {maquina}: "))
    total_consumo += consumo  # Acumula o consumo total
print(f"O consumo total da fábrica é de {total_consumo} kWh.")

# Exercício 4 - Identificador de Peças Defeituosas (for + if)
# Percorra uma lista de medidas de peças: 
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5].
# O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
# Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada".

pecas = [50.1, 49.8, 52.0, 50.0, 48.5]
for medida in pecas:
    if 48 < medida >= 50.0:
        print(f"Peça com medida {medida}mm: Aprovada")
    else:
        print(f"Peça com medida {medida}mm: Rejeitada")
print("Fim da avaliação de peças.")

# Exercício 5 - Uma balança industrial está pesando um lote de 6 sacos de insumos. O peso ideal de cada saco é 50kg, mas o sistema aceita variações.
# Crie um programa que peça ao usuário o peso de cada saco (via input dentro do loop) e, para cada um, informe se ele está "Dentro do limite" (entre 48kg e 52kg) ou "Fora do limite". No final, exiba quantos sacos estão dentro do limite.

sacos_dl = 0
for saco in range(1,7):
    peso = float(input(f"Digite o peso do saco {saco} em kg: "))
    if 48 <= peso <= 52:
        print(f"Saco {saco} com peso {peso}kg: Dentro do limite")
        sacos_dl += 1  # Conta os sacos dentro do limite
    else:
        print(f"Saco {saco} com peso {peso}kg: Fora do limite")
print(f"Quantidade de sacos dentro do limite: {sacos_dl}")
# O Desafio: Gestão de Ciclo Térmico
# Você deve criar um programa que monitore a temperatura de uma estufa que processa um lote de 5 peças.
# Regras do Sistema: O programa deve rodar em um loop até que 5 peças válidas sejam processadas.
# Para cada peça, peça ao usuário a temperatura atual (input).
# Filtro de Erro (continue): Se o usuário digitar uma temperatura negativa, exiba "Erro de leitura no sensor" e use o continue para pedir a temperatura novamente (essa leitura não conta como peça processada).
# Parada de Emergência (break): Se a temperatura for maior que 150°C, o sistema deve exibir "ALERTA CRÍTICO: Risco de Explosão!", interromper o loop imediatamente e encerrar o programa.

ciclo = 0
while ciclo < 5:
    temperatura = float(input(f"Digite a temperatura da peça {ciclo + 1} em °C: "))
    
    if temperatura < 0:
        print("Erro de leitura no sensor. Por favor, digite uma temperatura válida.")
        continue  # Pede a temperatura novamente sem contar como peça processada
    
    if temperatura > 150:
        print("ALERTA CRÍTICO: Risco de Explosão!")
        break  # Interrompe o loop imediatamente e encerra o programa
    
    print(f"Peça {ciclo + 1} processada com temperatura {temperatura}°C.")
    ciclo += 1  # Conta a peça processada
    
    print(f"Peça {ciclo} processada com sucesso. Temperatura dentro do limite.")
print("Fim do monitoramento de temperatura.")

# Exercicio 6 - Contador de Peças com Falha (while + if + continue)
# Uma linha de produção tem um sensor que detecta falhas em peças. O programa deve contar quantas peças com falha foram detectadas. O usuário deve digitar "sim" para indicar que uma peça tem falha e "não" para indicar que está boa. O programa deve continuar pedindo a condição da peça até que o usuário digite "fim". No final, exiba o total de peças com falha detectadas.