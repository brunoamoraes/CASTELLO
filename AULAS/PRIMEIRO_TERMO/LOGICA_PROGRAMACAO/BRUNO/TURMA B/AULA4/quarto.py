# 2. O Laço while (Repetições Indeterminadas)
# Use o while quando você não sabe quando vai parar. Ele depende de uma condição (como um sensor de segurança ou um botão de emergência).
# Exemplo 1: Monitor de Temperatura (Loop Infinito Controlado)
# Repete enquanto a temperatura estiver segura
# Início
import time
temperatura = 25
while temperatura < 40:
    print(f"Temperatura atual: {temperatura}°C. Sistema operando...")
    time.sleep(1)
    temperatura += 3  # Simulando o aquecimento da máquina
print("ALERTA! Temperatura atingiu o limite. Desligando motor...")

# Exemplo 2: Monitoramento de Temperatura com Lista de Leituras
# Lista de temperaturas lidas pelo sensor por minuto
leituras = [70, 75, 82, 98, 110, 85, 80] 

for temp in leituras:
    if temp > 100:
        print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência.")
        break  # O loop para aqui e NÃO lê os próximos valores (85 e 80)
    print(f"Temperatura está em {temp}°C. Operação normal.")

print("Sistema desligado. Aguardando manutenção.")


materiais = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
for peca in materiais:
    if peca != "metal":
        print(f"Aviso: Peça de {peca} detectada. Desviando para descarte...")
        continue  # Pula o restante do código abaixo e vai para a próxima peça
    
    # Este código só roda se a peça for de metal
    print(f"Processando peça de {peca}. Furando e polindo...")

print("Fim do lote de produção.")