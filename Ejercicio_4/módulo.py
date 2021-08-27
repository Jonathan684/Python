
'''
#valor = round(random.uniform(1,2),2)
#print(valor)
#nombres = ["jonathan","nadia","cande"]
#nombre = random.choice(nombres)

'''
import random
class Atletas():
    def __init__(self, Nomb, Tiempo_Nat, Tiempo_ciclismo, Tiempo_corriendo):
        self.Nombre = Nomb
        self.Tiempo_Natacion = Tiempo_Nat
        self.Tiempo_ciclismo = Tiempo_ciclismo
        self.Tiempo_corriendo = Tiempo_corriendo 
    def __str__(self):
        cadena = self.Nombre + " " + str(self.Tiempo_Natacion) + " " + str(self.Tiempo_ciclismo) + " " + str(self.Tiempo_corriendo)
        
        #r += '{:<15}'.format('Codigo: '+str(self.codigo))
        return cadena 

def cargar_datos_manual(vector):
    for i in range(len(vector)):
        atleta = str(input("Ingrese nombre del atleta: "))
        tiempo_n = float(input("Ingrese tiempo de natación: "))
        tiempo_c = float(input("Ingrese tiempo ciclismo: "))
        tiempo_corr = float(input("Ingrese tiempo corriendo: "))
        vector[i] = md.Atletas(atleta, tiempo_n, tiempo_c, tiempo_corr)
    return vector

def cargar_datos_automatico(vector):
    cadena = ("Nadia","Jonathan","Cande")
    for i in range(len(vector)):
        atleta = random.choice(cadena)
        tiempo_n = round (random.uniform(1,4), 2)
        tiempo_c = round (random.uniform(1,4), 2)
        tiempo_corr = round (random.uniform(1,4), 2)
        vector[i] = Atletas(atleta, tiempo_n, tiempo_c, tiempo_corr)
    return vector