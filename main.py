import multiprocessing

from Hadanka import MaHadanka
from Hra import MaHra

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    guessed = manager.list()

    print("Napiste vetu \n")
    veta = input()

    hadanka = MaHadanka(veta)
    hra = MaHra()

    pool = []

    for i in range(0, 4):
        p1 = multiprocessing.Process(target=hra.hraj, args=(hadanka, veta,guessed,))
        pool.append(p1)

    for i in pool:
        i.start()
    for j in pool:
        j.join()
