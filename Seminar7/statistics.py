class Statistics:
    def count_colors(self,autos,color):
        cnt = 0
        for auto in autos:
            if auto.color == color:
                cnt += 1
        return cnt

    def avg_year(self,autos,make):
        sum = 0
        cnt = 0

        for auto in autos:
            if auto.make == make:
                cnt += 1
                sum += auto.year

        return sum/cnt