"""
Limite de 10 transações diarias
Mostrar no extrato data e hora das transações
"""
import datetime
import os


def data():
    momento = datetime.datetime.strftime(datetime.datetime.now(), "%d/%m/%Y  %H:%M:%S")
    return momento

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

saldo = 0
saque = 0
LIMITE_SAQUE = 3
cont = 0
transacao = 0
LIMITE_TRANSACAO = 10
estrato = []

cabecalho = """
|=======Bem-vindo ao Banco=======|


(d)deposito (s)saque (e)extrato (q)sair: """
while True:
    acao = input(cabecalho)
    
    if acao == 'd':
        os.system("clear")
        if transacao >= LIMITE_TRANSACAO:
            print("Maximo de 10 transações diarias atingidas")
        else:
            deposito = depositar()
            if deposito > 0:
                transacao = transacao + 1
                saldo += deposito
                hora = data()
                estrato.append(f"Valor depositado de   R${deposito:.2f}   {hora}")      
                os.system("clear")
    elif acao == 's':
        os.system("clear")
        if cont >= LIMITE_SAQUE:
            print("Limite máximo de saques atingido, faça outra operação")
        else:
            saque = sacar(saldo)
            if saque > 0:  # Só subtrai se o saque foi autorizado
                saldo -= saque
                hora = data()
                estrato.append(f"Valor sacado da conta R${saque:.2f}    {hora}")
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
        print("Insira um valor que seja válido")
        os.system("clear")