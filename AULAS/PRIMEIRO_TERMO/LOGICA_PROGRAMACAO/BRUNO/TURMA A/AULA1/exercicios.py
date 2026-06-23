# Exercicio 1
# Criar um algoritmo pergunte essas informações seu nome, idade, curso e seu hobbie e apresente no final o resultado
print("Informações pessoais \n")
nome = input("Digite seu nome: \n")
idade = int(input("Digite sua idade: \n"))
curso = input("Digite seu curso: \n")
hob = input("Digite seu hobbie: \n")
print("Os resultados são: \n", nome, curso, idade, hob)

# Exercício 2
# Criar um algoritmo que pergunte o valor A e o valor B e apresente o resultado em um valor C
print("Cálculo de Valores")
valorA = int(input("Digite o valor A: \n"))
valorB = int(input("Digite o valor B: \n"))
valorC = valorA + valorB
print("O resultado dos valores são: \n ", valorC)
print(valorA+valorB)

# Exercício 3
# Criar um algoritmo calcule sua viagem por 3 pedágios, em cada pedágio será cobrado um valor e no fim apresente o total das passagens
print("Cálculo de Pedágio")
p1 = int(input("Digite o valor do 1º Pedágio: \n"))
p2 = int(input("Digite o valor do 2º Pedágio: \n"))
p3 = int(input("Digite o valor do 3º Pedágio: \n"))
total = p1 + p2 + p3


# Exercício 4
# Criar um algoritmo para calcular o IMC (Indice de Massa Corporal). 
# Para esse cálculo precisamos do peso e altura. O cálculo deverá ser peso / altura * altura ou peso / altura^2 ou por altura**altura
print("Cálculo de IMC")
peso = float(input("Digite o seu peso: \n"))
altura = float(input("Digite sua altura: \n"))
print("O seu IMC é: ",peso/(altura*altura) )
