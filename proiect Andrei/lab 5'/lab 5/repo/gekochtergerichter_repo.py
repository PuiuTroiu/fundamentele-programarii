from data_repo import Data_repo
from models.gekochterGericht import GekochterGericht
import pickle
class Gekochtergerichter_repo(Data_repo):
    def __init__(self):
        self.file='Food.data'
        self.gekochtergerichte=[]

    def add(self, neues_gericht):
        self.gekochtergerichte.append(neues_gericht)
        self.save()

    def delete_food(self,food:GekochterGericht):
        food_list = []
        with open(self.file, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    food_list.append(obj)
                except EOFError:
                    break

        for c in food_list:
            for k in c:
                if k.id == food:
                    food_list.remove(k)
        f = open(self.file, 'wb')
        for k in food_list:
            pickle.dump(k, f)
        f.close()
    def load(self):
        with open(self.file, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    self.gekochtergerichte.append(obj)
                except EOFError:
                    break
        return self.gekochtergerichte

    def find_dish(self, selected_dish):
        gerichte = self.load()
        for dishes in gerichte:
            found_dish = list(filter(lambda d: selected_dish.lower() in d.name.lower(), dishes))
            if found_dish:
                return found_dish