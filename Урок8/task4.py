class Sklad:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year
        self.printers_ = {}

    def __str__(self):
        return f'Добавляем на склад:---> \n Модель:{self.name}\n сделано в:{self.make}\n Год выпуска:{self.year}\n'

    def add_tech(self, subj):
        self.printers_.append(subj)


class Printer(Sklad):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)
        self.printer_dict = []

    def to_take(self, subj):
        self.printers_.append(subj)