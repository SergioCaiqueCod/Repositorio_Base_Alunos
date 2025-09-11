numero= int(input('digite uma nota de 0 a 10:'))

while numero<0 or numero>10:
    print('invalido')
    numero = int(input('digite novamente '))
print('valido')