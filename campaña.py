# campaña.py

from anuncio import Video, Display, Social
from error import LargoExcedidoException

class Campaña:
    def __init__(self, nombre, anuncios_data):
        self._anuncios = []  # composición de una lsita para anuncios
        self.nombre = nombre  # usa setter para validar
        self._fecha_inicio = None
        self._fecha_termino = None
        self.__crear_anuncios(anuncios_data)

    def __crear_anuncios(self, anuncios_data):
        """
        Crea objetos de tipo Video, Display o Social a partir de los datos entregados.
        Cada elemento de anuncios_data debe ser un diccionario con al menos:
        - tipo: "Video", "Display", "Social"
        - cuaquier otro dato requerido por el constructor
        """
        for anuncio in anuncios_data:
            tipo = anuncio.get("tipo")
            if tipo == "Video":
                self._anuncios.append(Video(
                    anuncio["duracion"],
                    anuncio["url_archivo"],
                    anuncio["url_clic"],
                    anuncio["sub_tipo"]
                ))
            elif tipo == "Display":
                self._anuncios.append(Display(
                    anuncio["alto"],
                    anuncio["ancho"],
                    anuncio["url_archivo"],
                    anuncio["url_clic"],
                    anuncio["sub_tipo"]
                ))
            elif tipo == "Social":
                self._anuncios.append(Social(
                    anuncio["alto"],
                    anuncio["ancho"],
                    anuncio["url_archivo"],
                    anuncio["url_clic"],
                    anuncio["sub_tipo"]
                ))

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 250:
            raise LargoExcedidoException("El nombre excede los 250 caracteres permitidos.")
        self._nombre = nuevo_nombre

    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, nueva_fecha):
        self._fecha_inicio = nueva_fecha

    @property
    def fecha_termino(self):
        return self._fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, nueva_fecha):
        self._fecha_termino = nueva_fecha

    @property
    def anuncios(self):
        return self._anuncios

    def __str__(self):
        tipos = {"Video": 0, "Display": 0, "Social": 0}
        for anuncio in self._anuncios:
            tipo_nombre = type(anuncio).__name__
            if tipo_nombre in tipos:
                tipos[tipo_nombre] += 1
        return (
            f"Nombre de la campaña: {self.nombre}\n"
            f"Anuncios: {tipos['Video']} Video, {tipos['Display']} Display, {tipos['Social']} Social"
        )

