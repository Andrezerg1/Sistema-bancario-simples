#SISTEMA BANCÁRIO
#Esse sistema tem como objetivo aplicar meus conhecimentos em python, de modo simplificado, ao criar um sistema de gerenciamento de bancos.

#criação de um dicionário global para armazenamento das contas cadastradas
contas = {}


#Criação de funções

def criarConta():
    numero = int(input("Digite o número da conta: "))

    if numero in contas:
        print("Essa conta já existe.")
        return

    titular = input("Digite o nome do titular: ")
    contas[numero] = {"titular": titular, "saldo": 0.0}
    print("Conta criada com sucesso.")

def listarContas():
    if not contas:
        print("Não existe nenhuma conta cadastrada.")
        return

    for numero, info in contas.items():
        print(f"Conta: {numero} | Titular: {info['titular']} | Saldo: R$ {info['saldo']:.2f}")

def Deposito():
    numero = int(input("Digite o número da conta: "))
    if numero not in contas:
        print("Conta não encontrada.")
        return

    valorDeposito = float(input("Insira o valor do depósito: "))
    contas[numero]["saldo"] += valorDeposito
    print("Depósito realizado com sucesso.")

def sacar():
    numero = int(input("Digite o número da conta: "))
    if numero not in contas:
        print("Conta não encontrada.")
        return

    valorSaque = float(input("Digite o valor a ser sacado: "))
    if valorSaque > contas[numero]["saldo"]:
        print("Saldo insuficiente.")
        return

    contas[numero]["saldo"] -= valorSaque
    print("Saque realizado.")

def transferir():
    origem = int(input("Digite o número da conta de origem: "))
    destino = int(input("Digite o número da conta destino: "))

    if origem not in contas or destino not in contas:
        print("Uma das contas está incorreta.")
        return

    valorTransferencia = float(input("Valor da transferência: "))
    if valorTransferencia > contas[origem]["saldo"]:
        print("Saldo insuficiente.")
        return

    contas[origem]["saldo"] -= valorTransferencia
    contas[destino]["saldo"] += valorTransferencia
    print("✔ Transferência concluída!")

def menu():
    while True:
        print("\n===== SISTEMA BANCÁRIO SIMPLES =====")
        print("1. Criar conta")
        print("2. Listar contas")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Transferir")
        print("6. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            criarConta()
        elif opcao == "2":
            listarContas()
        elif opcao == "3":
            Deposito()
        elif opcao == "4":
            sacar()
        elif opcao == "5":
            transferir()
        elif opcao == "6":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")


# Iniciar o sistema
menu()