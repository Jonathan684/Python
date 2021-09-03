class Servicio():
    def __init__(self,num_id, nomb_pac, tipo_pract, cant_dias_trat, cant_medic):
        self.numero_identif = num_id
        self.nombre_paciente = nomb_pac
        self.tipo_practicas = tipo_pract
        self.cantidad_días = cant_dias_trat
        self.cantidad_medicam = cant_medic
    
    #def __str__(self): 
       #s = ''
       #s = ' Numero ID:   ' + str(self.numero_identif)
       #s += ' Nombre del paciente:   ' + self.nombre_paciente
       #s += ' Tipo de practicas:  ' + str(self.tipo_practicas)
       #s += ' Cantidad días de tratamiento:  ' + str(self.cantidad_días)
       #s += ' Cantidad de medicamentos entregados/ aplicados:   ' + str(self.cantidad_medicam)
       
       #return s

    #def __str__(self): ---> CON FORMAT
        #r = ''
        #r += '{:<15}'.format('Número ID: ' + str(self.numero_identif))
        #r += '{:<15}'.format('Nombre del paciente:  ' + self.nombre_paciente
        #r += '{:<18}'.format('Tipo de practicas:  ' + str(self.tipo_practicas)
        #r += '{:<18}'.format('Cantidad días de tratamiento:  ' + str(self.cantidad_días)
        #r += '{:<15}'.format('Cantidad de medicamentos entregados/ aplicados:   ' + str(self.cantidad_medicam)

    def __str__(self): 
        s ='Número ID: {:^10} Nombre del paciente:{:<20}Tipo de practicas:{:<10}Cantidad días de tratamiento:{:<10} Cantidad de medicamentos entregados/ aplicados:{:<10}'
        s = s.format(str(self.numero_identif) , self.nombre_paciente, str(self.tipo_practicas), str(self.cantidad_días), str(self.cantidad_medicam))
        ##print(f"{bcolors.OK}"+datos+"{bcolors.RESET}")
        return s
