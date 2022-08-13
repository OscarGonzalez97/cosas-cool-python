import pytube


def descargar_video():
    # Pedimos url del video
    url = input('Ingrese la url del video: ')
    # especificamos la carpeta para guardar
    path = 'videosYoutube'

    # linea magica para descargar el video
    pytube.YouTube(url).streams.get_highest_resolution().download(path)
