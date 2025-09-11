# Enunciado: Crie uma função que receba um nome e um horário (manhã,
# tarde, noite) e retorne uma saudação personalizada.

nom= input('digite seu nome ')
hor= input ('digte seu horario')

def valores (nom,hor):
    if hor== 'manhã':
        print ('Olá',nom,'bom dia')
        
    elif hor== 'noite':
        print ('Olá',nom,'boa noite')

    elif hor== 'tarde':
        print('Olá',nom,'tarde')


valores (nom,hor)