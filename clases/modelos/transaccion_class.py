
def procesar_transaccion(evento, instancia_cliente):
    fecha= evento["fecha"]
    tipo= evento["tipo"]
    estado= evento["estado"]
    monto= evento["monto"]
    razon= ""

    if evento["estado"]=="RECHAZADA":
        if evento["tipo"]=="RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
            if evento["monto"] > evento["cupoDiarioRestante"]:
                razon= "Excede el limite diario de extraccion"
            elif evento["monto"] > evento["saldoEnCuenta"]:
                razon= "Fondos insuficientes"
        
        if evento["tipo"]=="ALTA_TARJETA_CREDITO":
            if evento["totalTarjetasDeCreditoActualmente"] >= instancia_cliente.total_tarjetas_credito:
                razon= "Excede la cantidad de tarjetas permitidas"

        if evento["tipo"]=="ALTA_CHEQUERA":
            if evento["totalChequerasActualmente"] >= instancia_cliente.total_chequeras:
                razon= "Excede la cantidad de chequeras permitidas"

        if evento["tipo"]=="COMPRA_DOLAR":
            if instancia_cliente.cuenta_dolares == 0:
                razon= "No puede operar con dolares"
            elif evento["monto"] > evento["saldoEnCuenta"]:
                razon= "Fondos insuficientes"
        
        if evento["tipo"]=="TRANSFERENCIA_ENVIADA":
            if evento["monto"] > evento["saldoEnCuenta"]:
                razon= "Fondos insuficientes"
        
        if evento["tipo"]=="TRANSFERENCIA_RECIBIDA":
            if evento["monto"] > instancia_cliente.limite_transferencia_recibida:
                razon= "Monto mayor al permitido sin previo aviso"

    return {
            "fecha":fecha, 
            "tipo":tipo, 
            "estado":estado, 
            "monto":monto, 
            "razon": razon
            }

