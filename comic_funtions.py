from Comic import *
from txt_functions import *
import os
from Serialaux import*

def new_comic(comics):
    """
    Registra usuarios nuevos en la base de datos
    Recibe: Lista de usuarios
    Devuelve: Lista de usuarios con nuevo usuario registrado
    """
    os.system('clear')
    title = input('Título: ')
    while (len(title) >40):
        print('El título debe contener menos de 40 caracteres')
        title = input('Título: ')

    serial = input('Serial: ')
    while not (len(serial) == 8) or (not serial.isnumeric()):
        print('Ingreso inválido') 
        serial = input('Serial: ')

    price = input('Precio de venta: ')
    while (not price.isnumeric()) or int(price) > 999 :
        print('Ingreso inválido')
        price = input('Precio de venta: ')

    stock = input('Stock disponible: ')
    while (not stock.isnumeric()) or int(stock) > 99 :
        print('Ingreso inválido')
        price = input('Stock disponible: ')

    new_comic = Comic(int(serial), title, int(price), int(stock))
    comics.append(new_comic)
    os.system('clear')
    print('Se ha añadido el siguiente cómic a la base de datos:')
    new_comic.show_attributes()
    print('')

    return comics

def list_seriales(comics):
    seriales = []
    for i, comic in enumerate(comics):
        new_serial = Serialaux(comic.serial, i)
        seriales.append(new_serial)
    
    return seriales