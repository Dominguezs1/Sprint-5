
from clases.parser import Parser
from clases.procesador_html import crear_html

if __name__=="__main__":
    
    parser=Parser()
    cliente=parser.leerDatos("eventos.json")
    html= crear_html(cliente)
    
    print("Cliente procesado: " + cliente.nombre + ", " + cliente.apellido)


