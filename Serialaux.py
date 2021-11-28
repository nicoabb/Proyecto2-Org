class Serialaux:
    def __init__(self, serial, index):
        self.serial = serial
        self.index = index

    def show_attributes(self):
        print(f'Serial: {self.serial} Index: {self.index}')
