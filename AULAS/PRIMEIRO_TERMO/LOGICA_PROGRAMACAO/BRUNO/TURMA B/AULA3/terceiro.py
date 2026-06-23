# # 1. O Laço 'for' (Repetições Determinadas)
# # Use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças).
# # Exemplo: Relatório de Produção Diária
# # Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# # Exemplo 1
# for lote in range(1, 6):
#     print(f"Processando lote número {lote}...")
#     print("Qualidade verificada. [OK]")
# print("Produção do dia finalizada!")

# # Exemplo 2
# for b in range(10):
#     print(f"Quantidade total {b} foi...")

# # Exemplo 3
# # Imagine o seguinte cenário, iremos produzir 20 discos de vinil.
# for disco in range(21):
#     print(f"Produção de discos {disco} foi de...")

# Exemplo 4
# pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo", "Prego", "Chave de Fenda"]
# itempecas = ["Cilindricas", "Eixo Cônico", "Radiais", "Madeira", "Bola", "Cabeça Chata","Chave metalica verde"]

# for item in pecas:
#     print(f"Item em estoque: {item} e {itempecas}")
#     for item2 in itempecas:
#         print(f"Item de peças em estoque: {itempecas}")

# Exemplo 5
# Imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opção você deseja e a partir da seleção ele listar os produtos
print("Loja da Nazareth")
print("Opção 1- Peças")
print("Opção 2- Item Peças")
menu = int(input("Escolha uma opção"))

pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo", "Prego", "Chave de Fenda"]
itempecas = ["Cilindricas", "Eixo Cônico", "Radiais", "Madeira", "Bola", "Cabeça Chata","Chave metalica verde"]

if menu == 1:
    for item1 in pecas:
        print(f"Sua lista de peças {pecas} são...")
elif menu == 2:
    for item1 in itempecas:
        print(f"Sua lista de itens de peças {itempecas} são...")
else:
    print("Opção inválida: Encerrando o sistema")

# # Exercício 1
# # 1. Contador de Produção (for)
# # Uma esteira processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e, para cada número, imprima: "Peça nº X processada com sucesso". No final, exiba "Ciclo de produção concluído".
for ciclo in range(1,11):
    print(f"Peça nº {ciclo} processada com sucesso... :)")
print("Ciclo de produção concluído... :)")

# Exercício 2
# Imagine a produção de frutas em uma feira. Desejo apresentar as frutas banana, manga, melancia, abacaxi. Com uma quantidade de 10 bananas , 5 mangas , 10 melancias e 13 abacaxi.
# No fim da produção gostaria de ter um total das produções

# Exercício 3
# Montar uma tabuada inicialmente pode ser usado por um valor fixo e depois usar a pergunta
