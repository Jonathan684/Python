'''
Empresa celulares
Una empresa dedicada a la venta de líneas para celulares nos pidió un
 programa que permita realizar una serie de informes. 
De cada línea se sabe numero, titular, tipo de plan (valor de 0 a 19), 
cantidad de minutos consumidos, provincia donde se activo la línea (valor de 1 a 23)

Usted debe realizar dicho programa, controlado por un 
menú de opciones para que lleve a cabo los siguientes ítems:

1 - Cargar un vector de n Líneas, validando que el tamaño a cargar sea mayor a 
cero y que el tipo de producto y tipo de plan sean válidos. 
El Arreglo debe generarse en forma ordenada por numero.

2 - Listar todas las líneas a razón de un registro por vez

3 - Generar un archivo binario con todas las líneas donde la cantidad de minutos 
consumidos superen un valor X ingresado por teclado. 

Muestre dicho archivo a razón de una registro a la vez y al 
final indique que porcentaje representan las líneas del plan Y 
ingresado por parámetro sobre el total de líneas del archivo.

4 - Determinar e informar la cantidad de minutos consumidos 
 por cada tipo de plan y en cada provincia
 a la que pertenece esa línea. Son 460 contadores

5 - Mostrar la línea con menor cantidad de minutos consumidos 
para las provincias x o y 
(donde ambos valores son ingresados por parámetro), 
en caso que haya mas de una mostrarlas a todas

6 - Buscar una línea X ingresada por teclado. 
Si existe incrementar sus minutos consumidos en un 20% y 
mostrar los datos de la línea. Caso contrario indicar con 
un mensaje que no existe
'''


import os
import pickle
from registro import * 
import random

def validar_entre(min, max):
    numero = int(input('Ingrese el número de provincia: '))
    while (numero <= min) and (numero >= max):
            numero = int(input('Error! Ingrese un número comprendido entre 0 y 3: '))
    return numero

def mostrar(lineas_tel):
    for i in range(len(lineas_tel)):
        print(lineas_tel[i])
        
def validar_opcion(inf,mjs):
    n = int(input(mjs))
    while n <= inf:
        print('Error! Ingrese un número mayor a ' , inf, ':')  
        n = int(input())
    return n
    
def add_in_order(lineas_tel, registro):
    izq, der = 0, len(lineas_tel)-1
    while izq <= der :
        c = (izq + der) // 2
        if lineas_tel[c].numero_linea == registro.numero_linea:
            pos = c
            break
        if registro.numero_linea < lineas_tel[c].numero_linea:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    lineas_tel[pos:pos] = [registro]
'''
    Una empresa dedicada a la venta de líneas para celulares nos pidió un
    programa que permita realizar una serie de informes. 
    De cada línea se sabe numero, titular, tipo de plan (valor de 0 a 19), 
    cantidad de minutos consumidos, provincia donde se activo la línea (valor de 1 a 23)
'''
def carga_automatica(lineas_tel,n):  ## Cambio del parcial 1 al 2 
    nombre_titular = ['Nadia', 'Matías', 'Facundo', 'Jonathan', 'Candelaria', 'Florencia','Andrés','Cristiano','Gerard','Ana','Enzo','Eric']
    for i in range(n):
        numero_linea = i +1
        nombr_titular = random.choice(nombre_titular)
        tipo_plan = random.randint(0, 19) 
        cantidad_minutos = round(random.uniform(0,10000),2)
        prov_linea = random.randint(1, 23)
        registro = Lineas(numero_linea, nombr_titular,tipo_plan,cantidad_minutos, prov_linea)
        add_in_order(lineas_tel, registro)
    print("Registro generado")
    return lineas_tel


''' 
    3 - Generar un archivo binario con todas las líneas donde la cantidad de minutos 
    consumidos superen un valor X ingresado por teclado. 
    
    Muestre dicho archivo a razón de una registro a la vez y al 
    final indique que porcentaje representan las líneas del plan Y 
    ingresado por parámetro sobre el total de líneas del archivo
'''
def generar_archivo(lineas_tel, nombre_archivo, x): 
    f = open(nombre_archivo, 'wb') # Abre el archivo si existe y si lo crea
    for linea_telefono in lineas_tel:
        if((linea_telefono.cantidad_minutos > x)):
            pickle.dump(linea_telefono, f)
    f.close()
    print('Archivo creado !')

