# # Funções são blocos de código reutilizáveis. 
# # O "f" no Python, usado antes das aspas de uma string (como f"texto {variável}"), indica que se trata de uma f-string (ou formatted string literal).  Ele informa ao Python que a string contém expressões entre chaves {} que devem ser avaliadas em tempo de execução e substituídas pelos seus valores reais. 

# def saudacao(nome):
#     return f"Olá, {nome}!"

# mensagem = saudacao("Maria")
# print(mensagem) 

# def age(idade):
#     return f"Sua idade é, {idade}!"
# mensagem = age("16")
# print(mensagem)

# def boas_vindas(nome, cargo):
#     print(f"Olá, {nome}! Você é o novo {cargo}.")

# boas_vindas("Ana", "Desenvolvedora")
# boas_vindas("Carlos", "Gerente")
# boas_vindas("Bruno", "Professor")


# # Conversões
# nome = input("Seu nome: ")
# idade = int(input("Sua idade: ")) # Converte texto para inteiro
# print(f"{nome}, tem {idade} anos.")

# # Exercício 1
# # Criar um algoritmo que calcule suas notas e apresente o
# #  resultado final do semestre e do ano
# # Formativa e Somativa 0 a 100
# # Somativa 1 e Somativa 2 / 2 - Calculo da Média
# # Apresentar a média dos dois semestres como resultado final
# print("Cálculo de Notas - Senai")
# print("Somativas do Primeiro Semestre")
# nome = input("Digite o nome do aluno \n")
# p1 = float(input("Digite a nota Somativa 1: \n"))
# p2 = float(input("Digite a nota Somativa 2: \n"))
# ptotal = (p1 + p2) / 2
# print("As somativas do primeiro semestre são: \n", "do aluno", nome ,round(ptotal,2))


# Exercício 2
# Criar um algoritmo que calcule o dobro dos valores
print("Calculadora de valores em Dobro")
x = float(input("Digite o valor que deseja dobrar \n"))
print("O valor do dobro ficou: \n", x*2)

# Exercício 3
# Mercado do Senai
# Criar um algoritmo para calcular uma compra realizada. Na compra deve conter o nome do produto, o valor e a quantidade comprada. 
# No final da compra deve ter o total e apresentar um relatório da sua compra realizada.

# Exercício 4
# Criar um algoritmo para calcular a compra de livros e peça para inserir uma porcentagem de desconto sobre o produto comprado.
# O algoritmo deve perguntar o nome do livro, o valor, a quantidade e o valor de desconto que será aplicado. No final deve conter o valor total da compra com o desconto aplicado.

# Exercício 5
# Criar um algoritmo para simular o cálculo de uma tabuada
# inserir o operador e o multiplicador
