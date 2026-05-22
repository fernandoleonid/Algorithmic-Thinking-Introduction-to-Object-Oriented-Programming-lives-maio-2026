import os

def limpar_tela ():
    os.system('clear')

def pausar():
    print()
    input('Aperte ENTER para continuar...')

conta = {
        'titular': 'Fernando',
        'agencia': '123',
        'cc': '987654',
        'saldo': 0.0,
        'historico': []
    }

def exibir_extrato ():
    limpar_tela()
    print ('******* EXTRATO ********')
    print (f'Titular: {conta["titular"]}')
    print (f'Agencia: {conta["agencia"]}')
    print (f'Conta corrente: {conta["cc"]}')
    print ()
    for movimento in conta['historico']:
        print (f'{movimento['tipo']} -> {movimento['valor']}')
    print (f'Saldo atual: {conta['saldo']}')
    pausar()

def registrar_movimento(tipo,valor):
    conta['historico'].append({
        'tipo': tipo,
        'valor': valor
    })  

def depositar():
    valor = float(input('Digite o valor para deposito: '))
    conta['saldo'] += valor
    registrar_movimento('Entrada', valor)
    print ('Deposito realizado com sucesso!!!')
    pausar()

def sacar ():
    valor = float(input ('Digite o valor para sacar: '))
    conta['saldo'] -= valor
    registrar_movimento('Saída', valor)
    print ('Saque feito com sucesso!!!')
    pausar()

def exibir_menu ():
    limpar_tela()
    print ('***** Caixa Eletrônico *****')
    print ('1 - Saldo')
    print ('2 - Extrato')
    print ('3 - Depositar')
    print ('4 - Sacar')
    print ('0 - Sair')

def processar_opcao (opcao):
    if opcao == '1':
        print (f'Saldo atual: {conta['saldo']}')
        pausar()
    elif opcao == '2':
        exibir_extrato()
    elif opcao == '3':
        depositar()
    elif opcao == '4': 
        sacar()
    elif opcao == '0':
        exit()
    else:
        print ('Opção errada!!!')

def app():
    opcao = ''
    while opcao != 0:
        exibir_menu()
        opcao = input('Escolha uma opção: ')
        processar_opcao(opcao)

app()