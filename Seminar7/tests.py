from statistics import Statistics
from auto import Auto
from cont import Cont

def test_count_color():
    s = Statistics()
    autos = [Auto('m1','m2',1000,'red'),
             Auto('m1','m2',1000,'blue'),
             Auto('m1','m2',1000,'red')]
    color = 'red'
    assert s.count_colors(autos) == 2

def test_plata():
    cont = Cont(100)

    cont.plata(10)
    assert cont.amount == 90

    cont.depundere(10)
    assert cont.amount == 100
