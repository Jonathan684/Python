import os
import pickle
from registro import * 
import random

'''
Enunciado:
    Una empresa de producciones cinematográficas mantiene información sobre las distintas películas que tiene en
    desarrollo. Por cada película se registran los datos siguientes: 
    número de identificación de la película (un número entero),
    título (una cadena), 
    importe invertido en su producción, 
    tipo de película (un valor entre 0 y 9 incluidos, de la forma 0: acción, 1: comedia, 2: drama, etc.) 
    y un número para identificar el pais de origen de la película (un número  entero entre 0 y 19 incluidos) 
    Se pide definir un tipo registro Pelicula con los campos que se indicaron, y un programa
    completo con menú de opciones para hacer lo siguiente:
    
    1- Cargar los datos de n registros de tipo Pelicula en un arreglo de registros (cargue n por teclado). Puede cargar los
        datos manualmente, o puede generarlos aleatoriamente. El arreglo debe crearse de forma que siempre quede
        ordenado de menor a mayor, según el título de las películas. Se considerará incorrecta la solución basada en cargar
        el arreglo completo y ordenarlo al final.
        
    2- Mostrar el arreglo creado en el punto 1, a razón de un registro por línea.
    
    3- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todas las películas cuyo pais de
        origen no sea el 10 y cuyo importe invertido sea menor a un valor x que se carga por teclado.

    4- Mostrar el archivo creado en el punto 3, a razón de un registro por línea en la pantalla.
    
    5- Buscar en el arreglo creado en el punto 1 un registro en el cual el número de identificación de la película sea igual a
        num (cargar num por teclado). Si existe, mostrar por pantalla todos los datos de ese registro. Si no existe, informar
        con un mensaje. La búsqueda debe detenerse al encontrar el primer registro que coincida con el patrón pedido.
    
    6- Usando el arreglo creado en el punto 1, determine la cantidad de películas de cada posible tipo por cada posible
        pais de origen (o sea, 10 * 20 = 200 contadores en una matriz de conteo). Muestre sólo los resultados que sean
        diferentes de 0.
'''

######################################################################################################
'''
    1- Cargar los datos de n registros de tipo Pelicula en un arreglo de registros (cargue n por teclado). Puede cargar los
        datos manualmente, o puede generarlos aleatoriamente. El arreglo debe crearse de forma que siempre quede
        ordenado de menor a mayor, según el título de las películas. Se considerará incorrecta la solución basada en cargar
        el arreglo completo y ordenarlo al final.
    
'''    
def carga_automatica(peliculas):
    titulo_peli =['Iron man', 'Avengers', 'Batman vs Superman', 'Romeo y Julieta']
    for i in range(len(peliculas)):
        num_id = i
        titulo = random.choice(titulo_peli)
        importe = round(random.uniform(0,10000),2)
        tipo_pelicula = random.randint(0, 2)  
        num_pais_origen = random.randint(0, 4)
        peliculas[i] = Pelicula(num_id, titulo, importe, tipo_pelicula, num_pais_origen)
    return peliculas 


'''
    2- Mostrar el arreglo creado en el punto 1, a razón de un registro por línea.
'''
def mostrar(peliculas):
    for i in range(len(peliculas)):
        print(peliculas[i])
        

'''
3- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todas las películas cuyo pais de
    origen no sea el 10 y cuyo importe invertido sea menor a un valor x que se carga por teclado.
'''
def generar_archivo(peliculas, fd, x): 
    f = open(fd, 'wb') # Abre el archivo si existe y si lo crea
    for pelicula in range(len(peliculas)): 
        if((peliculas[pelicula].num_pais_origen != 10) and (peliculas[pelicula].importe < x)):
            pickle.dump(peliculas[pelicula], f)
    f.close()
'''
    4- Mostrar el archivo creado en el punto 3, a razón de un registro por línea en la pantalla.
''' 
def mostrar_archivo(fd):
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
5- Buscar en el arreglo creado en el punto 1 un registro en el cual el número de identificación de la película sea igual a
   num (cargar num por teclado). Si existe, mostrar por pantalla todos los datos de ese registro. Si no existe, informar
   con un mensaje. La búsqueda debe detenerse al encontrar el primer registro que coincida con el patrón pedido.
'''   

def buscar_arreglo(peliculas):
    nom = int(input('Ingrese número de identificación de la película:'))
    for i in range(len(peliculas)):
        if peliculas[i].num_id == nom:
            print(peliculas[i])
        else:
            print('No hay coincidencias')
'''
    6- Usando el arreglo creado en el punto 1, determine la cantidad de películas de cada posible tipo por cada posible
       pais de origen (o sea, 10 * 20 = 200 contadores en una matriz de conteo). Muestre sólo los resultados que sean
       diferentes de 0.
'''
def cant_peli_x_país_origen(peliculas):
    filas = 10
    columnas = 20 
    m = [[0]*columnas for f in range(filas)]
    for i in range(len(peliculas)):
        m[peliculas[i].tipo_pelicula][peliculas[i].num_pais_origen] += 1 
    
    for j in  range(len(m)):
        for k in range(len(m[0])):
            if m[j][k] != 0:
                print('Tipo de película',j,' Cantidad por cada país : ',k , ' : ' ,m[j][k]) 

def validar_n(inf,mjs):
    n = int(input(mjs))
    while n <= inf:
        print('Error! Ingrese un número mayor a ' , inf, ':')  
        n = int(input())
    return n
def principal():
    peliculas = list() 
    opcion = -1
    pelicula= 'Registros.dat'
    while opcion != 0:
        print(50 * '-')
        print('MENÚ DE OPCIONES: ')
        print('EMPRESA DE PRODUCCIONES CINEMATOGRÁFICAS')
        print(50 * '-')
        print('1. Cargar automaticamente')
        print('2. Mostrar ')
        print('3. Crear un archivo de registros')
        print('4. Mostrar datos cargados previamente ')
        print('5. Buscar película')
        print('6. Cantidad de películas por país')
        print('0. Salir')
        
        opcion = int(input('Elija su opcion :'))
        if opcion == 1:
            n = validar_n(0,"Ingrese la cantidad de peliculas: ")
            peliculas = n * [0]
            peliculas = carga_automatica(peliculas)
        else:
            if len(peliculas) == 0:
                print('Debe ingresar la opcion 1.')  
            elif opcion == 2 :
                mostrar(peliculas)
            elif opcion == 3:
                x = validar_n(0,'Ingrese importe invertido en la pelicula: ') 
                generar_archivo(peliculas, pelicula, x)
            elif opcion == 4:
                mostrar_archivo(pelicula)
            elif opcion == 5:
               buscar_arreglo(peliculas)
            elif opcion == 6:
                cant_peli_x_país_origen(peliculas)
            elif opcion == 0:
                print('Hasta luego! :) ')         

if __name__ == '__main__':
    principal() 