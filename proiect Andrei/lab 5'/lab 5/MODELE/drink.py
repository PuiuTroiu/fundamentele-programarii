from court import Court

class Drink(Court):
    def __init__(self,id,portion,price,alcoholcontent):
        super().__init__(id,portion,price)
        self.alcoholcontent=alcoholcontent
