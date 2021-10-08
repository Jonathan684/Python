import os
import pickle
from registro import * 
import random

'''
    Un colegio o asociación de profesionales mantiene información sobre sus distintos miembros. 
    Por cada miembro se registran los campos siguientes: número de dni del profesional (un número entero), 
    nombre del profesional (una cadena),
    importe que paga al colegio por mes,
    tipo de afiliación (un valor entre 0 y 4 incluidos, por ejemplo de la forma 0: vitalicio, 1: transitorio, 2: indirecto, etc.) 
    y un número que identifica el tipo de trabajo que desempeña (un número entero entre 0 y 14 incluidos, para indicar 
    (por ejemplo): 0: empleado, 1: jefe o director, 2: administrativo, etc.) 
    Se pide definir un tipo registro Profesional con los campos que se indicaron, y un programa completo con menú de opciones para hacer lo siguiente:

    1- Cargar los datos de n registros de tipo Profesional en un arreglo de registros (cargue n por teclado). 
    Puede cargar los datos manualmente, o puede generarlos aleatoriamente. 
    El arreglo debe crearse de forma que siempre quede ordenado de menor a mayor, según el dni de los profesionales. 
    Se considerará incorrecta la solución basada en cargar el arreglo completo y ordenarlo al final.

    2- Mostrar el arreglo creado en el punto 1, a razón de un registro por línea.

    3- Buscar en el arreglo creado en el punto 1 un profesional con dni igual a un valor doc (doc es cargado por teclado). 
    Si no existe, informar con un mensaje. Si existe mostrar todos sus datos, al final agregar un mensaje que indique que tiene el importe desactualizado, 
    si es menor a un valor imp (tambien cargado por teclado)

    4- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todos los profesionales cuyo tipo de trabajo sea 3, 4 o 5 
    y cuyo importe pagado mensual sea mayor a un valor x que se carga por teclado.

    5- Mostrar el archivo creado en el punto 3, a razón de un registro por línea en la pantalla.
    
    6- Buscar en el arreglo creado en el punto 1 un registro en el cual el nombre del profesional sea igual a nom (cargar nom por teclado). 
    Si existe, mostrar por pantalla todos los datos de ese registro. Si no existe, informar con un mensaje. 
    La búsqueda debe detenerse al encontrar el primer registro que coincida con el patrón pedido.

    7- Usando el arreglo creado en el punto 1, determine la cantidad de profesionales de cada posible tipo d afiliación por cada posible tipo de trabajo 
    (o sea, 5 * 15 = 75 contadores en una matriz de conteo). Muestre sólo los resultados que sean diferentes de 0.
''' 

def mostrar(profesional):
    for i in range(len(profesional)):
        print(profesional[i])
        
def validar_opcion(inf,mjs):
    n = int(input(mjs))
    while n <= inf:
        print('Error! Ingrese un número mayor a ' , inf, ':')  
        n = int(input())
    return n
    
def add_in_order(profesional, registro):
    izq, der = 0, len(profesional)-1
    while izq <= der :
        c = (izq + der) // 2
        if profesional[c].numero_DNI == registro.numero_DNI:
            pos = c
            break
        if registro.numero_DNI < profesional[c].numero_DNI:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    profesional[pos:pos] = [registro]

def carga_automatica(profesional,n):  ## Cambio del parcial 1 al 2 
    nombre_profesional = ['Nadia', 'Matías', 'Facundo', 'Jonathan', 'Candelaria', 'Florencia','Andrés','Cristiano','Gerard','Ana','Enzo','Eric']
    for i in range(n):
        numero_DNI = i
        nombr_profesional = random.choice(nombre_profesional)
        importe_x_mes = round(random.uniform(0,10000),2)
        tipo_afiliación = random.randint(0, 4) 
        tipo_trabajo = random.randint(0, 14)
        registro = Colegio(numero_DNI, nombr_profesional, importe_x_mes, tipo_afiliación, tipo_trabajo)
        add_in_order(profesional, registro)
    print("Registro generado")
    return profesional 
