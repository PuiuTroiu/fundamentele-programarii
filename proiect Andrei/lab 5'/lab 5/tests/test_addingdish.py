from models.gekochterGericht import GekochterGericht
from repo.gekochtergerichter_repo import Gekochtergerichter_repo

def test_addingfood():
    food1=GekochterGericht('fish',300,70,20)
    food2=GekochterGericht('chips',320,60,20)
    food3=GekochterGericht('beans',200,50,10)
    gekochtergericht_repo=Gekochtergerichter_repo()
    gekochtergericht_repo.add_gekochtergericht(food1)
    gekochtergericht_repo.add_gekochtergericht(food2)
    gekochtergericht_repo.add_gekochtergericht(food3)
    print(gekochtergericht_repo.find_gekochteergerichtname('beans'))

test_addingfood()
