class Product(object):
    def __init__(self,name):
        self.__name = name

    def __str__(self):
        return self.__name

class Inventory(object):
    def __init__(self):
        self.__items = []

    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print("new item added")
        else:
            raise ValueError("Invalid Item")

    def get_number_of_items(self):
        return len(self.__items)

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self,items):
        self.__items = items

my_inventory = Inventory()
my_inventory.add_new_item(Product('tv'))
my_inventory.add_new_item(Product('radio'))
print(my_inventory.get_number_of_items())

items = my_inventory.items
items.append(Product('audio'))
print(my_inventory.get_number_of_items())

items.append(Product('computer'))
my_inventory.items = items
print(my_inventory.get_number_of_items())

for product in my_inventory.items:
    print(product)