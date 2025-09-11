print('(1)Adicionar unidades\n(2)remover unidades\n(3)verificar o estoque atual\n(4)sair')
estoque=  50 
while True:
    option= (input('digite a opção:'))

    if option== '1':
        acres= int(input('digite o valor'))
        estoque=estoque+acres
        print('estoque final:',estoque)

    if option=='2':
        remov= int (input('digite a quantidade para a remoção:'))
        
        if estoque < remov:
            print('não liberar')
        
        else:
            estoque=estoque-remov
            print('estoque atual:',estoque)
            
    elif option=='3':
        print('estoque final:',estoque)

    elif option== '4':
        print('saindo do aplicativo...')
        break