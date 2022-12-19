import multiprocessing
import time

from Hadanka import MaHadanka
from Hra import MaHra

if __name__ == '__main__':
    start = time.time()
    pocet_procesu = multiprocessing.cpu_count()
    manager = multiprocessing.Manager()
    guessed = manager.list()

    print("Napiste vetu \n")
    veta = input().lower()

    hadanka = MaHadanka(veta)
    hra = MaHra()
    hadanka.nacti_slovnik()
    slova = hadanka.hadej_slovo()

    pool = []
    if len(slova) < pocet_procesu:
        p2 = multiprocessing.Process(target=hra.hraj, args=(hadanka, slova, guessed,))
        pool.append(p2)

    else:
        for i in range(0, pocet_procesu):
            p1 = multiprocessing.Process(target=hra.hraj, args=(hadanka, slova[i::pocet_procesu], guessed,))
            pool.append(p1)

    for i in pool:
        i.start()
    for j in pool:
        j.join()
    print("Uhodnuto:", guessed)