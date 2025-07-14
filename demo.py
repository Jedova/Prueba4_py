from campaña import Campaña
from error import SubTipoInvalidoException, LargoExcedidoException

# Datos iniciales de prueba: campaña con 1 anuncio tipo Video
anuncios_data = [
    {
        "tipo": "Video",
        "duracion": 13,
        "url_archivo": "video1.mp4",
        "url_clic": "https://clic.cl",
        "sub_tipo": "instream"
    }
]

campaña = Campaña("Campaña Demo", anuncios_data)

##Mostrar campaña original##
print(campaña)

##Solicitar cambios al usuario##

nuevo_nombre = input("Ingrese nuevo nombre para la campaña: ")
nuevo_subtipo = input("Ingrese nuevo sub_tipo para el anuncio (Video): ")

try:
    campaña.nombre = nuevo_nombre
    campaña.anuncios[0].sub_tipo = nuevo_subtipo

except (LargoExcedidoException, SubTipoInvalidoException) as e:
    print(f"Ocurrió un error: {e}")
    with open("error.log", "a", encoding="utf-8") as f:
        f.write(str(e) + "\n")

else:
    print("\nActualización exitosa.")
    print(campaña)
