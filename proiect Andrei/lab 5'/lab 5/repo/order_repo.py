from data_repo import Data_repo
import pickle
from models.drink import Drink
from models.gekochterGericht import GekochterGericht

class Order_repo(Data_repo):

    def __init__(self):
        self.file='Orders.data'
        self.orders=[]

    def add_to_order(self, neue_speise):
        self.orders.append(neue_speise)
        f = open(self.file, 'ab')
        pickle.dump(self.orders, f)
        f.close()

    def calculate_total_cost(self,gericht:GekochterGericht, getrank:Drink):
        return gericht.price+getrank.price


