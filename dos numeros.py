#este programa va a indentificardos numeros 19 y por lo menos 3 numeros 5
#9/26/2023 ernesto ihuit

list = [1,2,3,19,20,5,4,5,19,5]
contador19 = 0
contador5 = 0 
for i in range(len(list)):
    #print(i, "", list(i))
        if list[i] == 19:
            contador19 +=1
        
        if list[i] == 5:
            contador5 += 1
print (contador19, "", contador5)
if (contador19 == 2 and contador5 >= 3):
    print ("true")
else:
    print ("false")