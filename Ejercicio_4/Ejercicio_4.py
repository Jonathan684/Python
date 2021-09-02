import módulo as md

def cargar_datos_manual(vector):
    for i in range(len(vector)):
        atleta = str(input("Ingrese nombre del atleta: "))
        tiempo_n = float(input("Ingrese tiempo de natación: "))
        tiempo_c = float(input("Ingrese tiempo ciclismo: "))
        tiempo_corr = float(input("Ingrese tiempo corriendo: "))
        vector[i] = md.Atletas(atleta, tiempo_n, tiempo_c, tiempo_corr)
    return vector

def promedio(vector):
    promedio_por_participante = len(vector) * [0]
    Cantidad_competencias = 3
    for i in range(len(vector)):
        suma = vector[i].Tiempo_Natacion + vector[i].Tiempo_ciclismo + vector[i].Tiempo_corriendo
        promedio_por_participante[i] = round((suma / Cantidad_competencias),2)
    for i in range(len(promedio_por_participante)):
        print("Promedio ",promedio_por_participante[i],vector[i].Nombre)
    return promedio_por_participante

def definir_podio(promedio_por_participante, vector):
    aux = promedio_por_participante.copy() # Copia en vector en otro
    aux.sort(reverse=True)  # Ordenarla de forma inversa
    top_diez = aux[:3]  # Y capturar los 3 primeros elementos
    pos1 = promedio_por_participante.index(top_diez[0])
    pos2 = promedio_por_participante.index(top_diez[1])
    pos3 = promedio_por_participante.index(top_diez[2])    
    print("Podio 1:"+vector[pos1].Nombre+" Podio 2:"+vector[pos2].Nombre+" Podio 3:"+vector[pos3].Nombre)
    


def principal():
    vector = list()
    promedio_por_participante = list()
    opcion = -1
    while opcion !=0:
        print('\nAtletismo')
        print('1. Cargar')
        print('0. Salir')
        
        opcion = int(input('Elija su opcion :'))
        
        if opcion == 1:
            print('1. Carga (M)anual o (A)utomatica? ')
            carga =  input('Elija su opcion :')
            if carga == 'm':
                n = int(input("Ingrese la cantidad de atletas : "))
                vector = n * [0]
                vector = cargar_datos_manual(vector)
            elif carga == 'a':
                n = int(input("Ingrese la cantidad de atletas : "))
                vector = n * [0]
                vector = md.cargar_datos_automatico(vector)
        
        promedio_por_participante  = promedio(vector)
        print(40*'_')
        definir_podio(promedio_por_participante,vector)
        print(40*'_')

if __name__ == '__main__':
    principal()