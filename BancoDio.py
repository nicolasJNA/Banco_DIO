import os

saldo = 0.0
saque = 0
LIMITE_SAQUE = 3
cont = 0
estrato = []

def sacar(saldo_atual):
    retirar = float(input("Digite o valor para o saque: "))
    if retirar > 500:
        print("Valor ultrapassa o limite permitido (R$500.00)")
        return 0
    elif retirar > saldo_atual:
        print(f"Valor do saque superior ao saldo\nSaldo atual: R${saldo_atual:.2f}")
        return 0
    else:
        return retirar

def depositar():
    valor = float(input("Digite o valor para o deposito: "))
    if valor < 0:
        print("Digite um valor válido")
        return 0
    else:
        return valor

cabecalho = """
|=======Bem-vindo ao Banco=======|


(d)deposito (s)saque (e)extrato (q)sair: """

while True:
    acao = input(cabecalho)
    
    if acao == 'd':
        os.system("clear")
        deposito = depositar()
        if deposito > 0:
            saldo += deposito
            estrato.append(f"Valor depositado de R${deposito:.2f}")
        os.system("clear")
    elif acao == 's':
        os.system("clear")
        if cont >= LIMITE_SAQUE:
            print("Limite máximo de saques atingido, faça outra operação")
        else:
            saque = sacar(saldo)
            if saque > 0:  # Só subtrai se o saque foi autorizado
                saldo -= saque
                estrato.append(f"Valor sacado da conta R${saque:.2f}")
                cont += 1
    elif acao == 'q':
        break
    elif acao == 'e':
        os.system("clear")
        print('========ESTRATO========')
        for operacao in estrato:
            print("{}".format(operacao))
        print(f"\nSaldo atual: R${saldo:.2f}")
        print("=======================")
        input('\nPressione enter para continuar')
        os.system("clear")
    else: 
        print("Insira um valor válido")
        os.system("clear")