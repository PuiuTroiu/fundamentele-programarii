class Iterator:
    def __init__(self,beg):
        self.val_iterator = 0
        self.beg = beg

    def ValueIndex(self,index):
        if self.valid(index):
            return self.beg.beg[index]
        else:
            raise IndexError("Index out of range")
    def next(self,*args):
        if self.val_iterator+1 < len(self.beg.beg):
            self.val_iterator += 1
            return self.beg.beg[self.val_iterator]

    def first(self):
        return self.beg.beg[0]

    def valid(self,index):
        if index >= 0 and index < len(self.beg.beg):
            return True
        raise IndexError("Index out of range")

    def getCurrent(self):
        if self.valid(self.val_iterator):
            return self.beg.beg[self.val_iterator]



