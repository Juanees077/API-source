from spyne import Application, ServiceBase, Integer, Float
from spyne.decorator import rpc
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class ServicioTriangulo(ServiceBase):
    @rpc(Float, Float, _returns=Float)
    def calcular_area(ctx, base, altura):
        return (base * altura) / 2

aplicacion = Application([ServicioTriangulo], 'spyne.ejemplos.triangulo.soap',
                         in_protocol=Soap11(validator='lxml'),
                         out_protocol=Soap11())

aplicacion_wsgi = WsgiApplication(aplicacion)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    servidor = make_server('127.0.0.1', 8000, aplicacion_wsgi)
    print("Escuchando en http://127.0.0.1:8000")
    servidor.serve_forever()
