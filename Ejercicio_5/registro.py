class Trabajos():
    def __init__(self, num_ident,nombre_trabajo,tipo_trabajo, importe, cant_pers):
        self.numero_identificion = num_ident
        self.descrip_trabajo = nombre_trabajo
        self.tipo_de_trabajo = tipo_trabajo
        self.importe_trab = importe
        self.personal = cant_pers
    
    def __str__(self): 
       s = ''
       s =  ' Num_ID ' + str(self.numero_identificion)       
       s += ' Desc ' + self.descrip_trabajo 
       s += ' Tipo_trab ' + self.tipo_de_trabajo
       s += ' Importe ' + str(self.importe_trab) 
       s += ' Personal ' + str(self.personal)
       return s  
