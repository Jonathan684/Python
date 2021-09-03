from hashlib import blake2b
import random 
from registro import *


def pac_practicas (historiales):
    acumulador = 30 * [0]  
    for i in range(len(acumulador)):
        for j in range(len(historiales)):
            if i == historiales[j].tipo_practicas:
                acumulador[i] += 1
    #s = ' '            
    for k in range(len(acumulador)):
        #if(acumulador[k] != -1):
        print( " Tipo de practica ", k ,":  ", 'Cantidad de pacientes por esta especialidad: ' , acumulador[k])
        #s += str(acumulador[k]) +" "
    #print(s)


def num_ID_cant_trat (historiales, numero_ident, cant_días_tratamiento):
        indice = -1
        for i in range(len(historiales)):
            if (historiales[i].numero_identif == numero_ident) and (historiales[i].cantidad_días <= cant_días_tratamiento):
                indice = i
                break
        if indice != -1:
            print('Existe! \n Los datos del paciente son: ' , historiales[indice])
        else:
            print('No existe paciente con tal característica!')


def validar_n(n):
    numero = int(input('Ingrese el número de pacientes: '))
    while True:
        if(numero > n):
            return numero       
        else:
            numero = int(input('Error! Ingrese un número mayor a 0: '))
        
        
def carga_automatica(historiales):
    nombr_pac = ['Claudia', 'Jonathan', 'Julia', 'Candelaria', 'Maria', 'Nadia', 'Matias', 'Ana']
    for i in range(len(historiales)):
        numero_identif = i
        nombr_paciente = random.choice(nombr_pac)
        tipo_practica = random.randint(0,29)
        cantidad_dia = random.randint(1,100)
        cantidad_de_med = random.randint(1,20)
        historiales[i] = Servicio(numero_identif, nombr_paciente, tipo_practica, cantidad_dia,cantidad_de_med )
    return historiales 


def ordenar_mayor(historiales):
    n = len(historiales)
    for i in range(n-1):
        for j in range (i + 1, n):
            if historiales[i].nombre_paciente > historiales[j].nombre_paciente:
                historiales[i] , historiales[j] = historiales[j], historiales[i]
    mostrar(historiales)


def mostrar(historiales):
    for i in range(len(historiales)):
        print(historiales[i])


def principal():
    historiales = list() 
    opcion = -1
    while opcion != 0:
        print('\n')
        print(50 * '*')
        print('*        MENÚ DE OPCIONES: ')
        print('* ZONA DE EMERGENCIAS. PLANILLAS DE PACIENTES')
        print(50 * '*')
        print('1. Ingresar cantidad de pacientes:')
        print('2. Mostrar ordenado los datos del paciente')
        print('3. Cantidad de pacientes por cada tipo de práctica')
        print('4. Buscar paciente')
        print('5. Mostrar')
        print('0. Salir')
        
        opcion = int(input('Elija su opcion :'))
        if opcion == 1:
            n = validar_n(0)
            historiales = n * [0]
            historiales = carga_automatica(historiales)
        else:
            if len(historiales) == 0:
                print('\n', 'DEBE INGRESAR LA OPCION 1!')  
            elif opcion == 2 :
                ordenar_mayor(historiales)
            elif opcion == 3:
                pac_practicas (historiales)
            elif opcion == 4:
                numero_ident= int(input('Ingrese número de identificación del paciente: '))
                cant_días_tratamiento = int(input('Ingrese cantidad de días del tratamiento: '))
                num_ID_cant_trat (historiales, numero_ident, cant_días_tratamiento)
            elif opcion == 5:
                mostrar(historiales)

if __name__ == '__main__':
    principal()