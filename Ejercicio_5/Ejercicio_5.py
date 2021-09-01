import random
from registro import *
#import registro as re
def validar_n(n):
    numero = int(input('Ingrese el número de trabajos: '))
    while True:
        if(numero > n):
            return numero       
        else:
            numero = int(input('Error! Ingrese un número mayor a 0: '))

def validar(min, max):
    numero = int(input('Ingrese el número identificador del trabajador: '))
    while True:
        if(numero >= min) and (numero <= max):
            return numero       
        else:
            numero = int(input('Error! Ingrese un número comprendido entre 0 y 3: '))
        
def carga_automatica(trabajos):
    tipos_trabajo = ['interios','exterior','piletas', 'tapizados']
    for i in range(len(trabajos)):
        num_id = random.randint(0,3)
        descrip_trabajo = tipos_trabajo[num_id]
        importe_trab = round(random.uniform(0,1000),2)
        personal = random.randint(0,20)
        trabajos[i] = Trabajos(num_id, descrip_trabajo, importe_trab, personal)
    return trabajos

def mostrar(trabajos):
    for i in range(len(trabajos)):
        print(trabajos[i])


def principal():
    trabajos = list() 
    
    opcion = -1
    while opcion != 0:
        print('Compañía de servicios')
        print('1. Cargar')
        print('2. Sin definir')
        print('3. Sin definir')
        print('4. Mostrar')
        print('0. Salir')
        opcion = int(input('Elija su opcion :'))
        
        if opcion == 1:
            n = validar_n(0)
            trabajos = n * [0]
            trabajos = carga_automatica(trabajos)
            ##numero = validar(0,3)
            #print('Número válido!', numero)
        if opcion == 4:
            mostrar(trabajos)




            
if __name__ == '__main__':
    principal() 