'''
    3- Buscar en el arreglo creado en el punto 1 un profesional con dni igual a un valor doc (doc es cargado por teclado). 
    Si no existe, informar con un mensaje. Si existe mostrar todos sus datos, al final agregar un mensaje que indique que tiene el importe desactualizado, 
    si es menor a un valor imp (tambien cargado por teclado)
'''
def buscar_arreglo(profesional):
    nom = int(input('Ingrese número de DNI del profesional:'))
    flag = False
    for i in range(len(profesional)):
        if profesional[i].numero_DNI == nom:
            flag = True
            print('Profesional encontrado con éxito!')
            print(profesional[i])
            imp = int(input('Ingrese importe que abona por mes: '))
            if  profesional[i].importe_x_mes < imp:            
                print('Su importe está desactualizado!')
    if flag == False :
        print('No existe tal profesional!')

''' 4- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todos los profesionales cuyo tipo de trabajo sea 3, 4 o 5 
    y cuyo importe pagado mensual sea mayor a un valor x que se carga por teclado.
'''
def generar_archivo(profesionales, nombre_archivo, x): 
    f = open(nombre_archivo, 'wb') # Abre el archivo si existe y si lo crea
    for profesional in profesionales:
        if((profesional.tipo_trabajo == 3 or profesional.tipo_trabajo ==  4 or profesional.tipo_trabajo ==  5) and (profesional.importe_x_mes > x)):
            pickle.dump(profesional, f)
    f.close()
    print('Archivo creado !')
''' 
  5- Mostrar el archivo creado en el punto 3, a razón de un registro por línea en la pantalla.
'''    
def mostrar_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):  
        f = open(nombre_archivo, 'rb')
        size = os.path.getsize(nombre_archivo) 
        while f.tell() < size:
            reg = pickle.load(f)
            print(reg)
        f.close()
    else:
        print('El archivo', nombre_archivo, 'esta vacío')

'''
    6- Buscar en el arreglo creado en el punto 1 un registro en el cual el nombre del profesional sea igual a nom (cargar nom por teclado). 
    Si existe, mostrar por pantalla todos los datos de ese registro. Si no existe, informar con un mensaje. 
    La búsqueda debe detenerse al encontrar el primer registro que coincida con el patrón pedido.
'''

def buscar_registro(profesionales):
    nom = input('Ingrese nombre del profesional: ')
    for i in range(len(profesionales)):
        if profesionales[i].nombr_profesional == nom: 
            print(profesionales[i])
            return   
    print('No hay coincidencias')
'''
    7- Usando el arreglo creado en el punto 1, determine la cantidad de profesionales de cada posible tipo d afiliación por cada posible tipo de trabajo 
    (o sea, 5 * 15 = 75 contadores en una matriz de conteo). Muestre sólo los resultados que sean diferentes de 0.
'''
def cant_prof_x_tipo_afiliación(profesionales):
    filas = 5
    columnas = 15 
    m = [[0]*columnas for f in range(filas)]
    for i in range(len(profesionales)):
        m[profesionales[i].tipo_afiliación][profesionales[i].tipo_trabajo] += 1 
    
    for j in  range(len(m)):
        for k in range(len(m[0])):
            if m[j][k] != 0:
                print('Tipo de afiliación',j,'Tipo de trabajo ',k , ' : ' ,m[j][k]) 
    
def principal():
    profesionales = [] ## Como la ppor insercion ordenada generamos una lista vacia
    nombre_archivo = 'profesional.dat'
    opcion = -1
    while opcion != 0: ### <<--------------------
        opcion = menu()
        if opcion == 1:
            n = validar_opcion(0, 'Ingrese cantidad de profesionales: ')
            profesionales = carga_automatica(profesionales,n)
        elif len(profesionales) > 0:
            if opcion == 2:
                print("mostrar")
                mostrar(profesionales)
            elif opcion == 3:
                buscar_arreglo(profesionales)
            elif opcion == 4:
                x = float(input('Ingrese un importe: '))
                generar_archivo(profesionales, nombre_archivo, x)
            elif opcion == 5:
                mostrar_archivo(nombre_archivo)
            elif opcion == 6:
                buscar_registro(profesionales)
            elif opcion == 7:
                cant_prof_x_tipo_afiliación(profesionales)
            elif opcion == 0:
                print('Hasta luego! :)')
        else:
            print('Primero debe cargar el arreglo de tipo de profesionales')


if __name__ == '__main__':
    principal()
