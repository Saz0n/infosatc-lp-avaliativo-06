
numero = 0
def rotacao():
    numero = int(input("Digite o um numero negativo ou postivo:"))
    lista_01 = [1,2,3,4,5,6,7,8,9]
    if(numero<0):
        lista_01[8] = lista_01[7]
        lista_01[7] = lista_01[6]
        lista_01[6] = lista_01[5]
        lista_01[5] = lista_01[4]
        lista_01[4] = lista_01[3]
        lista_01[3] = lista_01[2]
        lista_01[2] = lista_01[1]
        lista_01[1] = lista_01[0]
        lista_01.pop(0)
        lista_01.insert(0,"9")
        print(lista_01)
    else:
        lista_01[0] = lista_01[1]
        lista_01[1] = lista_01[2]
        lista_01[2] = lista_01[3]
        lista_01[3] = lista_01[4]
        lista_01[4] = lista_01[5]
        lista_01[5] = lista_01[6]
        lista_01[6] = lista_01[7]
        lista_01[7] = lista_01[8]
        lista_01.pop(8)
        lista_01.insert(8,"1")
        print(lista_01)    
        
rotacao()

