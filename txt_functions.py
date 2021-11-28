import pickle
import os

def cargar_datos_txt(archivo, datos):
    '''
    Carga datos a un archivo externo
    Recibe: Nombre del archivo y datos a cargar
    Devuelve: Void
    '''
    escritura_binaria = open(archivo, 'wb')
    datos = pickle.dump(datos, escritura_binaria)
    escritura_binaria.close()

def recibir_datos_txt(archivo, datos):
    '''
    Extrae datos de un archivo externo
    Recibe: Nombre del archivo y lista donde recibimos los datos
    Devuelve: lista con los datos extraídos del archivo externo
    '''
    lectura_binaria = open(archivo, 'rb')
    if os.stat(archivo).st_size != 0:

        datos = pickle.load(lectura_binaria)
    lectura_binaria.close()
    return datos
