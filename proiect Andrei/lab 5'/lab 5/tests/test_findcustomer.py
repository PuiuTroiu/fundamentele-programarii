from repo.customer_repo import Customer_repo
from models.customer import Customer

def test_customer():
    customer1=Customer('Vasile Pop','str. idk,nr. 9')
    customer2=Customer('Ioan Pop','str. 21 Decembrie,nr. 78')
    customer_repo=Customer_repo()
    customer_repo.add_customer(customer1)
    customer_repo.add_customer(customer2)
    print(customer_repo.find_customername('Vasile Pop'))

test_customer()
#??? nu merge pentru ca nu gaseste modulul data_repo??? nu inteleg