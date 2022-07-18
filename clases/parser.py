
import json
from .modelos.cliente_class import Cliente

class Parser:

    def leerDatos(self, filename:str):
        with open(filename) as jsonFile:
            entrada = json.load(jsonFile)
            cliente = Cliente(entrada)
        return( cliente )
