idade= int(input('digte sua idade:'))
estud= input('você é estudante (sim/não)?')

if estud== 'não' and idade >0 and idade <12:
    print ('o valor do ingrsso é 8,00 reais.')

elif estud== 'sim' and idade >0 and idade <=100:
    print ('o valor do ingresso é de 12,00 reais.')

elif estud == 'não' and idade >65 and idade <=100:
    print ('o valor do ingrsso é de 10,00 reais.')
    
elif estud== "não" and idade >=13 and idade <64:
    print ('o valor do ingresso é de 20,00 reais.')