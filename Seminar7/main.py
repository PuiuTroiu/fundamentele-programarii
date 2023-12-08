from frac import Frac
from die import Die
from statistics import Statistics
from auto import Auto
from cont import Cont
from tests import test_plata
def main():
    # d = Die(6)
    # roll = d.roll()
    # while roll != 6:
    #     print(f"rolled: {roll}")
    #     roll = d.roll()

    # f1 = Frac(1,2)
    # f1.extend(10)
    # f1.reduce()
    # print(f"{f1.numitor}/{f1.numarator}")

    # s = Statistics()
    #
    # autos = [Auto('m1', 'm2', 1000, 'red'),
    #          Auto('m1', 'm2', 1000, 'blue'),
    #          Auto('m1', 'm2', 1000, 'red')]
    #
    # color = 'red'
    #
    # print(f'#red autos= {s.count_colors(autos,color)}')
    #
    # print(f'avg year = {s.avg_year(autos, "m1")}')

    newAccount = Cont(100)

    newAccount.plata(10)
    newAccount.depundere(20)
    test_plata()
    print(newAccount.amount)

    k1 = Cont(100)
    k2 = Cont()

    print(k2.amount)


main()