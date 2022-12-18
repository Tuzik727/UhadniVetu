import multiprocessing

from Hra import guessed
from Hadanka import MaHadanka
from Hra import MaHra

if __name__ == "__main__":
    while True:
        pool = []
        process_count = multiprocessing.cpu_count()

        print("Napiste vetu \n")
        veta = input()

        hadanka = MaHadanka(veta)
        hra = MaHra()

        for process in range(process_count):
            p = multiprocessing.Process(target=hra.hraj, args=(hadanka,))
            pool.append(p)

        for p in pool:
            p.start()

        for p in pool:
            p.join(timeout=0)

        print("uhadnuto")
        print('The lists are:', '\n'.join([str(guessed) for guessed in guessed]), sep='\n')
