import os
import pickle
from registro import * 
import random
'''
Enunciado:
Un laboratorio farmacéutico mantiene información sobre los distintos medicamentos que produce.
Por cada medicamento se registran los datos siguientes: número de identificación (un entero),
nombre del medicamento (una cadena), precio de venta, tipo de medicamento (un valor entre 0 y 24 incluidos, por ejemplo: 0: oncológico, 1:pediátrico, etc.) 
y tipo de presentación (un número entero entre 0 y 9 incluidos, para indicar (por ejemplo): 0: cápsulas,1: inyectable, etc.) 

Se pide definir un tipo registro Medicamento con los campos que se indicaron, y un programa
completo con menú de opciones para hacer lo siguiente:

1- Cargar los datos de n registros de tipo Medicamento en un arreglo de registros (cargue n por teclado). 
Puede cargar los datos manualmente, o puede generarlos aleatoriamente.
El arreglo debe crearse de forma que siempre quede ordenado de menor a mayor,
según el número de identificación de los medicamentos,
y para hacer esto debe aplicar el algoritmo de inserción ordenada con búsqueda binaria. 
Se considerará directamente incorrecta la solución basada en cargar el arreglo completo y ordenarlo al final,
o aplicar el algoritmo de inserción ordenada, pero con búsqueda secuencial.


2- Mostrar el arreglo creado en el punto 1, a razón de un registro por línea.

3- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todos los registros cuyo tipo sea 0 o 1
y cuyo importe a facturar sea menor a un valor x que se carga por teclado.

4- Mostrar el archivo creado en el punto 3, a razón de un registro por línea en la pantalla.

5- Buscar en el arreglo creado en el punto 1 un registro en el cual el nombre del medicamento sea igual a nom 
(cargar nom por teclado). Si existe, mostrar por pantalla todos los datos de ese registro. 
Si no existe, informar con un mensaje.
La búsqueda debe detenerse al encontrar el primer registro que coincida con el patrón pedido.

6- Usando el arreglo creado en el punto 1, 
determine la cantidad de medicamentos de cada posible tipo por cada posible forma de presentación
(o sea, 25 * 10 = 250 contadores en una matriz de conteo). Muestre sólo los resultados diferentes de 0.
'''
 
'''5- Buscar en el arreglo creado en el punto 1 un registro en el cual el nombre del medicamento sea igual a nom 
(cargar nom por teclado). Si existe, mostrar por pantalla todos los datos de ese registro. 
Si no existe, informar con un mensaje.
La búsqueda debe detenerse al encontrar el primer registro que coincida con el patrón pedido.
'''

def cant_med_x_present(laboratorio):
    filas = 25
    columnas = 10 
    m = [[0]*columnas for f in range(filas)]
    for i in range(len(laboratorio)):
        m[laboratorio[i].tipo_medicamento][laboratorio[i].tipo_present] += 1 
    
    for j in  range(len(m)):
        for k in range(len(m[0])):
            if m[j][k] != 0:
                print('Tipo de medicamento',j,'Tipo de presentacion ',k , ' : ' ,m[j][k]) 
    

def buscar_arreglo(laboratorio):
    nom = input('Ingrese nombre del medicamento:')
    for i in range(len(laboratorio)):
        if laboratorio[i].nomb_medicamento == nom:
            print(laboratorio[i])


def mostrar_archivo(fd):
    print("Se muestra el archivo")
    if os.path.exists(fd):  
        f = open(fd, 'rb')
        size = os.path.getsize(fd) 
        while f.tell() < size:
            reg = pickle.load(f)
            print(reg)
        f.close()
    else:
        print('El archivo', fd, 'esta vacío')


'''
    3- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todos los registros cuyo tipo sea 0 o 1
    y cuyo importe a facturar sea menor a un valor x que se carga por teclado.
'''
def generar_archivo(registro, fd, x): 
    f = open(fd, 'wb') # Abre el archivo si existe y si lo crea
    for med in range(len(registro)): 
        if((registro[med].tipo_medicamento == 0) or (registro[med].tipo_medicamento == 1)) and (registro[med].precio_venta < x):
            pickle.dump(registro[med], f)
    f.close()


def mostrar(laboratorio):
    for i in range(len(laboratorio)):
        print(laboratorio[i])
        
def validar_n(inf,mjs):
    n = int(input(mjs))
    while n <= inf:
        print('Error! Ingrese un número mayor a ' , inf, ':')  
        n = int(input())
    return n
    
def carga_automatica(laboratorio):
    nombre_medic = ['CuraPlus', 'ABC', 'Ernec', 'Blastop', 'Clonazepan']
    for i in range(len(laboratorio)):
        numero_identificacion = i
        nomb_medicamento = random.choice(nombre_medic)
        precio_venta = round(random.uniform(0,10000),2)
        tipo_medicamento = random.randint(0, 2) ## NO OLVIDAR SACAR ESTOOOO 
        tipo_present = random.randint(0, 2)
        laboratorio[i] = Medicamentos(numero_identificacion, nomb_medicamento, precio_venta, tipo_medicamento, tipo_present)
    return laboratorio 

def principal():
    laboratorio = list() 
    opcion = -1
    nom_arch= 'Registros.dat'
    while opcion != 0:
        print(50 * '-')
        print('MENÚ DE OPCIONES: ')
        print('LABORATORIO DE MEDICAMENTOS')
        print(50 * '-')
        print('1. Cargar automaticamente')
        print('2. Mostrar ')
        print('3. Crear un archivo de registros')
        print('4. Mostrar datos cargados previamente : ')
        print('5. Buscar el nombre del medicamento : ')
        print('6. Buscar el nombre del medicamento : ')
        print('0. Salir')
        
        opcion = int(input('Elija su opcion :'))
        if opcion == 1:
            n = validar_n(0,"Ingrese la cantidad de medicamentos: ")
            laboratorio = n * [0]
            laboratorio = carga_automatica(laboratorio)
        else:
            if len(laboratorio) == 0:
                print('Debe ingresar la opcion 1.')  
            elif opcion == 2 :
                mostrar(laboratorio)
            elif opcion == 3:
                x = validar_n(0,'Ingrese importe del medicamento: ') 
                generar_archivo(laboratorio, nom_arch,x )
            elif opcion == 4:
                mostrar_archivo(nom_arch)
            elif opcion == 5:
                buscar_arreglo(laboratorio)
            elif opcion == 6:
                cant_med_x_present(laboratorio)            
if __name__ == '__main__':
    principal() 