class Pelicula:
    def __init__(self, num_id, titulo, importe, tipo_pelicula, num_pais_origen):
        self.num_id = num_id
        self.titulo = titulo
        self.importe = importe
        self.tipo_pelicula = tipo_pelicula
        self.num_pais_origen = num_pais_origen

    #def __str__(self): 
       #s = ''
       #s =  ' Num_ID ' + str(self.numero_identificacion)    
       #s += ' Nomb_medic ' + str(self.nomb_medicamento)
       #s += ' Precio_venta ' + str(self.precio_venta)
       #s += ' Tipo_medicamento ' + str(self.tipo_medicamento)
       #s += ' Tipo_present ' + str(self.tipo_present)
       #return s  


    def __str__(self): 
        s ='Número ID: {:^10} Título:{:<20} Importe:{:<10} Tipo de película:{:<10} País de origen:{:<10}'
        s = s.format(str(self.num_id) , self.titulo, str(self.importe), str(self.tipo_pelicula), str(self.num_pais_origen))
        return s