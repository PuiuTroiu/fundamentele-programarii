class Raum:
    def __init__(self,no,seats):
        self.no = no
        self.seats = seats

    def __str__(self):
        # return f'Raum(no = {self.no}, seats = {self.seats})'
        return f'{self.no},{self.seats}'

    def __eq__(self, other):
        return self.no == other.no


class Lab(Raum):
    def __init__(self,no,seats,os):
        Raum.__init__(self,no,seats)

        if os not in ['Unix', 'Linux', 'Windows']:
            raise AttributeError("os not allowed...")

        self.os = os

    def __str__(self):
        # return f'Lab(no = {self.no}, seats = {self.seats}, os = {self.os})'
        return f'{self.no},{self.seats},{self.os})'


class Building:
    def __init__(self, rooms):
        self.rooms = rooms

    def seats(self):
        for room in self.rooms:
            print(room.seats)

    def write_data(self):
        f = open('data.out','w')
        for room in self.rooms:
            f.write(str(room) + '\n')
        # for room in self.rooms:
        #     if type(room) == Lab:
        #         f.write(f'{room.no}, {room.seats}, {room.os}\n')
        #     else:
        #         f.write(f'{room.no}, {room.seats}\n')

        f.close()

    def read_data(self):
        f = open('data.txt','r')

        for line in f:
            attrs = line.strip().split(',')
            if len(attrs) == 2:
                self.room.append(Raum(attrs[0],attrs[1]))
            else:
                self.room.append(Raum(attrs[0],attrs[1],attrs[2]))

        f.close()
def main():
    r1 = Raum('21A', 100)
    r2 = Raum('21B',100)

    # print(r1)
    # print(r1 == r2)

    l1 = Lab('01A',20,'Windows')

    b = Building([r1,r2,l1])
    b.seats()

    b.write_data()

    print(l1)
main()
