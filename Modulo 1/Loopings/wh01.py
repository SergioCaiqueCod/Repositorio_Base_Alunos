# # peça ao usuario para digitar uma senha e valida a senha o codigo nao deve parar caso o
# usuario digite a senha incorreta

senha= input('digite sua senha:')

while senha!= '1234':
    print ('acesso negado')

    senha= input ('digite sua senha:')


print('acesso liberado')

