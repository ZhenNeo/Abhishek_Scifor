import csv

class Item():
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        # run validations of price and quantity
        assert price >= 0, f"price {price} should be greator than or equal to 0"
        assert quantity >= 0, f"quantity {quantity} should be greator than or equal to 0"

        # assign attributed to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def display_discount(self):
        self.price = self.price * self.pay_rate
 
    @classmethod
    def instantiate_from_csv(cls):
        with open('Scifor/shop.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


class Phone(Item):
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):
        # call t osuper function to have access to all attributes / methods of Item
        super().__init__(
            name, price, quantity
        )
        
        # run validations of price and quantity
        assert broken_phones >= 0, f"Broken Phones {broken_phones} should be greator than or equal to 0"

        # assign to self object
        self.broken_phones = broken_phones


phone1 = Phone("javaPhonev20", 700, 10, 1)
print(Item.all)



