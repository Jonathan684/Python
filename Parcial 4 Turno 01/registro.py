
class Medicamentos:
    def __init__(self, num_ident,nomb_medicamento,precio_venta, tipo_medicamento, tipo_present):
        self.numero_identificacion = num_ident
        self.nomb_medicamento = nomb_medicamento
        self.precio_venta = precio_venta
        self.tipo_medicamento = tipo_medicamento
        self.tipo_present = tipo_present

    #def __str__(self): 
       #s = ''
       #s =  ' Num_ID ' + str(self.numero_identificacion)    
       #s += ' Nomb_medic ' + str(self.nomb_medicamento)
       #s += ' Precio_venta ' + str(self.precio_venta)
       #s += ' Tipo_medicamento ' + str(self.tipo_medicamento)
       #s += ' Tipo_present ' + str(self.tipo_present)
       #return s  


    def __str__(self): 
        s ='Número ID: {:^10} Nombre del medicamento:{:<20}Precio de venta:{:<10}Tipo de medicamento:{:<10} Tipo de presentación:{:<10}'
        s = s.format(str(self.numero_identificacion) , self.nomb_medicamento, str(self.precio_venta), str(self.tipo_medicamento), str(self.tipo_present))
        ##print(f"{bcolors.OK}"+datos+"{bcolors.RESET}")
        return s