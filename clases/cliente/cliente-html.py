CLASSIC = "CLASSIC"
BLACK = "BLACK"
GOLD = "GOLD"

class Cliente:

    def __init__(self, **kwargs) -> None:
        self.cuneta = Cuenta(**kwargs)

    def inicializar(self, datos):
        self.numero = datos["numero"]
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]
        self.direccion = Direccion(**datos["direccion"])


class GrabadoHtmL:

    def crearHtml(self):
        return """ 
        <div class="cliente">
            <div class="numero">{}</div>
            <div class="nombre">{}</div>
            <div class="direccion">{}</div>
        </div>
        """.format(self.numero, self.nombre, self.apellido, self.direccion.crearHtml())

    def grabarHtml():
        archivo = open("index.html", "w")
        archivo.write(self.crearHtml())
        archivo.close()