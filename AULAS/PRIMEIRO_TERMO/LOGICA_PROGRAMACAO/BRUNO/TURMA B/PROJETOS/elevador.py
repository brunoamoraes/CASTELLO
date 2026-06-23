# Meu primeiro projeto de elevador em Python! 

print("Bem-vindo ao Elevador Python!")
andar_atual = 0
while True:
    try:
        destino = int(input("Digite o andar de destino (0-10): "))
        if destino < 0 or destino > 10:
            raise ValueError("Andar inválido. Por favor, digite um número entre 0 e 10.")
        
        print(f"Elevador se movendo do andar {andar_atual} para o andar {destino}...")
        andar_atual = destino
        print(f"Chegamos ao andar {andar_atual}!")

        if input("Deseja escolher outro andar? (s/n): ").lower() != 's':
            print("Obrigado por usar o Elevador Python! Até a próxima!")
            break
        for listagem in range(10):
            print(f"Andar {listagem} - {'[X]' if listagem == andar_atual else '[ ]'}")

    except ValueError as erro:
        print(f"Erro: {erro}. Tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")
        print("Programa encerrado.")
        break