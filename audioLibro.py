import PyPDF2
import pyttsx3


def audio_libro():
    # Leemos el pdf especificando el path en la computadora
    pdfReader = PyPDF2.PdfFileReader(open('resume.pdf', 'rb'))

    # dejamos que el speaker maneje todo
    speaker = pyttsx3.init()

    # spliteamos las paginas y leemos una a una
    for page_num in range(pdfReader.numPages):
        text = pdfReader.getPage(page_num).extractText()
        speaker.say(text)
        speaker.runAndWait()

    # paramos el speaker

    speaker.stop()

    # guardamos el audiolibro en un path
    engine = pyttsx3.init()
    engine.save_to_file(text, 'resumen.mp3')
    engine.runAndWait()
