from ui.ui_console import Console
from models.customer import Customer
from models.drink import Drink
from models.gekochterGericht import GekochterGericht


def main():
    customer=Customer(1,'vasile','str. alb nr. 1')
    drink=Drink(2,100,200,50)
    food=GekochterGericht(3,250,50,30)

    console=Console(food,drink,customer)
    console.run()

main()