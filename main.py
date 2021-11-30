from txt_functions import *
from Comic import *
from comic_functions import *
from search_functions import *
from Titleaux import *
import os


def main():

    comics = []  # lista donde se van a almacenar los comics
    try:
        comics = recibir_datos_txt('lista_comics.txt', comics)
        # lista donde se van a almacenar los seriales con su respectivo índice (estructura auxiliar)
        seriales = list_seriales(comics)
        # lista donde se van a almacenar los títulos con su respectivo índice (estructura auxiliar)
        titles = list_titles(comics)
        all_titles = list_all_titles(comics)
    except:
        print('El archivo lista_comics.txt no existe')

    os.system('clear')

    while True:
        opcion = input(
            'Bienvenido! Seleccione una de las siguienes opciones:\n[1] Registrar un nuevo cómic\n[2] Buscar un cómic\n[3] Comprar un cómic\n[4] Reabastecer inventario\n[5] Eliminar un cómic\n[6] Salir\n>>')
        while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "6":
            opcion = input(
                'Ingreso inválido\nDebe Ingresar el número de la opción que desea realizar\n>> ')

        # Registro por serial, título, precio de venta, stock actual
        if opcion == '1':
            # se agrega un nuevo objeto comic a la lista
            comics = new_comic(comics)
            # agregar comic nuevo a estructura auxiliar de seriales y títulos
            seriales = list_seriales(comics)
            titles = list_titles(comics)
            cargar_datos_txt('lista_comics.txt', comics)
            all_titles = list_all_titles(comics)

        # Búsqueda de historieta por serial o consulta de palabras
        elif opcion == '2':
            os.system('clear')
            # Dejo esto escrito aca para que lo vean, pero como lo vamos a usar varias veces, deberiamos convertirlo en una función que retorne el objeto de comic buscado
            option_two = input(
                '[1] Buscar por serial \n[2] Buscar por título\n[3] Salir\n>>')
            while (option_two != '1' and option_two != '2' and option_two != '3'):
                print('Ingreso inválido')
                option_two = input(
                    '[1] Buscar por serial \n[2] Buscar por título\n[3] Salir\n>>')
            if option_two == '1':
                s = input('Ingrese el serial del comic que desea buscar: ')
                while not (len(s) == 8) or (not s.isnumeric()):
                    print('Ingreso inválido')
                    s = input('Ingrese el serial del comic que desea buscar: ')

                os.system('clear')
                comic = buscar_por_serial(int(s), comics, seriales)
                #cuando convirtamos en funcion, aqui va return comic
                comic.show_attributes()
                print('')
            elif option_two == '2':
                t = input('Ingrese el título del comic que desea buscar: ')
                while not (len(t) <= 40):
                    print('Ingreso inválido')
                    t = input('Ingrese el título del comic que desea buscar: ')
                os.system('clear')

                # cuando convirtamos en funcion, aqui va return comic
                comics_encontradas = buscar_por_titulo(
                    t, comics, titles, all_titles)
                if comics_encontradas != None:
                    contador = all_titles.count(t)
                    if contador > 1:
                        for i in comics_encontradas:
                            i.show_attributes()
                        titles = list_titles(comics)
                    else:
                        comics_encontradas.show_attributes()
                print('')

        # Comprar (siempre y cuando haya suficiente stock)
        elif opcion == '3':
            # copiar el codigo de la busqueda y luego usar el método comic.buy(cantidad)
            pass

        # Reabastecimiento
        elif opcion == '4':
            # copiar el codigo de la busqueda y luego usar el método comic.addstock(cantidad)
            pass

        # Eliminación
        elif opcion == '5':
            # copiar el codigo de la busqueda y luego usar el método comic.delete()
            pass
            # Falta agregar el compactador, que borra de la lista todo lo que está eliminado lógicamente

        # Salir
        elif opcion == '6':
            os.system('clear')
            break


main()
