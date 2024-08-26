# Sistema Bancário Simples em Python

## Curso: Engenharia de Dados com Python - DIO
## Aluna: Natália Ferreira

# Definição do menu de operações
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Inicialização das variáveis principais
saldo = 0  # Saldo da conta
limite = 500  # Limite máximo por saque
extrato = ""  # Histórico de transações
numero_saques = 0  # Contador de saques realizados no dia
LIMITE_SAQUES = 3  # Limite máximo de saques diários

# Loop principal do sistema
while True:
    # Exibe o menu e solicita uma opção ao usuário
    opcao = input(menu)

    # Operação de depósito
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        # Verifica se o valor do depósito é positivo
        if valor > 0:
            saldo += valor  # Atualiza o saldo com o valor do depósito
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Adiciona o depósito ao extrato
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Operação de saque
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        # Verificações das regras para saque
        excedeu_saldo = valor > saldo  # Verifica se o saque excede o saldo disponível
        excedeu_limite = valor > limite  # Verifica se o saque excede o limite por operação
        excedeu_saques = numero_saques >= LIMITE_SAQUES  # Verifica se o número de saques diários foi atingido

        # Condições que impedem o saque
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        # Se todas as condições forem satisfeitas, o saque é realizado
        elif valor > 0:
            saldo -= valor  # Deduz o valor do saque do saldo
            extrato += f"Saque: R$ {valor:.2f}\n"  # Adiciona o saque ao extrato
            numero_saques += 1  # Incrementa o número de saques realizados
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Operação de extrato
    elif opcao == "e":
        # Exibe o extrato ou uma mensagem se não houver transações
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")  # Exibe o saldo atual formatado
        print("==========================================")

    # Encerrar o sistema
    elif opcao == "q":
        break  # Sai do loop principal e encerra o programa

    # Caso a opção seja inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
