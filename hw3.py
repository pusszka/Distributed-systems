import time
import random
import queue
import threading
import concurrent.futures


lock = threading.RLock()

def colatz(q):
    lock.acquire()
    try:
        
        digit = q.queue[0]
        print(list(q.queue))

        if digit != 1:

            if digit % 2 == 0:

                digit /=2

            else:

                digit = 3*digit+1

            q.put(digit)
            q.get()

        else:

            q.get()

    finally:

        lock.release()

        if q.empty() != True:

            colatz(q)
    

if __name__ == '__main__':
    start_time = time.perf_counter()
    q = queue.Queue()
    N = random.randint(2,30)
    for i in range(1,N):
        q.put(i)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(colatz,q)
        future.result()

    end_time = time.perf_counter()

    print(f'Execution time: {end_time- start_time: 0.6f}')
    