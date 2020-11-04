#Não esta funcionando corretamente
#a = ()    
#b = {}
#c = []

entrada = (input("Digite a sua string, ela deve estar alinhada com um dos seguintes itens ({[]}):"))
abc =  ("({[]})")
ab =  ("({ })")   
bc =  ("{[]}")
a =  ("()")
b =  ("{ }" )
c =  ("[]") 

print(entrada)
if (entrada in abc):
    print("A string insirida está alinhada")
    True
elif (entrada in ab):
    print("A string insirida está alinhada")
    True
elif (entrada in bc):
    print("A string insirida está alinhada")
    True
elif (entrada in a):
    print("A string insirida está alinhada")
    True
elif (entrada in b):
    print("A string insirida está alinhada")
    True
elif (entrada in c):
    print("A string insirida está alinhada")
    True
else:
    print("A string não esta alinhada")
    False