<<<<<<< HEAD
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
    tipos_trabajo = ['interior','exterior','piletas', 'tapizados']
    nombre_trabajo = ['Limpieza', 'mantenimiento', 'pulidos','refacciones']
    for i in range(len(trabajos)):
        
        nomb_trabajo = random.choice(nombre_trabajo)
        num_id = i #random.randint(0,10) 
        tipo_trabajo = tipos_trabajo[random.randint(0,3)]
        importe_trab = round(random.uniform(0,1000),2)
        personal = random.randint(0,20)
        trabajos[i] = Trabajos(num_id, nomb_trabajo ,tipo_trabajo, importe_trab, personal)
    return trabajos

def mostrar(trabajos):
    for i in range(len(trabajos)):
        print(trabajos[i])

def ordenar_mayor(trabajos):
    n = len(trabajos)
    for i in range(n-1):
        for j in range (i + 1, n):
            if trabajos[i].importe_trab < trabajos[j].importe_trab:
                trabajos[i] , trabajos[j] = trabajos[j], trabajos[i]
    mostrar(trabajos)

def personal_por_trabajo(trabajos):
    
    Tipos_de_trabajos = ['interior' , 'exterior', 'piletas', 'tapizados']
    valores_a_comparar = len(Tipos_de_trabajos)*[0] # Inicializada en cero 
    indices = len(Tipos_de_trabajos) * [-1] # Inicializada en menos uno
    for i in range(len(Tipos_de_trabajos)):
        for j in range(len(trabajos)):
            if (Tipos_de_trabajos[i] == trabajos[j].descrip_trabajo) and (valores_a_comparar[i] < trabajos[j].personal):
                valores_a_comparar[i] = trabajos[j].personal
                indices[i] = j ## Guardo la posicion donde esta la mayor cantidad de personas                  
    for k in range(len(indices)):
        if(indices[k] != -1):
            print(Tipos_de_trabajos[k],'\n',trabajos[indices[k]])  

def personal_por_trabajo2(trabajos):
    may_int,id_int = 0, -1
    may_ext,id_ext = 0, -1
    may_pil,id_pil = 0, -1
    may_tap,id_tap = 0, -1
    for j in range(len(trabajos)):
        if ('interior' == trabajos[j].descrip_trabajo) and (may_int < trabajos[j].personal):
            may_int = trabajos[j].personal
            id_int = j
        elif ('exterior' == trabajos[j].descrip_trabajo) and (may_ext < trabajos[j].personal):
            may_ext = trabajos[j].personal
            id_ext = j
        elif ('piletas' == trabajos[j].descrip_trabajo) and (may_pil < trabajos[j].personal):
            may_pil = trabajos[j].personal     
            id_pil = j
        elif ('tapizados' == trabajos[j].descrip_trabajo) and (may_tap < trabajos[j].personal):    
            may_tap = trabajos[j].personal
            id_tap = j 
    
    if(id_int != -1):
        print("Mayor de interiores ", trabajos[id_int])
    if(id_ext != -1):
        print("Mayor de exteriores ", trabajos[id_ext])
    if(id_pil != -1):
        print("Mayor de piletas ", trabajos[id_pil])
    if(id_tap != -1):
        print("Mayor de tapizados ", trabajos[id_tap])            

def search_job(trabajos, descrip):
    Index = -1
    for i in range(len(trabajos)):
        if trabajos[i].descrip_trabajo == descrip:
            Index = i 
            break
    if Index != -1:
        print('Existe!' , trabajos[i])
    else:
        print('No existe tal descripción!')





def mostrar(trabajos):
    for i in range(len(trabajos)):
        print(trabajos[i])

def principal():
    trabajos = list() 
    opcion = -1
    while opcion != 0:
        print('MENÚ DE OPCIONES: ')
        print('COMPAÑÍA DE SERVICIOS')
        print(50 * '-')
        print('1. Cargar automaticamente')
        print('2. Mostrar ordenado')
        print('3. Personal por trabajo 1')
        print('4. Descripción de trabajo')
        print('5. Mostrar')
        print('0. Salir')
        
        opcion = int(input('Elija su opcion :'))
        if opcion == 1:
            n = validar_n(0)
            trabajos = n * [0]
            trabajos = carga_automatica(trabajos)
        else:
            if len(trabajos) == 0:
                print('Debe ingresar la opcion 1.')  
            elif opcion == 2 :
                ordenar_mayor(trabajos)
            elif opcion == 3:
                personal_por_trabajo(trabajos)
            elif opcion == 4:
                descrip = input('Ingrese la descripción del trabajo: ')
                search_job(trabajos, descrip)
                #personal_por_trabajo2(trabajos)
            elif opcion == 5:
                mostrar(trabajos)
