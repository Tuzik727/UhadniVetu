import re

from interfaces import Hadanka


class MaHadanka(Hadanka):

    def __init__(self, veta: str):
        if not re.match("^[a-zA-Z?><;,{}_.+=!@#$%&*|']*$", veta):
            raise Exception("veta nesmi obsahovat neco mimo anglickych charakteru")
        self.veta = veta
        self.slovo = veta.split(' ')
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.slovo):
            raise StopIteration
        result = self.slovo[self.index]
        self.index += 1
        return result

    def pocet_slov(self):
        return len(self.slovo)

    def hadej_slovo(self, slovo: str):
        return self.slovo

    def hadej_vetu(self, veta: str):
        return self.veta == veta

