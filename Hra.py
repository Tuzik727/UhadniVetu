import multiprocessing
import queue

from timeout_decorator import timeout
from english_words import english_words_set as ews
from Hadanka import MaHadanka
from interfaces import Hra

guessed = []


class MaHra(Hra):
    def hraj(self, hadanka: MaHadanka):

        lock = multiprocessing.Lock()

        with lock:
            global guessed
            isRun = True
            while isRun:
                for i in ews:
                    for j in hadanka.hadej_slovo(i):
                        if i == j:

                            if len(i) > 8:
                                raise Exception("Prekrocili jste maximalni velikost slova(10)")

                            guessed.append(i)

                            if len(guessed) == len(hadanka.hadej_slovo(i)):
                                print(i)
                                isRun = False
