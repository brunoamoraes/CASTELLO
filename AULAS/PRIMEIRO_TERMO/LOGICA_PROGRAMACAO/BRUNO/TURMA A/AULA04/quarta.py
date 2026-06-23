# # 1. O Laço 'for' (Repetições Determinadas)
# # Use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças).
# # Exemplo: Relatório de Produção Diária
# # Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# Exemplo 1
# lote = int(input("Digite a quantidade"))
# for lote in range(1, 6):
#     print("Processando lote número {lote}...")
#     print("Qualidade verificada. [OK]")
# print("Produção do dia finalizada!")

# # Exemplo 2
# for b in range(6,11):
#     print(f"Quantidade total {b} foi...")

# # Exemplo 3
# # Imagine o seguinte cenário, iremos produzir 20 discos de vinil.
# for vinil in range(1,21):
#     print(f"Produção de {vinil}, diária")

# Exemplo 4
# pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo", "Prego", "Chave de Fenda", "Alicate"]
# itempecas = ["Cilindrica", "Duplo", "Cônica", "Prego", "Orelha", "Redondo", "Phillips", "Universal"]

# for item in pecas:
#     print(f"Item em estoque: {item} e {itempecas}")

# Exemplo 5
# Imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opção você deseja e a partir da seleção ele listar os produtos
    
# print("Menu de Opções de Filmes e Séries")
# print("1 Para Filmes ou 2 Séries ")
# escolha = int(input("Digite a opção:"))

# if escolha == 1:
#     filmes = ["Bons de Bico", "Colecionador de Ossos", "Gente Grande"]
#     for fil in filmes:
#         print(f"Os filmes que pode escolhar {filmes} são:")
# elif escolha == 2:
#     series = ["Stranger Things", "Dark","The Boys"]
#     for ser in series:
#         print(f"{series}")
# else:
#     print("Encerramos nosso sistema")

# # Exercício 1
# # 1. Contador de Produção (for)
# # Uma esteira processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e, para cada número, imprima: "Peça nº X processada com sucesso". No final, exiba "Ciclo de produção concluído".
# for ciclo in range(1,11):
#     print(f"Peça nº {ciclo} processada com sucesso... :)")
# print("Ciclo de produção concluído... :)")

# Exercício 2
# Imagine a produção de frutas em uma feira. Desejo apresentar as frutas banana, manga, melancia, abacaxi. Com uma quantidade de 10 bananas , 5 mangas , 10 melancias e 13 abacaxi.
# No fim da produção gostaria de ter um total das produções

# for ban in range(1,11):
#     print(f"{ban} ")

# for man in range(1,6):
#     print(f"{man} ")

# total = ban + man 

# # Exercício 3
# # Montar uma tabuada inicialmente pode ser usado por um valor fixo e depois usar a pergunta
# print("Tabuada")
# tab = int(input("Digite qual tabuada você quer"))
# for numero in range(1,11):
#     resultado = tab * numero
#     print(f"{tab} X {numero} = {resultado}")


