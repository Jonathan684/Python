import random
import módulo as md
valor = round(random.uniform(1,2),2)
print(valor)

nombres = ["jonathan","nadia","cande"]
nombre = random.choice(nombres)
print(nombre)

n=3
Datos = n * [0]
## registro == clase
##Datos = 3 * [0]
print(50*"--")
Datos[0] = md.Alumnos("Manzana",20)
Datos[1] = md.Alumnos("Pera",20)
Datos[2] = md.Alumnos("Naranja",20)
#i=0
# while i != len(Datos)
    #pritn(Datos[i])
    #i +=1
v = []
v.append(2)
v.append(3)
v.append(1)
print(v)
for i in range(len(Datos)):
    print(Datos[i])



''''
Recorrer todo --> for o while
     mientras (condicion)
    encontrar en mayor --> if

print(Datos[0].fruta)
'''