# Tratamento de Erros
# Organizar de forma adequada o código é essencial para evitar erros e garantir que o programa funcione corretamente. O tratamento de erros é uma prática importante para lidar com situações inesperadas que podem ocorrer durante a execução do programa.

# try e except são estruturas usadas para capturar e lidar com erros de forma controlada. O código dentro do bloco try é executado normalmente, mas se ocorrer um erro, o programa pula para o bloco except, onde você pode definir como lidar com o erro.
while True:
    try:
        # Código que pode gerar um erro
        numero = int(input("Digite um número: "))
        resultado = 10 / numero
        print(f"O resultado é: {resultado}")

    except ValueError:
        print("Erro: Você deve digitar um número válido. ")
        continue

    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
        break
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")
        break

print("Programa encerrado.")


