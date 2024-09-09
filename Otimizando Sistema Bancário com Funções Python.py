
# Otimizando o Sistema Bancário com Funções Python

## Curso: Engenharia de Dados com Python - DIO
## Aluna: Natália Ferreira

import textwrap

def menu():
    """
    Exibe o menu de operações disponíveis e retorna a opção selecionada pelo usuário.
    """
    menu = """\n
    ================ MENU ================
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [lc] Listar contas
    [q]  Sair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    """
    Função para realizar depósito na conta.
    
    Argumentos:
    - saldo (float): Saldo atual da conta.
    - valor (float): Valor a ser depositado.
    - extrato (str): Histórico das transações.

    Retorno:
    - saldo (float): Saldo atualizado após o depósito.
    - extrato (str): Histórico atualizado com a transação de depósito.
    """
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Função para realizar saque na conta.
    
    Argumentos nomeados:
    - saldo (float): Saldo atual da conta.
    - valor (float): Valor a ser sacado.
    - extrato (str): Histórico das transações.
    - limite (float): Limite máximo por saque.
    - numero_saques (int): Contador de saques realizados no dia.
    - limite_saques (int): Limite máximo de saques diários.

    Retorno:
    - saldo (float): Saldo atualizado após o saque.
    - extrato (str): Histórico atualizado com a transação de saque.
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    """
    Função para exibir o extrato da conta.
    
    Argumentos:
    - saldo (float): Saldo atual da conta (posicional).
    - extrato (str): Histórico das transações (nomeado).
    """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    """
    Função para cadastrar um novo usuário (cliente) do banco.
    
    Argumentos:
    - usuarios (list): Lista de usuários existentes.

    A função solicita ao usuário informações pessoais e verifica duplicidade de CPF.
    """
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    """
    Função para buscar um usuário na lista pelo CPF.

    Argumentos:
    - cpf (str): CPF do usuário a ser buscado.
    - usuarios (list): Lista de usuários.

    Retorno:
    - dict: Usuário encontrado ou None se não encontrado.
    """
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    """
    Função para criar uma nova conta corrente vinculada a um usuário existente.

    Argumentos:
    - agencia (str): Número da agência.
    - numero_conta (int): Número sequencial da conta.
    - usuarios (list): Lista de usuários existentes.

    Retorno:
    - dict: Nova conta criada ou None se o usuário não for encontrado.
    """
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    """
    Função para listar todas as contas cadastradas.

    Argumentos:
    - contas (list): Lista de contas existentes.
    """
    for conta in contas:
        linha = f"""\n
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    """
    Função principal que controla o fluxo do sistema bancário.
    """
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    # Variáveis principais
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    # Loop principal do sistema
    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


# Início do programa
if __name__ == "__main__":
    main()
