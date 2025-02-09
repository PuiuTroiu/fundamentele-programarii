from data_repo import Data_repo
from models.drink import Drink
import pickle

class Drink_repo(Data_repo):
    def __init__(self):
        self.file='Drinks.data'
        self.drinks=[]

    def add_drink(self,drink):
        self.drinks.append(drink)
        self.save()

    def read_drinks_list(self):
        f = open(self.file, 'rb')
        while True:
            try:
                x = pickle.load(f)
                self.drinks.append(x)
            except EOFError:
                break
        f.close()
        return self.drinks

    def delete_drink(self,drink:Drink):
        drinks_list = []
        with open(self.file, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    drinks_list.append(obj)
                except EOFError:
                    break

        for c in drinks_list:
            for k in c:
                if k.id == drink:
                    drinks_list.remove(k)
        f = open(self.file, 'wb')
        for k in drinks_list:
            pickle.dump(k, f)
        f.close()

    def find_drink(self, selected_drink):
        getranke = self.read_drinks_list()
        for drinks in getranke:
            found_drink = list(filter(lambda d: selected_drink.lower() in d.name.lower(),drinks))
            if found_drink:
                return found_drink



