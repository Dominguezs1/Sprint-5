
from .transaccion_class import procesar_transaccion

class Cliente:

    def __init__(self, datos) -> None:

        self.numero = datos["numero"]
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]
        self.dni = datos["dni"]
        self.tipo = datos["tipo"]

        if self.tipo == 'CLASSIC':

            self.limite_extraccion_diario = 10000
            self.limite_transferencia_recibida = 150000,
            self.costo_transferencia = 0.01
            self.total_tarjetas_credito = 0
            self.total_chequeras = 0
            self.cuenta_dolares = 0
            self.saldo_descubierto_disponible = 0

        elif self.tipo == 'GOLD':       
            self.limite_extraccion_diario = 20000
            self.limite_transferencia_recibida = 500000,
            self.costo_transferencia = 0.005
            self.total_tarjetas_credito = 1
            self.total_chequeras = 1
            self.cuenta_dolares = 0
            self.saldo_descubierto_disponible = 10000
            
        elif self.tipo == 'BLACK':       
            self.limite_extraccion_diario = 100000
            self.limite_transferencia_recibida = 9999999999999999
            self.costo_transferencia = 0
            self.total_tarjetas_credito = 5
            self.total_chequeras = 2
            self.cuenta_dolares = 1
            self.saldo_descubierto_disponible = 10000
        
        self.procesados = []
        for evento in datos["transacciones"]:
            self.procesados.append( procesar_transaccion(evento, self) )


        
