from Comic import *

def busqueda_binaria_serial(lista, x):
    #busqueda binaria para el serial 
    #devuelve la posicion en la que se encuentra el serial o -1 si no existe
    #se puede acceder al serial como seriales[x]

    arr = sorted(lista, key=lambda lista: lista.serial)
    for a in arr:
        print(f'{a.index}: {a.serial}')
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
    print(index)
    if(index==-1):
        print('El serial que ingresó no coincide con ningún comic')
        return
    comic_index = seriales[index].index

    comic = comics[comic_index]
    return comic
