import time
import random
from threading import Thread,Lock

locker = Lock()
class First:
    def __init__(self,value = 0):

        self.value = value
    
    def get_value(self):

        return self.value

    def set_value(self,value):

        self.value = value


class Second:
    def __init__(self,value = 0):
        self.value = value
    
    def get_value(self):

        return self.value

    def set_value(self,value):

        self.value = value


def target(F,S,K,locker,):
        locker.acquire()
        print('Start thread')
        first_num=0
        second_num=0
        for i in range(K):
            N1=random.random()
            N2=random.random()
            new_num1=first_num+F.get_value()
            new_num2=second_num+S.get_value()
            F.set_value(new_num1)
            S.set_value(new_num2)
        
        locker.release()


if __name__ == '__main__':
    start_time = time.perf_counter()
    F = First()
    S = Second()
    N = random.randint(10,20)
    K1 = random.randint(10000,20000)
    K2 = random.randint(10000,20000)
    threads = []
    for i in range(N):

        if i < N/2:

            thread = Thread(target =target,args = (F,S,K1,locker) )

        elif i >= N/2:

            thread = Thread(target = target,args = (F,S,K2,locker))

        thread.start()
        threads.append(thread)
    
    for t in threads:
        t.join()
    end_time = time.perf_counter()

    print(f'Execution time: {end_time- start_time: 0.2f}')

