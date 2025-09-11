sala= int(input('digite o seu salario:'))
idad= int(input('digite a sua idade:'))

if sala>=3000:
    print('liberado')
else:
    print('acesso negado')

    if idad>=21:
        print('liberado')
    else:
        print('acesso negado')
