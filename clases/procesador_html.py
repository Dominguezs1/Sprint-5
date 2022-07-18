
style = """
                <style>
                    table, td, th {
                        border: 1px solid #ddd;
                        text-align: left;
                    }
                    table {
                        border-collapse: collapse;
                        width: 100%;
                    }
                    th, td {
                        padding: 15px;
                    }
                </style>
"""

def crear_html(cliente):
    transacciones = ""
    espaciado = '               '
    for e in cliente.procesados:
        transacciones += espaciado + "<tr><td>{fecha}</td><td>{tipo}</td><td>{estado}</td><td>{monto}</td><td>{razon}</td></tr> \n".format(
            fecha = e["fecha"],
            tipo = e["tipo"].replace("_", " "),
            estado = e["estado"],
            monto = e["monto"],
            razon = e["razon"]
        )

    html = """
<html>
    <head>
        <title>Transacciones del cliente</title> {style}
    </head>
    <body>
        <h1>{apellido}, {nombre}</h1>
        <h3>Numero cliente: {numero}</h3>
        <h3>DNI: {dni}</h3>
        <h3>Tipo: {tipo}</h3>
        <table>
            <tr><th>Fecha</th><th>Tipo</th><th>Estado</th><th>Monto</th><th>Razon</th></tr>
            {transacciones}
        </table>
    </body>
</html>
    """.format(
            style= style,
            numero= cliente.numero,
            nombre= cliente.nombre,
            apellido= cliente.apellido,
            dni= cliente.dni,
            tipo= cliente.tipo,
            transacciones= transacciones
            )

    archivo=open("index.html", "w")
    archivo.write(html)
    archivo.close()
