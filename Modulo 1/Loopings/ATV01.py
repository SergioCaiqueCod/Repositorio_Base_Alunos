us= input('digite alguma palavra')
vogais= 'aeiou'
contador= 0
print('Essas são as vogais')
for i in us:
    if i in vogais:
        print(i)
        contador+=1

print(f'total de vogais:{contador}')
    
