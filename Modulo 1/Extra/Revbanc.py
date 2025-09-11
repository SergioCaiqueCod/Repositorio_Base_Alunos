print ('(1)sacar\n(2)depositar\n(3)ver saldo\n(4)sair')
total= 1000
while True:
    option=(input(' digite a opção:'))

    if option== '1':
        saque=int(input('digite o valor do saque'))

        if saque>total:
            print('recusado')
        else:
            total=total - saque
            print (total,'saque realizado com sucesso\n')

    elif option== '2':
        deposit=int(input('digite o valor do deposito:'))
        total=total+deposit
        print(' Este é o total:',total)

    elif option== '3':
        print('Ver saldo',total)
    elif option =='4':
        print('obrigado por usar nossos serviços!')
        break