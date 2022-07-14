import json
from typing import Tuple
from .cliente import Cliente

class Parser:

    def leerDatos(self, filename:str):
        transacciones = []
        with open(filename) as jsonFile:
            eventos = json.load(jsonFile)
            cliente = self.parserClientes(eventos)
            for e in eventos["transacciones"]:
                transacciones.append(e)


        return(cliente, transacciones)

    def parserClientes(self, datos) -> Clientes:
        tipo = datos["tipo"]

        if (tipo =="CLASSIC"):
            cliente = ClienteClassic()
        elif (tipo =="GOLD"):
            cliente = ClienteGold()
        elif (tipo =="BLACK"):
            cliente = ClienteBlack()

        return cliente