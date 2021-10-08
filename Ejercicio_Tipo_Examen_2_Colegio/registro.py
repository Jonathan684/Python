class Colegio:
    def __init__(self, numero_DNI,nombr_profesional,importe_x_mes, tipo_afiliación, tipo_trabajo):
        self.numero_DNI = numero_DNI
        self.nombr_profesional = nombr_profesional
        self.importe_x_mes = importe_x_mes
        self.tipo_afiliación = tipo_afiliación
        self.tipo_trabajo = tipo_trabajo

    
    def __str__(self): 
        s ='Número de DNI: {:^10} Nombre del profesional: {:<20}Importe de venta: {:<10}Tipo de afiliación: {:<10} Tipo de trabajo: {:<10}'
        s = s.format(str(self.numero_DNI) , self.nombr_profesional, str(self.importe_x_mes), str(self.tipo_afiliación), str(self.tipo_trabajo))
        return s

def menu():
    cad = '\n\nMenu de Opciones\n' \
          '=======================================\n' \
          '1 --- Cargar un vector con los tipos de profesionales\n' \
          '2 --- Mostar los profesionales cargados\n' \
          '3 --- Buscar un profesional por DNI\n' \
          '4 --- Crear un archivo de registros\n' \
          '5 --- Mostrar el archivo \n' \
          '6 --- Buscar un registro \n' \
          '7 --- Generar matriz de acumulacion\n' \
          '0 --- Salir\n' \
          'Ingrese su opcion: \n'
    return int(input(cad))

# 1 - Primero registro 
# 2 - Menu 
# 3 - Cargar el registro (Carga automatica) 
# 4 - Mostrar el registro 
# 5 - Las opciones