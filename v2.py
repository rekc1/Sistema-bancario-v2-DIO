usuarios = {}
contas_correntes = {}

def cria_usuario(nome,nascimento,cpf,endereco):
    if cpf in usuarios:
        pass
    else:
        usuarios[cpf] = {"nome": nome, "nacismento": nascimento, "endereço": endereco, "cpf": cpf}

def cria_conta(cpf):
    saldo_inicial = 0
    extrato_inicial = ""
    if cpf in usuarios:
        if cpf not in contas_correntes:
            contas_correntes[cpf] = {"agencia": "0001", "numero": len(contas_correntes)+1, "saldo": saldo_inicial, "extrato": extrato_inicial, "usuario": usuarios[cpf]}
        else:
            pass
    else:
        pass

def consultar_extrato(cpf):
    if contas_correntes[cpf]["extrato"] != "":
        r_extrato = contas_correntes[cpf]["extrato"]
    else:
        r_extrato = ("Nenhuma operação foi realizada!")

    return print(f"---EXTRATO---\n {r_extrato}")
def depositar(cpf,valor):
    contas_correntes[cpf]["saldo"] += valor
    contas_correntes[cpf]["extrato"] += f"Depósito: {valor}/ "

def sacar(cpf,valor):
    contas_correntes[cpf]["saldo"] -= valor
    contas_correntes[cpf]["extrato"] += f"Saque: {valor}/ "

cria_usuario("Renato","05/03/2003",42979308897,"Rua Ipês/SP")
# cria_usuario("Matheus","20/03/2003",3993757748,"Rua Tokuzo Terazaki/SP")
# cria_usuario("Natalie","20/03/2003",1234567899,"Rua Tokuzo Terazaki/SP")
#
cria_conta(42979308897)
# cria_conta(3993757748)

Limite_Saque = 3
Valor_Maximo_Saque = 500
saques_realizados = 1
menu = 0

cpf = int(input("CPF: "))
print(f"\nOlá {usuarios[cpf]['nome']}!")

while menu != 5:
    if cpf in contas_correntes:
        menu = int(input(" \n [1] Depósitar\n [2] Sacar\n [3] Consultar Extrato\n [4] Listar contas\n [5] Sair\n R:"))
        if menu == 1:
            valor_deposito = float(input("\nQuanto deseja depositar?\n R:"))
            depositar(cpf, valor_deposito)
            print("\nDepósito realizado com sucesso!")
        elif menu == 2:
            valor_saque = float(input("\nQuanto deseja sacar?\n R:"))
            if saques_realizados <= Limite_Saque:
                if valor_saque <= Valor_Maximo_Saque:
                    if valor_saque <= contas_correntes[cpf]["saldo"]:
                        sacar(cpf, valor_saque)
                        print("\nSaque realizado com sucesso")
                        saques_realizados += 1
                    else:
                        print("\nNão foi possível realizar o saque por falta de saldo!")
                else:
                    print(f"\nNão é possível fazer saques acima de {Valor_Maximo_Saque}!")
            else:
                print("Número limite de saques diário excedido!")
        elif menu == 3:
            consultar_extrato(cpf)
        elif menu == 4:
            print(contas_correntes)

    elif cpf in usuarios:
        r_criar_conta = input(f"\nolá {usuarios[cpf]['nome']} você ainda não ativiou a sua conta deseja ativar agora? (s/n)\n R:")
        if r_criar_conta == "s":
            cria_conta(cpf)
            print("\nParabéns agora você já pode acessar a sua conta!")
        else:
            menu = 5

    else:
        r_criar_usuario = str(input(f"O CPF: {cpf} não foi encontrado no nosso banco de dados deseja criar um usuario?(s/n)\n R:"))
        if r_criar_usuario == "s":
            nome = str(input("Nome:"))
            nascimento = str(input("Data de nascismento:"))
            endereco = str(input("Endereço:"))
            cria_usuario(nome,nascimento,cpf,endereco)
            print("Usuário criado com sucesso, agora é só ativar a sua conta e aproveitar as vantagens de ser cliente do melhor Banco da América Látina!")
        else:
            menu = 5