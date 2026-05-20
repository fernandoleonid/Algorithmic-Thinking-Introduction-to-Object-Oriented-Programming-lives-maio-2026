saldo = 0.0
opcao = ''
while opcao != '0':
    print ()
    print ('***** CAIXA ELETRÔNICO *****')
    print ('1 - Ver saldo')
    print ('2 - Depositar')
    print ('3 - Sacar')
    print ('0 - Sair')
    opcao = input('Escolha uma das opções: ')
    
    print ()
    if opcao == '1':
        print (f'--> Saldo atual: R$ {saldo:.2f}')

    elif opcao == '2':
        valor = float(input('Digite o valor para depositar: '))
        if valor > 0:
            saldo += valor
            print ('Deposito realizado com sucesso!')
        else:
            print ('Valor inválido!!!')
    elif opcao == '3':
        valor_saque = float(input('Digite o valor de saque: '))
        if valor_saque <= 0:
            print ('Valor inválido!')
        elif valor_saque > saldo:
            print ('Saldo insuficiente!')
        else:
            saldo = saldo - valor_saque
            print ('Saque realizado com sucesso!')
    elif opcao == '0':
        print ('Saindo do sistema...')
    else:
        print ('Opção inválida, tente novamente!')