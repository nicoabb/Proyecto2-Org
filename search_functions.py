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

    # Revisar bien este arr
    arr = sorted(lista, key=lambda lista: lista.title)
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2
        print(f' mid: {mid}')

        print(f'La x: {x}')
        if arr[mid].title < x:
            low = mid + 1

        elif arr[mid].title > x:
            high = mid - 1

        else:
            return mid

    return -1


def buscar_por_titulo(title, comics, titles, all_titles):
    contador = all_titles.count(title)
    print(f'Contador: {contador}')

    # Si el contador es mayor que uno quiere decir que la palabra se repite.
    # Por ejemplo, si es Batman y Batman sale en mas de un titulo, entonces el contador va a ser mayor que 1
    if contador > 1:
        # Hacer la busqueda mas de una vez, quitando, cada vez, el anterior que encontro
    else:
        # Hace la busqueda normal
        index = busqueda_binaria_title(titles, title)

    if(index == -1):
        print('El título que ingresó no coincide con ningún comic')
        return
    comic_index = titles[index].index

    comic = comics[comic_index]
    return comic
