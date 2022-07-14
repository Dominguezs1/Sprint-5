
class BuilderCliente:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def getDatosClienteClassic():
        return {
            "limite_extraccion_diario": 10000,
            "limite_extraccion_mensual": 50000,
            "limite_extraccion_anual": 100000,
        }

    @staticmethod
    def getDatosClienteBlack():
        return {
            "limite_extraccion_diario": 20000,
            "limite_extraccion_mensual": 500000,
            "limite_extraccion_anual": 1000000,
        }
    
    @staticmethod
    def getDatosClienteGold():
        return {
            "limite_extraccion_diario": 30000,
            "limite_extraccion_mensual": 2000000,
            "limite_extraccion_anual": 5000000,
        }
