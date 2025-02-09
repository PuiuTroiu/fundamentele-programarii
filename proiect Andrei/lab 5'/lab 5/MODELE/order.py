from identifiable import Identifiable
from court import Court
from drink import Drink
import functools

# class Order(Identifiable):
#     def __init__(self,id,gesamtkosten):
#         super().__init__(id)
#         self.dishes=[]
#         self.drinks=[]
#         self.gesamtkosten=gesamtkosten
#
#     def add_food(self,food:Court):
#         self.dishes.append(food)
#
#     def delete_food(self,food:Court):
#         self.dishes.pop(food)
#
#     def add_drink(self,drink:Drink):
#         self.drinks.append(drink)
#
#     def delete_drink(self,drink:Drink):
#         self.drinks.pop(drink)
#
#     def cost_of_order(self):
#         costs=[]
#         for i,j in self.dishes,self.drinks:
#             a=getattr(i,'price')
#             b=getattr(j,'price')
#             costs.append(a)
#             costs.append(b)
#         self.gesamtkosten=functools.reduce(lambda x,y:x+y,costs)
#         return self.gesamtkosten[0]
#
#     def bill_gen(self):
#         #ar trebui ceva cu map dar nu inteleg ce ar trebui sa fac cu map la metoda asta
#         bill_list=[]
#         for i in self.dishes:
#             bill_list.append(self.dishes[i])
#         for j in self.drinks:
#             bill_list.append(self.drinks[j])
#         return bill_list
#
#     def bill_print(self,bill_list=list):
#         print('----------BILL----------')
#         for i in bill_list:
#             a=getattr(bill_list[i],'name')
#             b=getattr((bill_list[i],'price'))
#             print(f'{a}..........{b}')
#         print(f'TOTAL: {self.gesamtkosten[0]}')
#
# billprint=Order(123,0)
# salad=Court(350,100)
# billprint.add_food(salad)
# billprint.bill_print()

class Order(Identifiable):
    def __init__(self, id: int, kunden_id: int, gerichts_id: list, getränk_id: list):
        Identifiable.__init__(self, id)
        self.kunden_id = kunden_id
        self.gerichts_id = gerichts_id
        self.getränk_id = getränk_id
        self.gesamtkosten = 0

    def calculate_total_cost(self, gerichte, getränke):
        gericht_kosten = [gericht.price for gericht in gerichte if gericht.id in self.gerichts_id_liste]
        getränk_kosten = [getränk.price for getränk in getränke if getränk.id in self.getränk_id_liste]
        self.gesamtkosten = sum(gericht_kosten) + sum(getränk_kosten)

    def generate_bill(self, gerichte, getränke, kunden):
        customer_name = ""
        customer_address = ""

        for customer in kunden:
            if customer.id == self.kunden_id:
                customer_name = self.kunde.name
                customer_address = self.kunde.address
                break

        ordered_dishes = [gericht for gericht in gerichte if gericht.id in self.gerichts_id_liste]
        ordered_drinks = [getränk for getränk in getränke if getränk.id in self.getränk_id_liste]

        rechnung = f'===== Rechnung =====\nKunde: {customer_name}\nAdresse: {customer_address}\nBestellte Gerichte: \n'
        for gericht in ordered_dishes:
            rechnung += f"{gericht.id}: {gericht.portionsgröße} - {gericht.preis}\n"
        rechnung += "\nBestellte Getränke:\n"
        for getränk in ordered_drinks:
            rechnung += f"{getränk.id}: {getränk.portionsgröße} - {getränk.preis}\n"
        rechnung += f'\nGesamtkosten:{self.gesamtkosten}\n'
        return rechnung


