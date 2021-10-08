class Servicios:
    def __init__(self, num_id, nomb_titular, tipo_cliente, tipo_producto, monto_mensual):
        self.num_id = num_id
        self.nomb_titular = nomb_titular
        self.tipo_cliente = tipo_cliente
        self.tipo_producto = tipo_producto
        self.monto_mensual = monto_mensual

    # def __str__(self):
    # s = ''
    # s =  ' Num_ID ' + str(self.numero_identificacion)
    # s += ' Nomb_medic ' + str(self.nomb_medicamento)
    # s += ' Precio_venta ' + str(self.precio_venta)
    # s += ' Tipo_medicamento ' + str(self.tipo_medicamento)
    # s += ' Tipo_present ' + str(self.tipo_present)
    # return s

    def __str__(self):
        s = 'Número ID: {:^10} Nombre del titular: {:<20} Tipo de cliente: {:<10}Tipo de producto: {:<10} Monto mensual: {:<10}'
        s = s.format(str(self.num_id), self.nomb_titular, str(self.tipo_cliente), str(self.tipo_producto),
                     str(self.monto_mensual))
        return s
