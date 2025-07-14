
from error import SubTipoInvalidoException

class Anuncio:
    SUB_TIPOS = () #cada subclase lo abordará

    def __init__(self, alto, ancho, url_archivo, url_clic, sub_tipo):
        self._alto=alto 
        self._ancho=ancho 
        self._url_archivo=url_archivo
        self._url_clic=url_clic
        self.sub_tipo = sub_tipo ##se aplica setter con validación


    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, nuevo_ancho):
        if nuevo_ancho > 0:
            self._ancho = nuevo_ancho
        else:
            self._ancho = 1 
    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, nuevo_alto):
        if nuevo_alto > 0:
            self._alto = nuevo_alto
        else:
            self._alto = 1

    @property
    def url_archivo(self):
        return self._url_archivo
    
    @url_archivo.setter
    def url_archivo(self, nuevo_url_archivo):
        self._url_archivo = nuevo_url_archivo

    @property
    def url_clic(self):
        return self._clic
    
    @url_clic.setter
    def url_clic(self, nuevo_url_clic):
        self._url_clic = nuevo_url_clic

    @property
    def sub_tipo(self):
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, nuevo_subtipo):
        if nuevo_subtipo in self.SUB_TIPOS:
            self._sub_tipo = nuevo_subtipo
        else:
            raise SubTipoInvalidoException(
                f"'{nuevo_subtipo}' no es un subtipo válido para {type(self).__name__}. "
                f"Subtipos permitidos: {self.SUB_TIPOS}"
            )

    @staticmethod
    def mostrar_formatos():
        print("FORMATOS DISPONIBLES:")
        for cls in Anuncio.__subclasses__():
            print(f"\nFORMATO: {cls.__name__}")
            print("=" * 20)
            for subtipo in cls.SUB_TIPOS:
                print(f"- {subtipo}")

### Video ###

class Video(Anuncio):

    SUB_TIPOS = ("instream", "outstream") ##3 se incluyen estas categorias para darle coherencia al código

    def __init__(self, duracion, url_archivo, url_clic, sub_tipo): ## se fija solo las variables a trabajar
        super().__init__(alto=1, ancho=1, url_archivo=url_archivo, url_clic=url_clic, sub_tipo=sub_tipo)
        self.duracion = duracion

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

### Subclase: Display ###

class Display(Anuncio):
    SUB_TIPOS = ("banner", "sidebar", "popup") ## solo coherencia 

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

### Social ###

class Social(Anuncio):
    SUB_TIPOS = ("facebook", "instagram", "tiktok") ##igual que códigos anteriores coom coherencia

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")