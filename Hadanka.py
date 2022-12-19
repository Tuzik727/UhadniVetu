import re

from interfaces import Hadanka


class MaHadanka(Hadanka):

    def __init__(self, veta: str):
        if not re.match("^[a-zA-Z ]+$", veta):
            raise Exception("veta smi obsahovat jen mala pismena anglicke abecedy a mezery")
        self.veta = veta
        self.slovo = veta.split(' ')
        self.index = 0

    def nacti_slovnik(self):
        with open("words.txt") as file_in:
            words = []
            for line in file_in:
                words.append(line.strip().lower())
            return words

    def pocet_slov(self):
        return len(self.slovo)

    def hadej_slovo(self):
        return self.slovo

    def hadej_vetu(self, veta: str):
        return self.veta
