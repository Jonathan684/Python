class libros():
    def __init__(self,nombre, precio,idioma):
        self.nombre = nombre
        self.precio = precio
        self.idioma = idioma


def buscar_mayor_precio(vector):
    idioma = int(input('Ingrese el idioma a buscar: '))
    temp1 = vector[0].idioma
    precio = 0
    flag = 0
    #temp2 = vector[0].precio
    for i in range(1,len(vector)):
        if vector[i].idioma == idioma:
            if(flag == 0):
                precio = vector[i].precio
                flag = 1
            elif(precio < vector[i]):
                precio = vector[i]
    return precio                

''' mayor = indice = 0

    for i in range(len(vector)):
        if idioma == vector[i].idioma:
            if vector[i].precio > mayor:
                mayor = vector[i].preciols
                
                indice = i
                print('El libro de mayor precio del idioma')
'''
def principal():
    v = 3 * [0]
    v[0] = libros("El principito", 45 , "español" )
    v[1] = libros("Romeo y Julieta", 34 ,'francés')
    v[2] = libros("Jumanji", 20 , 'español')
    precio = buscar_mayor_precio(v)
    print("Precio ",precio)