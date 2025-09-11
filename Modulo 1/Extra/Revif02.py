list = {-2,-1,0,2,8,10,20}
positivo= 0
negativo= 0
zero= 0

for list in list:
    
    if list >0 :
        positivo=positivo+1
       
    elif list <0:
        negativo= negativo+1
    elif list ==0:
        zero= zero+1

print ('relatorio:')
print ('positivos:',positivo)
print ('negativos:',negativo)
print ('zeros:',zero)