'''
    Muestre dicho archivo a razón de una registro a la vez y al 
    final indique que porcentaje representan las líneas del plan Y 
    ingresado por parámetro sobre el total de líneas del archivo
'''
def mostrar_archivo(nombre_archivo, plan_Y):
    if os.path.exists(nombre_archivo):  
        f = open(nombre_archivo, 'rb')
        size = os.path.getsize(nombre_archivo) 
        minutos_total = 0
        while f.tell() < size:
            reg = pickle.load(f)
            minutos_total += reg.cantidad_minutos
            print(reg)
        f.close()
    else:
        print('El archivo', nombre_archivo, 'esta vacío')
    porcentaje = ((plan_Y.cantidad_minutos / minutos_total) * 100)
    print('El porcentaje obtenido es: ', porcentaje, '% ')

def buscar_registro(profesionales):
    nom = input('Ingrese nombre del profesional: ')
    for i in range(len(profesionales)):
        if profesionales[i].nombr_profesional == nom: 
            print(profesionales[i])
            return   
    print('No hay coincidencias')


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

def buscar_plan(lineas_tel, num_lin):
    izq, der = 0, len(lineas_tel) - 1
    while izq <= der:
        c = (izq + der) // 2
        if lineas_tel[c].numero_linea == num_lin:
            return c 
        if num_lin < lineas_tel[c].numero_linea:
            der = c - 1
        else:
            izq = c + 1
    return -1
'''
    4- Determinar e informar la cantidad de minutos consumidos 
    por cada tipo de plan y en cada provincia
    a la que pertenece esa línea. Son 460 contadores
'''
def cant_minutos_x_cada_prov(lineas_tel):
    filas = 20
    columnas = 23
    m = [[0]*columnas for f in range(filas)]
    for i in range(len(lineas_tel)):
        m[lineas_tel[i].tipo_plan][lineas_tel[i].prov_linea-1] += 1 
    
    for j in  range(len(m)):
        for k in range(len(m[0])):
            if m[j][k] != 0:
                print('Tipo de plan',j,' En provincia : ',k , ' : ' ,m[j][k]) 





'''
5 - Mostrar la línea con menor cantidad de minutos consumidos 
   para las provincias x o y 
   (donde ambos valores son ingresados por parámetro), 
   en caso que haya mas de una mostrarlas a todas
'''  

def mostrar_linea(lineas_tel):
    prov_1 = validar_entre(0, 23)
    prov_2 = validar_entre(0, 23)
    minutos_men = 9999999999
    indice = 0
    for i in range(len(lineas_tel)):
        if lineas_tel[i].prov_linea == prov_1  or lineas_tel[i].prov_linea == prov_2 :
            if lineas_tel[i].cantidad_minutos < minutos_men:
                minutos_men = lineas_tel[i].cantidad_minutos
                indice = i
    print(lineas_tel[indice])       
 
'''
    6 - Buscar una línea X ingresada por teclado. 
    Si existe incrementar sus minutos consumidos en un 20% y 
    mostrar los datos de la línea. Caso contrario indicar con 
    un mensaje que no existe
    ## linea.cantidad_minutos ---------- 100
    ## incremento            = ---------- 20
'''
def buscar_arreglo(lineas_tel):
    num = validar_opcion(0, 'Ingrese número de línea:')
    flag = False
    for linea in lineas_tel:  
        if linea.numero_linea == num:
            linea.cantidad_minutos += ((linea.cantidad_minutos * 20)/ 100)
            flag = True
            print(linea)                
    if flag == False:
        print('No existe el númerode línea buscada')


def principal():
    #profesionales = [] ## Como la por insercion ordenada generamos una lista vacia
    nombre_archivo = 'Registros.dat'
    opcion = -1
    while opcion != 0: ### <<--------------------
        opcion = mostrar_menu()
        if opcion == 1:
            lineas_tel = []
            n = validar_opcion(0, 'Ingrese cantidad de registros: ')
            lineas_tel = carga_automatica(lineas_tel,n)
        elif len(lineas_tel) > 0:
            if opcion == 2:
                mostrar(lineas_tel)


            elif opcion == 3:
                x = validar_opcion(0, 'Ingrese cantidad de minutos consumidos:')
                num_lin = validar_opcion(0, 'Ingrese número de linea: ')
                pos = buscar_plan(lineas_tel,num_lin)
                if pos == -1:    
                    print("La linea no existe")
                else :
                    generar_archivo(lineas_tel, nombre_archivo, x)
                    mostrar_archivo(nombre_archivo,lineas_tel[pos])
            elif opcion == 4:
                cant_minutos_x_cada_prov(lineas_tel)
            elif opcion == 5:
                mostrar_linea(lineas_tel)
            elif opcion == 6:
                buscar_arreglo(lineas_tel)
            elif opcion == 0:
                print('Hasta luego! :)')
        else:
            print('Primero debe cargar el datos en el registro por favor.')
if __name__ == '__main__':
    principal()