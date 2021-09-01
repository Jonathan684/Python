class Trabajos():
    def __init__(self, num_ident, desc_trab, importe, cant_pers):
        self.numero_identificion = num_ident
        self.descrip_trabajo = desc_trab
        self.importe_trab = importe
        self.personal = cant_pers
    
    def __str__(self): 
       s = ''
       s = s + 'Num_ID ' + str(self.numero_identificion) + ' Desc ' + self.descrip_trabajo + ' importe ' + str(self.importe_trab) + ' personal ' + str(self.personal)
       return s  
