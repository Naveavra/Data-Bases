

class hat:
    def __init__(self, id, topping, supplier, quantity):
        self.id = id
        self.topping = topping
        self.supplier = supplier
        self.quantity = quantity

class supplier:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class order:
    def __init__(self, id, loaction, hat):
        self.id = id
        self.location = loaction
        self.hat = hat
