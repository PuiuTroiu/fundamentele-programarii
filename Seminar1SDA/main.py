from Bag import Bag
from Iterator import Iterator

def main():
    bag = Bag()
    it = Iterator(bag)
    # bag.beg = [1,2,"Informatica", [1,2,3], 12.3,1,1]

    bag.add(1)
    bag.add(2)
    bag.add("Informatica")
    bag.add([1,2,3])
    bag.add(12.3)
    bag.add(1)
    bag.add(1)
    bag.afisare()

    assert bag.size() == 7
    assert bag.search([1,2,3]) == True
    assert bag.nrOcurrences(1) == 3

    print(it.getCurrent())
    print(it.first())
    print(it.next())
    print(it.ValueIndex(4))


main()