class Instructiuni():
    lista_instr = {}


    def nume_cheie(self,nume,instr):
        self.lista_instr[nume] = str(instr)

    # def appendInstructiune(self,instr):
    #     self.lista_instr.append(instr)

    def checkedInstructiuni(self, instr):
        if instr in self.lista_instr:
            return False
        return True

    # def afisare_lista(self):
    #     vec = self.lista_instr.keys()
    #     print(vec)

    def get_val_cheie(self,nume):
        return self.lista_instr[str(nume)]
