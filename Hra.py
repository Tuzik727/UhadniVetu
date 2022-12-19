import multiprocessing
import random

from Hadanka import MaHadanka
from interfaces import Hra


class MaHra(Hra):

    def hraj(self, hadanka: MaHadanka, veta: list, guessed: list):
        lock = multiprocessing.Lock()
        with lock:
            for i in hadanka.nacti_slovnik():
                for j in veta:
                    if i == j:
                        print("Hadam: " + i)
                        guessed.append(i)
                        if len(guessed) == len(veta):
                            break

