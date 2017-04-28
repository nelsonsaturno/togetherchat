from channels import route
from .consumers import message_handler


# Es posible redfinir los metodos de la libreria websocket
# para manejar conexion, recepcion y desconexion de un socket
channel_routing = [
    # route("websocket.connect", connect_handler),
    route("websocket.receive", message_handler),
    # route("websocket.diconnect", disconnect_handler)
]
