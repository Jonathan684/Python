class Lineas:
    def __init__(self, numero_linea,nombr_titular,tipo_plan, cantidad_minutos, prov_linea):
        self.numero_linea = numero_linea
        self.nombr_titular = nombr_titular
        self.tipo_plan = tipo_plan
        self.cantidad_minutos = cantidad_minutos
        self.prov_linea = prov_linea

    
    def __str__(self): 
        s ='Número de Linea: {:^10} Nombre del titular: {:<20}Tipo de plan: {:<10}Cantidad de minutos consumidos: {:<10} Provincia donde se activó la línea: {:<10}'
        s = s.format(str(self.numero_linea) , self.nombr_titular, str(self.tipo_plan), str(self.cantidad_minutos), str(self.prov_linea))
        return s

def mostrar_menu():
    cad = '\n\nMenu de Opciones\n' \
          '=======================================\n' \
          '1 --- Cargar un vector con las líneas telefónicas\n' \
          '2 --- Listar todas las líneas\n' \
          '3 --- Generar un archivo\n' \
          '4 --- Informar la cantidad de minutos consumidos\n' \
          '5 --- Mostrar la línea con menor cantidad de minutos consumidos  \n' \
          '6 --- Buscar una línea \n' \
          '0 --- Salir\n' \
          'Ingrese su opcion: '
    return int(input(cad))

# 1 - Primero registro 
# 2 - Menu 
# 3 - Cargar el registro (Carga automatica) 
# 4 - Mostrar el registro 
# 5 - Las opciones