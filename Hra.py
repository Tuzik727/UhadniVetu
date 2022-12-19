import multiprocessing

from english_words import english_words_set as ews
from Hadanka import MaHadanka
from interfaces import Hra


class MaHra(Hra):

    def hraj(self, hadanka: MaHadanka, slova: list, guessed):
        slova = hadanka.hadej_slovo()
        lock = multiprocessing.Lock()

        while True:
            for i in ews:
                for j in range(len(slova)):
                    if i == slova[j]:
                        if guessed.__contains__(i):
                            break
                        guessed.append(i)
                        if len(i) > 8:
                            raise Exception("Prekrocili jste maximalni velikost slova(10)")
                        print("Hadam: " + slova[j])
                        if len(guessed) == len(slova):
                            print("Uhodnuto: ")
                            for a in guessed:
                                print(a + " ")
            break
    def opacko(self,hadanka: MaHadanka):
        slovnik = {}
        for i in hadanka.hadej_slovo():
            pass