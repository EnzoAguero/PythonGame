from principal import *
from configuracion import *
import random



def lectura(archivo, salida):
    for word in archivo:
        salida.append(word.rstrip('\n'))
def nuevaPalabra(lista):
    word= random.choice(lista)
    return word

def silabasTOpalabra(silaba):
    silaba= silaba.replace(' ','-')
    return silaba

def palabraTOsilaba(palabra):
    palabra = separador(palabra)
    return palabra

def esCorrecta(palabraEnSilabasEnPantalla, palabra):
    if (palabraEnSilabasEnPantalla== silabasTOpalabra(palabra)):
        return True

def puntaje(palabra):
    if len(palabra) < 10:
        return 5
    return 10

