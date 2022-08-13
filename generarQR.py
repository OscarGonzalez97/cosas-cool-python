import pyqrcode
import png

def genera_qr():
    # solicitamos nombre de nuestro archivo
    nombre_archivo = input('Ingrese el nombre de su QR: ')

    # solicitamos link o texto
    link = input('Ingrese link o texto de QR: ')

    # creamos el QR
    qr_code = pyqrcode.create(link)

    # Guardamos el archivo de la imagen
    qr_code.png(f'QRs/{nombre_archivo}.png', scale=5)
