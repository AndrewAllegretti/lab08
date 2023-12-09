class Car:
    def __init__(self, make, model, year, price):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price

    def __gt__(self, other):

        if self.make > other.make:
            return True
        if self.make == other.make:
            if self.model > other.model:
                return True
        if self.make == other.make and self.model == other.model:
            if self.year > other.year:
                return True
        if self.make == other.make and self.model == other.model and self.year == other.year:
            if self.price > other.price:
                return True
        return False


    def __lt__(self, other):
        if self.make < other.make:
            return True
        if self.make == other.make:
            if self.model < other.model:
                return True
        if self.make == other.make and self.model == other.model:
            if self.year < other.year:
                return True
        if self.make == other.make and self.model == other.model and self.year == other.year:
            if self.price < other.price:
                return True
        return False

    def __eq__(self, other):
        return self.make == other.make and self.model == other.model and self.year == other.year and self.price == other.price

    def __str__(self):
        return "Make: {}, Model: {}, Year: {}, Price: ${}".format(self.make, self.model, self.year, self.price)
    
