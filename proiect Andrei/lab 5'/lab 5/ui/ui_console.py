from repo.customer_repo import Customer_repo
from models.customer import Customer
from repo.gekochtergerichter_repo import Gekochtergerichter_repo
from models.gekochterGericht import GekochterGericht
from models.drink import Drink
from repo.drink_repo import Drink_repo
from models.order import Order
class Console:
    def __init__(self,gericht:GekochterGericht,drink:Drink,customer:Customer):
        self.gericht=gericht
        self.drink=drink
        self.customer=customer
        #self.order=order


    def menu(self):
        return """
        Choose option:
        1-customer
        2-menu options
        3-order
        4-exit
        """

    def customermenu(self): #opt1
        return"""
        Customer menu:
        1-add customer
        2-del customer
        3-view customers
        4-update a customer
        5-find a customer
        6-exit
        """

    def menuoptions(self): #opt2
        return"""
        menu options:
        1-food
        2-drink
        3-exit
        """

    def ordermenu(self): #opt3
        return"""
        Order menu:
        1-add to order
        2-calculate total
        3-generate bill
        4-exit
        """
    def foodmenu(self):
        return"""
        Food menu:
        1-add dish
        2-view avalibale dishes
        3-delete drink
        4-find dish
        5-exit
        """
    def drinkmenu(self):
        return """
        1-add drink
        2-view avalibale drinks
        3-delete drink
        4-find drink
        5-exit
        """

    def run(self):
        while True:
            print(self.menu())
            opt=int(input('Option:'))

            if opt==1:
                while True:
                    print(self.customermenu())
                    opt1=int(input('Option:'))
                    if opt1==1:
                        # id1=int(input('Customer id: '))
                        # nume1=str(input('Customer name: '))
                        # address1=str(input('Customer address: '))
                        # customer=Customer(id1,nume1,address1)
                        customerrepo=Customer_repo()
                        customerrepo.add_customer(self.customer)
                        print('Customer added')
                        break
                    if opt1==2:
                        # id2=int(input('Id of Customer to delete: '))
                        # name2=str(input('Name of Customer to delete: '))
                        # address2=str(input('Address of the customer to delete'))
                        # customer2=Customer(id2,name2,address2)
                        customerrepo1=Customer_repo()
                        customerrepo1.delete_customer(self.customer)
                        print('Customer deleted')
                        break
                    if opt1==3:
                        customerrepo3=Customer_repo()
                        print('Customers: ',customerrepo3.read_customer_list())
                        break
                    if opt1==4:
                        # id4=int(input('Old name: '))
                        # name4=str(input('Old name: '))
                        # address4=str(input('Old address: '))
                        # customer4=Customer(id4,name4,address4)
                        new_id=int(input('new id: '))
                        new_name=str(input('new name: '))
                        new_address=str(input('new address: '))
                        customerrepo4=Customer_repo()
                        customerrepo4.update_customer(new_id,new_name,new_address,self.customer)
                        print('Customer updated')
                        break
                    if opt1==5:
                        customerrepo5=Customer_repo()
                        print(customerrepo5.find_customer(self.customer))
                        break

                    if opt1==6:
                        break



            if opt==2:
                while True:
                    print(self.menuoptions())
                    opt2=int(input('Option:'))
                    if opt2==1:
                        while True:
                            print(self.foodmenu())
                            opt4=int(input('Option:'))
                            if opt4==1:#add
                                # id1=int(input('add food id:'))
                                # price1=int(input('add food price: '))
                                # portion1=int(input('add food portion: '))
                                # preptime1=int(input('add food preptime: '))
                                # food=GekochterGericht(id1,portion1,price1,preptime1)
                                gekochtergerichtrepo=Gekochtergerichter_repo()
                                gekochtergerichtrepo.add(self.gericht)
                                print('Food added')
                                break
                            if opt4==2:#delete
                                # id4 = int(input('add food id:'))
                                # price4 = int(input('add food price: '))
                                # portion4 = int(input('add food portion: '))
                                # preptime4 = int(input('add food preptime: '))
                                # food4 = GekochterGericht(id4, portion4, price4, preptime4)
                                gekochtergerichtrepo4=Gekochtergerichter_repo()
                                gekochtergerichtrepo4.delete_food(self.gericht)
                                print('food deleted')
                                break
                            if opt4==3:#view
                                foodrepo2=Gekochtergerichter_repo()
                                print(foodrepo2.load())
                                break

                            if opt4==4:#find
                                # id3 = int(input('add food id: '))
                                # price3 = int(input('add food price: '))
                                # portion3 = int('add food portion: ')
                                # preptime3 = int('add food preptime: ')
                                # food3=GekochterGericht(id3,portion3,price3,preptime3)
                                foodrepo3=Gekochtergerichter_repo()
                                print(foodrepo3.find_dish(self.gericht))
                                break
                            if opt4==5:
                                break
                    if opt2==2:
                        while True:
                            print(self.drinkmenu())
                            opt5=int(input('Option:'))
                            if opt5==1:
                                # id1=int(input('add drink id: '))
                                # price1=int(input('add drink price: '))
                                # portion1=int(input('add drink portion: '))
                                # alccontent1=int(input('add drink alcoholcontent: '))
                                # drink1=Drink(id1,portion1,price1,alccontent1)
                                drinkrepo1=Drink_repo()
                                drinkrepo1.add_drink(self.drink)
                                print('Drink added')
                                break
                            if opt5==2:
                                drinkrepo4=Drink_repo()
                                print(drinkrepo4.read_drinks_list())
                                break
                            if opt5==3:
                                # id3 = int(input('add drink id: '))
                                # price3 = int(input('add drink price: '))
                                # portion3 = int(input('add drink portion: '))
                                # alccontent3 = int(input('add drink alcoholcontent: '))
                                # drink3 = Drink(id3, portion3, price3, alccontent3)
                                drinkrepo3=Drink_repo()
                                drinkrepo3.delete_drink(self.drink)
                                print('Drink deleted')
                                break

                            if opt5==4:
                                # id2 = int(input('add drink id: '))
                                # price2 = int(input('add drink price: '))
                                # portion2 = int(input('add drink portion: '))
                                # alccontent2 = int(input('add drink alcoholcontent: '))
                                # drink2 = Drink(id2, portion2, price2, alccontent2)
                                drinkrepo2=Drink_repo()
                                print(drinkrepo2.find_drink(self.drink))
                                break
                            if opt5==5:
                                break
                    if opt2==3:
                        break

            if opt==3:
                while True:
                    print(self.ordermenu())
                    opt3=int(input('Option:'))
                    if opt3==1:
                        pass
                    if opt3==2:
                        pass
                    if opt3==3:
                        pass
                    if opt3==4:
                        break

            if opt==4:
                break