if __name__ == '__main__':
    principal() 


'''
tapizados = index
piletas = index
exteriores = index
interiores = index
=======
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
    tipos_trabajo = ['interior','exterior','piletas', 'tapizados']
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

def ordenar_mayor(trabajos):
    n = len(trabajos)
    for i in range(n-1):
        for j in range (i + 1, n):
            if trabajos[i].importe_trab < trabajos[j].importe_trab:
                trabajos[i] , trabajos[j] = trabajos[j], trabajos[i]
    mostrar(trabajos)

def personal_por_trabajo(trabajos):
    
    Tipos_de_trabajos = ['interior' , 'exterior', 'piletas', 'tapizados']
    valores_a_comparar = len(Tipos_de_trabajos)*[0] 
    indices = len(Tipos_de_trabajos) * [0]
    for i in range(len(Tipos_de_trabajos)):
        for j in range(len(trabajos)):
            if Tipos_de_trabajos[i] == trabajos[j].descrip_trabajo:
                if valores_a_comparar[i] < trabajos[j].personal:
                    valores_a_comparar[i]= trabajos[j].personal
                    indices[i] = j
                    
    for k in range(len(indices)):
        print(Tipos_de_trabajos[k],'\n',trabajos[indices[k]])  

def personal_por_trabajo2(trabajos):
    may_int,id_int = 0, 0
    may_ext,id_ext = 0, 0
    may_pil,id_pil = 0, 0
    may_tap,id_tap = 0, 0
    for j in range(len(trabajos)):
        if ('interior' == trabajos[j].descrip_trabajo) and (may_int < trabajos[j].personal):
            may_int = trabajos[j].personal
            id_int = j
        elif ('exterior' == trabajos[j].descrip_trabajo) and (may_ext < trabajos[j].personal):
            may_ext = trabajos[j].personal
            id_ext = j
        elif ('piletas' == trabajos[j].descrip_trabajo) and (may_pil < trabajos[j].personal):
            may_pil = trabajos[j].personal     
            id_pil = j
        elif ('tapizados' == trabajos[j].descrip_trabajo) and (may_tap < trabajos[j].personal):    
            may_tap = trabajos[j].personal
            id_tap = j 

    print("Mayor de interiores ", trabajos[id_int])
    print("Mayor de exteriores ", trabajos[id_ext])
    print("Mayor de piletas ", trabajos[id_pil])
    print("Mayor de tapizados ", trabajos[id_tap])            
    
def mostrar(trabajos):
    for i in range(len(trabajos)):
        print(trabajos[i])

def principal():
    trabajos = list() 
    opcion = -1
    while opcion != 0:
        print('MENÚ DE OPCIONES: ')
        print('COMPAÑÍA DE SERVICIOS')
        print(50 * '-')
        print('1. Cargar automaticamente')
        print('2. Mostrar ordenado')
        print('3. Personal por trabajo 1')
        print('4. Personal por trabajo 2')
        print('5. Mostrar')
        print('0. Salir')
        
        opcion = int(input('Elija su opcion :'))
        if opcion == 1:
            n = validar_n(0)
            trabajos = n * [0]
            trabajos = carga_automatica(trabajos)
            ##numero = validar(0,3)
            #print('Número válido!', numero)
        
        else:
            if len(trabajos) == 0:
                print('Debe ingresar la opcion 1.')  
            elif opcion == 2 :
                ordenar_mayor(trabajos)
            elif opcion == 3:
                personal_por_trabajo(trabajos)
            elif opcion == 4:
                personal_por_trabajo2(trabajos)
            elif opcion == 5:
                mostrar(trabajos)
                
            


            
if __name__ == '__main__':
    principal() 


'''
tapizados = index
piletas = index
exteriores = index
interiores = index
>>>>>>> c28ad03 (Ejercicio 6)
'''