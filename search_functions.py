from Comic import *


def busqueda_binaria_serial(lista, x):
    # busqueda binaria para el serial
    # devuelve la posicion en la que se encuentra el serial o -1 si no existe
    # se puede acceder al serial como seriales[x]

    arr = sorted(lista, key=lambda lista: lista.serial)
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if arr[mid].serial < x:
            low = mid + 1

        elif arr[mid].serial > x:
            high = mid - 1

        else:
            return mid

    return -1


def buscar_por_serial(serial, comics, seriales):
    index = busqueda_binaria_serial(seriales, serial)
    if(index == -1):
        print('El serial que ingresó no coincide con ningún comic')
        return
    comic_index = seriales[index].index

    comic = comics[comic_index]
    return comic


def busqueda_binaria_title(lista, x):
    # busqueda binaria para el serial
    # devuelve la posicion en la que se encuentra el serial o -1 si no existe
    # se puede acceder al serial como seriales[x]

    # Arr relaciona de manera random los indices con los titulos para hacer el arbol
    arr = sorted(lista, key=lambda lista: lista.title)
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2
        # Va chequeando si el titulo del indice actual es el que se esta buscando
        if arr[mid].title < x:
            low = mid + 1

        elif arr[mid].title > x:
            high = mid - 1

        else:
            return arr[mid].index

    return -1


def buscar_por_titulo(title, comics, titles, all_titles):
    """[summary]

    Args:
        title ([String]): [Valor ingresado por el usuario]
        comics ([List]): [Lista de objetos de tipo comic. Capaz no hace falta.]
        titles ([List]): [Lista de objetos de tipo Titleaux]
        all_titles ([List]): [Lista con todas las palabras que conforman los títulos (incluye repeticiones)]

    Returns:
    Dependiendo de la cantidad de repeticiones esta función retornara:
        [comic]: [El comic al que hace referencia la palabra ingresada por el usuario]
        [comics_list]: [Una lista con los comics a los que hace referencia la palabra ingresada por el usuario]
    """
    contador = all_titles.count(title)

    # Si el contador es mayor que uno quiere decir que la palabra se repite.
    # Por ejemplo, si es Batman y Batman sale en mas de un titulo, entonces el contador va a ser mayor que 1
    if contador > 1:
        counter = 0
        comics_lists = []
        while counter < contador:
            index = busqueda_binaria_title(titles, title)
            comic = comics[index]
            comics_lists.append(comic)
            titles = pop(titles, title, index)
            counter += 1
        return comics_lists

        # Hacer la busqueda mas de una vez, quitando, cada vez, el anterior que encontro para no repetir
        # Retorna una lista de comics
    else:
        # Hace la busqueda normal
        index = busqueda_binaria_title(titles, title)

    if(index == -1):
        print('El título que ingresó no coincide con ningún comic')
        return

    comic = comics[index]
    return comic


def pop(titles, title, index):
    aux = []
    contador = 0
    for v, w in enumerate(titles):
        if w.index == index:
            if aux == []:
                aux.append(v)
            else:
                contador += 1
                aux.append(v-contador)

    for i in aux:
        titles.pop(i)
    return titles
