"""
    APRIMORAMENTO DO BANCO 
    funções a serem criadas
        Saque; Deposito; Estrato, Criar_usuario; Criar_conta;
"""
import datetime

def validar_cpf(cpf, usuarios):
    for usuario in usuarios:
        if cpf == usuario.get("CPF"):
            print("Este usuario já existe no sistema")
            return usuario
    return None

def data():
    momento = datetime.datetime.strftime(datetime.datetime.now(), "%d/%m/%Y  %H:%M:%S")
    return momento

def deposito(saldo, valor, extrato):
    hora = data()
    if valor <= 0:
        print("Informe um valor válido")
        return saldo, extrato
    else:
        saldo += valor
        extrato.append(f"Deposito R${valor}          {hora}")
        return saldo, extrato

def imprimir():
    cabecalho = """

|=======Bem-vindo ao Banco=======|


(d)deposito
(s)saque 
(e)extrato 
(q)sair
(nu)novo usuario
(nc)nova conta
(lc)listar contas

"""
    escolha = input(cabecalho)
    return escolha

def cal_estrato(saldo, *, extrato):
    print('======HISTORICO DE OPERACOES======')
    for operacao in extrato:
        print(operacao)
    print(f"Saldo da conta: {saldo}")
    print("==================================")

def saque(*, saldo, valor, extrato, limite, num_saques, limite_saques):
    hora = data()
    if num_saques >= limite_saques:
        print("Limite de saques atingido, faça outra operação")
        return saldo, extrato, num_saques
    if valor <= 0:
        print("Informe um valor positivo para saque")
        return saldo, extrato, num_saques
    if valor > saldo:
        print(f"O valor do saque ultrapassa o valor do saldo da conta\nSaldo da conta: R${saldo}")
        return saldo, extrato, num_saques
    if valor > limite:
        print("O valor máximo de 500")
        return saldo, extrato, num_saques
    
    estrato.append(f"Valor do saque R${valor}        {hora}")
    num_saques += 1
    return saldo - valor, extrato, num_saques

def criar_usuario(usuarios):
    cpf = input('informe seu CPF(apenas numeros): ')
    if validar_cpf(cpf, usuarios):
        return 
    nome = input('informe seu nome: ')
    data_nascimento = input('Informe sua data de nascimento(dd-mm-aa): ')
    endereco = input('Informe seu endereço(logradouro, nº    -cidade estado): ')
    usuarios.append({"nome": nome, "data de nascimento": data_nascimento, "endereco": endereco, "CPF": cpf})
    print("Usuario criado com sucesso")

def criar_contas(agencia, numero_conta, usuarios):
    cpf = input('informe seu CPF: ')
    usuario = validar_cpf(cpf, usuarios)
    if usuario is None:
        print("usuario não encontrado")
        return None
    return {"Agencia": agencia, "Numero da conta": numero_conta, "Usuario": usuario}

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada")
        return
    
    print("LISTA DE CONTAS CADASTRADAS")
    for i, conta in enumerate(contas, 1):
        print(f"CONTA {i}:")
        print(f"   Agencia: {conta['Agencia']}")
        print(f"   Numero da Conta: {conta['Numero da conta']}")
        print(f"   Titular: {conta['Usuario']['nome']}")
        print(f"   CPF: {conta['Usuario']['CPF']}")

saldo = 0
AGENCIA = '0001'
estrato = []
limite = 500
numero_saques = 0
LIMITE_SAQUE = 3
usuarios = []
contas = []

while True:
    opcao = imprimir()
    if opcao == 'd':
        try:
            valor = float(input('Informe o valor do deposito: '))
            saldo, extrato = deposito(saldo, valor, extrato)
        except:
            print("Digite um valor numerico valido")
    elif opcao == 'e':
        cal_estrato(saldo, extrato=estrato)
    elif opcao == 's':
        try:
            valor = float(input('Informe o valor do saque: '))
            saldo, extrato, numero_saques = saque(
                saldo=saldo, valor=valor, extrato=estrato,
                limite=limite, num_saques=numero_saques,
                limite_saques=LIMITE_SAQUE
            )
        except:
            print("Digite um valor numerico valido")
    elif opcao == 'q':
        break
    elif opcao == 'nu':
        criar_usuario(usuarios)
    elif opcao == 'nc':
        numero_contas = len(contas) + 1
        conta = criar_contas(AGENCIA, numero_contas, usuarios)
        if conta:
            contas.append(conta)
            print("Conta criada com sucesso")
    elif opcao == 'lc':
        listar_contas(contas)
    else:
        print("Digite um valor valido")