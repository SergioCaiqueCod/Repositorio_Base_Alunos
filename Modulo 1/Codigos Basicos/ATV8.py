auto= int(input('digite a autonomia de km por litro:'))
tanq= int(input('digite os litros:'))

if auto * tanq >= 450:
    print('não precisa reabastecer')
else:
    print('precisa reabastecer')