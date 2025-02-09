import pickle

from data_repo import Data_repo


class Customer_repo(Data_repo):
    def __init__(self):
        self.file='Customers.data'
        self.customers=[]

    def add_customer(self,customer:Cust):
        self.customers.append(customer)
        self.save()

    def read_customer_list(self):
        f=open(self.file,'rb')
        while True:
            try:
                x=pickle.load(f)
                self.customers.append(x)
            except EOFError:
                break
        f.close()
        return self.customers

    def update_customer(self,new_id,new_name,new_address,customer_to_update:):
        lista=[]
        with open(self.file, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    lista.append(obj)
                except EOFError:
                    break

        if customer_to_update in lista:
            new_customer=(new_id,new_name,new_address)
            index=lista.index(customer_to_update)
            lista[index]=new_customer

        f = open(self.file, 'wb')
        for i in lista:
            pickle.dump(i, f)
        f.close()

    def delete_customer(self,customer:):
        kunden = []
        with open(self.file, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    kunden.append(obj)
                except EOFError:
                    break

        for c in kunden:
            for k in c:
                if k == customer:
                    kunden.remove(k)
        f = open(self.file, 'wb')
        for k in kunden:
            pickle.dump(k, f)
        f.close()

    def find_customer(self,customer:):
        x=0
        f=open(self.file,'rb')
        for line in self.file:
            for el in line:
                if el==customer:
                    x=customer
        f.close()
        return x
