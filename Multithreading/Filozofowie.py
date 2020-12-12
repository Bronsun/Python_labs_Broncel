import threading
import random
import time

Deadlock = False


class Philosopher(threading.Thread):
    def __init__(self,name,Left,Right):
        threading.Thread.__init__(self)
        self.name = name
        self.Left = Left
        self.Right = Right

    def run(self):
        while True:
            print('{0} myśli '.format(self.name))
            time.sleep(random.uniform(3,13))
            print('{0} jest głodny '.format(self.name) )
            self.getForks()
    def getForks(self):
        fork_1,fork_2 = self.Left,self.Right

        while True:
            fork_1.acquire(True)
            locked = fork_2.acquire(False)
            if locked:
                break
            if Deadlock is False:
                fork_1.release()
                print('{0} zmienia swoje zaintersowanie '.format(self.name))
                fork_1,fork_2 = fork_2,fork_1
            else:
                print('{0} czeka na widelec '.format(self.name))

            self.eating()
            fork_2.release()
            fork_1.release()

    def eating(self):
        print('{0} zaczyna jeść '.format(self.name))
        time.sleep(random.uniform(1,10))
        print('{0} kończy jedzenie i idzie myśleć dalej '.format(self.name))


def diner():
    forks = [threading.Lock() for n in range(5)]
    names = ('Mati', 'Karol', 'Kacper', 'Michał', 'Zuza')
    philosophers = [Philosopher(names[i], forks[i % 5], forks[(i + 1) % 5]) for i in range(5)]

    random.seed(345662)
    for p in philosophers:
        p.start()



diner()