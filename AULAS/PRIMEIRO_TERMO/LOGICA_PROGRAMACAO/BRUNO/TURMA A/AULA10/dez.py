# Tratamento de Erros e Depuração
# try e except são usados para lidar com erros de forma controlada, evitando que o programa quebre. O código dentro do bloco try é executado normalmente, mas se ocorrer um erro, o controle é passado para o bloco except, onde podemos lidar com a situação de forma apropriada.

# try:
#     numero = int(input("Digite um número: "))
#     resultado = 10 / numero
#     print("O resultado é:", resultado)

# except ValueError:
#     print("Erro: Você deve digitar um número válido.")

# except ZeroDivisionError:
#     print("Erro: Não é possível dividir por zero.")

# except KeyboardInterrupt:
#     print("\n Programa interrrompido")

# except TypeError:
#     print("Erro: Tipo de dado inválido.")

# except Exception as erro:
#     print("Erro inesperado:", erro)

# Exercicio 1
# Escreva um programa que solicite ao usuário calcule a média de três números. O programa deve lidar com possíveis erros, como a entrada de valores não numéricos ou a divisão por zero.


# Explicação de def: A palavra-chave "def" é usada para definir uma função em Python. Uma função é um bloco de código reutilizável que realiza uma tarefa específica. 
# return: A palavra-chave "return" é usada para finalizar a execução de uma função e retornar um valor para o local onde a função foi chamada. O valor retornado pode ser usado posteriormente no código.

# def nome_da_funcao(parametro1, parametro2):
#     # Corpo da função (código que será executado)
#     resultado = parametro1 + parametro2
#     return resultado

# Exemplo 1:
def saudacao(nome, idade):
    nome = input("Digite seu nome: ")
    return f"Olá, {nome}, {idade}!"
print(saudacao("", 14))


# Exemplo 2:
def calcular_media(num1, num2, num3):
    try:
        media = (num1 + num2 + num3) / 3
        return media
    except TypeError:
        return "Erro: Todos os valores devem ser números."
    except ZeroDivisionError:
        return "Erro: Não é possível dividir por zero."

print(f"calcular_media {(calcular_media(10, 20, 30))}")

# Exemplo 3:
def valores():
    print("Digite três valores:")
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    c = int(input("Digite o terceiro valor: "))
    return a, b, c
print(f"O maior valor é: {max(valores())}") 

# Exemplo 4:
# Calcule o dobro de um número fornecido pelo usuário, tratando erros de entrada inválida.
def calcular_dobro():
    try:
        valor_digitado = int(input("Digite o valor que deseja :)"))
        total_dobro = valor_digitado * 2
        return total_dobro
    
    except ValueError:
        print("Digite um número válido")
print(f"O calculo é: {calcular_dobro()}")

  
