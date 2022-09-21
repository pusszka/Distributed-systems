from threading import Thread
import time
def task1(lenght):

    for i in range(lenght):
        print(1)
        time.sleep(1)

def task2(lenght):
     for i in range(lenght):
        print(2)
        time.sleep(1)


def task3(lenght):
     for i in range(lenght):
        print(3)
        time.sleep(1)

start_time = time.perf_counter()

thr1 = Thread(target = task1,args=(5,))
thr2 = Thread(target = task2,args=(10,))
thr3 = Thread(target = task3,args=(5,))

thr1.start()
thr2.start()
thr3.start()

thr1.join()
thr2.join()
thr3.join()

end_time = time.perf_counter()

print(f'Execution time: {end_time- start_time: 0.2f}')