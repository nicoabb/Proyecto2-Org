
class Comic:
    def __init__(self, serial, title, price, stock):
        self.serial = serial
        self.title = title
        self.price = price
        self.stock = stock
        self.deleted = False

    def show_attributes(self):
        if self.deleted == False:
            print(
                f'Serial: {self.serial} Título: {self.title} Precio: {self.price}$ Cantidad disponible: {self.stock}')
        else:
            print('Este comic no se encuentra en la base de datos')

    def add_stock(self, add):
        if((self.stock+add) < 100):
            self.stock = self.stock + add
            print(f'Se han agregado {add} unidades al stock')
        else:
            print('Se ha superado la cantidad máxima de comics en el stock')

    def buy(self, quantity):
        if((self.stock-quantity) < 0):
            print(
                f'Lastimosamente no disponemos de esa cantidad de cómics, el stock disponible es de {self.stock}')

        else:
            print(f'El total de su compra es de {self.price*quantity}$')
            cont = input(
                '¿Está seguro que desea continuar con su compra?\n [1] si [2] no\n>>')
            while (cont != '1' and cont != '2'):
                print('Ingreso inválido')
                cont = input(
                    '¿Está seguro que desea continuar con su compra?\n [1] si [2] no\n>>')

            if cont == '1':
                self.stock = self.stock - quantity
                print(
                    f'Su compra de {quantity} unidades del comic {self.title} ha sido exitosa')
            else:
                print('Compra cancelada')

    def delete(self):

        cont = input(f'¿Está seguro que desea eliminar {self.title}?\n [1] si [2] no\n>>')
        while (cont != '1' and cont != '2'):
            print('Ingreso inválido')
            cont = input(f'¿Está seguro que desea eliminar {self.title}?\n [1] si [2] no\n>>')

        if cont == '1':
            self.deleted = True
            print(f'El cómic {self.title} ha sido eliminado')
        else:
            print('Operación cancelada')
