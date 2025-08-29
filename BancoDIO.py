"""
    APRIMORAMENTO DO BANCO 
    funções a serem criadas
        Saque; Deposito; Estrato, Criar_usuario; Criar_conta;
"""
import datetime

def data():
    momento = datetime.datetime.strftime(datetime.datetime.now(), "%d/%m/%Y  %H:%M:%S")
    return momento
def deposito(saldo,valor,extrato):
    hora = data()
    if valor < 0:
        print("informe um valor válido")
        return saldo,extrato
    else:
        saldo += valor
        extrato.append(f"Deposito R${valor}          {hora}")
        return saldo,extrato
def imprimir():
    cabecalho = """\n
|=======Bem-vindo ao Banco=======|


(d)deposito
(s)saque 
(e)extrato 
"""
    escolha = input(cabecalho)
    return escolha
def cal_estrato(saldo,*,estrato):
    print('======HISTORICO DE OPERACOES======')
    for contagem in range(len(estrato)):
        print(estrato[contagem])
    
    print("\nSaldo da conta: {}".format(saldo))
    print("==================================")
def saque(*,saldo,valor,estrato,limite,num_saques,limite_saques):
    hora = data()
    if(valor > saldo):
        print("O valor do saque ultrapassa o valor do saldo da conta\nSaldo da conta: R${}".format(saldo))
        return saldo,estrato
    elif(valor > limite):
        print("O valor máximo de 500")
        return saldo,estrato
    elif (num_saques > limite_saques):
        print("Limite de saques atingido, faça outra operação")
        return saldo,estrato
    else:
        estrato.append("Valor do saque R${}        {}".format(valor,hora))
        num_saques += 1
        return saldo-valor,estrato,num_saques


saldo = 0
estrato = []
limite = 500
numero_saques = 0
LIMITE_DEPOSITOS = 10
LIMITE_SAQUE = 3
usuarios = []
contas = []

while True:
    opcao = imprimir()
    if opcao == 'd':
        valor = float(input('Informe o valor do deposito: '))
        saldo,estrato = deposito(saldo,valor,estrato)
    elif opcao == 'e':
        cal_estrato(saldo,estrato=estrato)
    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))
        
        saldo,estrato,numero_saques = saque(saldo=saldo,valor=valor,estrato=estrato,limite=limite,num_saques=numero_saques,limite_saques=LIMITE_SAQUE)
        print(numero_saques)
    elif opcao == 'q':
        break
