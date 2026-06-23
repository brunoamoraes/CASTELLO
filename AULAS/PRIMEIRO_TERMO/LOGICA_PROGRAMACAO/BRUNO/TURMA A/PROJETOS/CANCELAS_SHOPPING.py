# Criar um algoritmo para que:

# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código






print("=============================================================")
print("Bem-vindo ao sistema de gerenciamento de cancelas do shopping!")
print("=============================================================")

numerodoveiculo = 0
tarifa_por_hora = 9.0

while True:
    print("\nEscolha uma opção:")
    print("1 - Sem parar (TAG)")
    print("2 - Ticket")
    print("0 - Encerrar sistema")
    
    entrada = input("Opção: ")

    if entrada == "0":
        print("Encerrando o sistema...")
        
        break

    elif entrada == "1" or entrada == "2":
        numerodoveiculo += 1
        
        placa = input(f"Digite a placa do veículo {numerodoveiculo}: ")
        
        tempo = float(input("Digite o horário de entrada: "))
        saida = float(input("Digite o horário de saída: "))

        if saida < tempo:
            print("Erro: horário de saída menor que entrada!")
            continue

        permanencia = saida - tempo
        valor = permanencia * tarifa_por_hora

        print("\n----- Dados do Veículo -----")
        print(f"Placa: {placa}")
        print(f"Tempo de permanência: {permanencia} horas")
        print(f"Valor a pagar: R${valor:.2f}")
        print(f"Veículo número: {numerodoveiculo}")

        if entrada == "1":
            print("Cobrança será feita automaticamente na TAG.")

        elif entrada == "2":
            print("Forma de pagamento:")
            print("1 - Dinheiro")
            print("2 - Cartão")

            pagamento = input("Escolha: ")

            if pagamento == "1":
                print("Pagamento em dinheiro selecionado.")
                print(f"Valor a pagar: R${valor}. Dirija-se ao caixa para efetuar o pagamento.")
                print("Obrigado pela preferência, volte sempre!")
            elif pagamento == "2":
                print("Pagamento com cartão selecionado.")
                print("1 debito ou 2 credito?")
                cartao = input("Escolha: ")
                if cartao == "1":
                    print("Pagamento no débito selecionado.")
                    print("obrigado pela escolha volte sempre")
                elif cartao == "2":
                    print("Pagamento no crédito selecionado.")
                    print("obrigado pela escolha volte sempre")
            else:
                print("Opção inválida de pagamento.")

    else:
        print("Opção inválida! Tente novamente.")