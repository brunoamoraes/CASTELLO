# Clean Code - Aula 6
# Para que usar?
# Como usar?
# print("Clean Code - Aula 6")
# aula = 6
# print(f"Estamos na aula {aula} de Clean Code")

# # Manipulação de arquivos e Texto
# texto = "  Python é Muito legal!  "
# print(texto.strip().upper()) # "PYTHON"
# print(texto.strip().lower())  # "python"
# print(texto.strip().capitalize())  # "Python"
# print(texto.strip().title())  # "Python"
# print(texto.strip().replace(" ", "_"))  # "Python"
# print(texto.strip().split())  # ["Python"]

# Escrevendo
# with open("notas.txt", "w") as arquivo:
#     arquivo.write("Estudar Python hoje!")
#     arquivo.write("\nLer sobre Clean Code.")

# # Lendo
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# Exercicio 1:
# Crie um programa que peça ao usuário para inserir uma frase e, em seguida, exiba a frase com as seguintes transformações:
# - Remova os espaços extras no início e no final da frase.
# frase = input("Digite uma frase: ")
# print(frase.strip())
# # - Converta a frase para letras maiúsculas.
# print(frase.strip().upper())

# Exemplo 1:
# Crie um programa que leia o conteúdo de um arquivo de texto e conte quantas vezes a palavra "Python" aparece no arquivo. Exiba o resultado para o usuário.
# print("Contagem de palavras em arquivo")
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     contagem = conteudo.count("Python")
#     print(f"A contagem de palavras {contagem} é de...")

# Execução de comandos do sistema
import os # importa o módulo os para interagir com o sistema operacional
# Onde estou?
# print(os.getcwd())
# # Listar arquivos na pasta
# print(os.listdir())
# print(os.listdir(".."))  # lista arquivos da pasta pai
# print(os.listdir("..\\.."))  # lista arquivos da pasta avô
# print(os.listdir("C:\\"))  # lista arquivos da raiz do C
# print(os.listdir("C:\\Users"))  # lista arquivos da pasta Users
# print(os.listdir("C:\\Users\\Public"))  # lista arquivos da pasta Public

# Outros comandos úteis:
# # Criar pasta
# os.mkdir("AULA7")
# # Renomear pasta
# os.rename("nova_pasta", "pasta_renomeada")
# # # Excluir pasta
# os.rmdir("pasta_renomeada")

# Exercicio 2: 
# Crie um script que mostre o caminho da pasta atual.

# # Exercicio 3:
# # Liste os arquivos da pasta atual.

# # Exercicio 4:
# # Crie uma pasta chamada "projetos" e depois renomeie para "meus_projetos". Por fim, exclua a pasta.