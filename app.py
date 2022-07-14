
from clases.parser import Parser

if __name__=="__main__":
    
    parser=Parser()
    cliente=parser.leerDatos('eventos.json')
    print(cliente)


