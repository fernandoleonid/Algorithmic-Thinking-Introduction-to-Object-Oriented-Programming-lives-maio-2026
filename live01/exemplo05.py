senha_cadastrada = '123'
senha_digitada = input('Digite sua senha: ')
tentativas = 0
limite_tentativas = 3

while senha_digitada != senha_cadastrada:
    tentativas += 1
    if tentativas >= limite_tentativas:
        print ('Limite de tentativa atingida, espere 4 horas para uma nova tentativa!')
        exit()

    print ('Senha errada, tente novamente!')
    senha_digitada = input('Digite sua senha: ')


print ('Entrando no sistema...')