from court import Court

class GekochterGericht(Court):
    def __init__(self,id,portion,price,preptime):
        super().__init__(id,portion,price)
        self.preptime=preptime


