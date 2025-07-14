class Video:
    def __init__(self, duracion): ## se fija solo las variables a trabajar
        self._ancho = 1 ##se fija
        self._alto = 1 ##se fija
        self.duracion = duracion  ## se modificará solo con el setter 

    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, nueva_duracion):
        if nueva_duracion > 0:
            self._duracion = nueva_duracion
        else:
            self._duracion = 5

    def comprimir_anuncio (self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio (self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")
        