import módulo as md

'''
Para calcular el promedio se debe sumar las cantidad de tiempo y 
dividirlo en la cantidad de participantes.
 T_N  5
 T_CI 4
 T_COR 1

 TIMEPO PROMEDIO =  3/10 

 Sumar los tiempo de una instancia del vector, ejemplo:
 V[0].Tiempo_natación + V[0].Tiempo_ciclismo + V[0].Tiempo_corriendo = T_total

 Cantidad_competencias = 3
 promedio = Cantidad_competencias / T_total

 Esto tambien se repite para v[1]. Se recomienda usar un ciclo for con un rango
 igual al tamaño del vector (len(vector))
 Anexo : El indice del ciclo for va a ser el indice para recorrer el vector.
 i.e v[i]
 '''
def promedio(vector):
    promedio_por_participante = len(vector) * [0]
    Cantidad_competencias = 3
    for i in range(len(vector)):
        suma = vector[i].Tiempo_Natacion + vector[i].Tiempo_ciclismo + vector[i].Tiempo_corriendo
        promedio_por_participante[i] = round((suma / Cantidad_competencias),2)
    
    return promedio_por_participante
        


###Cargar automatica
primer_atleta = 0
##TODO SE TIENE QUE VALIDAR
def principal():
    n = int(input("Ingrese la cantidad de atletas : "))
    #validar(n)
    vector = n * [0]
    promedio_por_participante = n*[0]
    #vector = cargar_datos_manual(vector)
    vector = md.cargar_datos_automatico(vector)
    promedio_por_participante  = promedio(vector)
    promedio(vector)
    for i in range(len(vector)):
        print(vector[i])

    for i in range(len(promedio_por_participante)):
        print(promedio_por_participante[i])


 
    

if __name__ == '__main__':
    principal()