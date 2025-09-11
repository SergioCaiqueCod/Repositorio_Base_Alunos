# Enunciado: Crie uma função que receba dois números e uma operação (+, -,
# *, /) e retorne o resultado da operação.
n1= int(input('digite um numero'))
n2= int(input('digite um numero'))
escolha= input('somar,subtração,dividir, multiplicar')

def somas (n1,n2,escolha):
    if escolha == 'soma':
        print (n1+n2)

    elif escolha == 'dividir':
        print (n1/n2)
    
    elif escolha == 'multiplicar':
        print (n1*n2)

    elif escolha == 'subtração':
        print (n1-n2)

somas (n1,n2,escolha)