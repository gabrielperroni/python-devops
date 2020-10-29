name = "Variavel" 
valor_name = 10.0
name_isvalid = True

print(name, valor_name, name_isvalid, sep='\n', end='\n')

print(type(valor_name))
print(name[0:2])

print('Teste de interpolação %s mais um %.2f' %(name, valor_name))

print('Teste de interpolação {} mais um {}' .format(name, valor_name))
print('Teste de interpolação {} mais um {:.3f}' .format(name, valor_name))


###17. Solicitando entrada ao usuário

print('Input Function')
input_variable = input('Type something now.')
print(input_variable + ' was typed')
print(f'What you typed was {input_variable}')


 #  18. Controle de fluxo com while	

print('while')
status = 1
while status == 1:
    status = int(input('Type somthing different from 1 to exit  '))

 #  19. Condições - IF/ELIF/ELSE	


 
 #  20. Primeira estrutura de dados - LISTA	

 list01 = []
count = 0

while count < 5:
    count += 1
    list01.append('FFFF' + str(count))
    print(list01)

    
 #  21. Controle de fluxo com FOR	

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

 #  22. Função Range	
 #  23. Função Enumerate
 #  24. Estrutura de dados - Dicionario	
 #  25. Estrutura de dados - Tuplas	
 #  26. Estrutura de dados - Conjuntos	
 #  27. Entrada e saída de arquivos	
 #  28. Manipulando arquivos CSV	
 #  29. Manipulando JSON - Serializar	
 #  30. Manipulando JSON - Deserializar	
 #  31. Funções: Introdução	
 #  32. Funções: Variáveis Locais e Globais	
 #  33. Funções: Parametros opcionais	
 #  34. Funções: Parametros nomeados	
 #  35. Tratativa de erros e exceções	
 #  36. Bibliotecas e gerenciamento de pacotes