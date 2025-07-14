
class SubTipoInvalidoException(Exception):
    "Excepción lanzada cuando el subtipo de un anuncio no está dentro de los permitidos"
    pass

class LargoExcedidoException(Exception):
    "Excepción lanzada cuando el nombre de una campaña supera los 250 caracteres."
    pass
