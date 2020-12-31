import os, re
import threading
import time

def thread_job(i):
    global sum
    sum += i

m = list(map(int,'4 5 6 3 4 5 3 4 3 2 3 4 5 3 4 5 2 1 2 3 4 5 3 2 3 4 4 3 2 2 2 2 2 2 2 2 2 22 1 12 3 4 2 2435 5 2345 4325 32 452 345 326 4326 246 346 34 64 632 53 425 345 324 543 5 325 32 453 245 345 34 5 2345 32 45 3245 342 5342 5 3425 234 25 2345 324 5 3245 2'.split()))
n = len(m)
print("Длина массива =", n)
sum = 0
start = time.time()
threads = [threading.Thread(target=thread_job(m[i])) for i in range(n)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("Сумма =", sum)

finish = time.time()
timen = finish - start
print("время1 = ", timen)


m = list(map(int,'1 2 3 4 5 6 7 8 9 1 2 3 4 2 3 4 5 34 4 3243 23 4 234 2  66 2435 342 532 45 3245 324 5234 532 45 3245 3245 34 5234 5324 5342 53 425 4325 324 5324 523 453245 324 5 3425 3425 342 5342 5432 532 45 342'.split()))
n = len(m)
print("Длина массива =", n)
sum = 0
start = time.time()
threads = [threading.Thread(target=thread_job(m[i])) for i in range(n)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("Сумма =", sum)

finish = time.time()
timen = finish - start
print("время2 = ", timen)


m = list(map(int,'324 3 4 324 234 23 423 42 34 234 23 42 34 324 23 423 42 34 23 324 324 32 4 324 3 4 324 32 4 234 23 432 4 324 23 423 4 234 3 24 432 324 324 32 42 34 234 32 432 42 34 2435 324 52 435 324 532 45 324 5 3245 234 532 45 324 5 4325 234 52 345 23 45 234 523 45 432 5 3245 324 5 432 5 4325 32 45 345 342 5 3245 324 5324 5 3425 24 35 2345 234 543 52 345 3245 3245 2345 3245'.split()))
n = len(m)
print("Длина массива =", n)
sum = 0
start = time.time()
threads = [threading.Thread(target=thread_job(m[i])) for i in range(n)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("сумма =", sum)

finish = time.time()
timen = finish - start
print("время3 = ", timen)
# 1 2 3 4 5 6 7 8 9 1 2 3 4 2 3 4 5 34 4 3243 23 4 234 2  66 2435 342 532 45 3245 324 5234 532 45 3245 3245 34 5234 5324 5342 53 425 4325 324 5324 523 453245 324 5 3425 3425 342 5342 5432 532 45 342
# 4 5 6 3 4 5 3 4 3 2 3 4 5 3 4 5 2 1 2 3 4 5 3 2 3 4 4 3 2 2 2 2 2 2 2 2 2 22 1 12 3 4 2 2435 5 2345 4325 32 452 345 326 4326 246 346 34 64 632 53 425 345 324 543 5 325 32 453 245 345 34 5 2345 32 45 3245 342 5342 5 3425 234 25 2345 324 5 3245 2
# 324 3 4 324 234 23 423 42 34 234 23 42 34 324 23 423 42 34 23 324 324 32 4 324 3 4 324 32 4 234 23 432 4 324 23 423 4 234 3 24 432 324 324 32 42 34 234 32 432 42 34 2435 324 52 435 324 532 45 324 5 3245 234 532 45 324 5 4325 234 52 345 23 45 234 523 45 432 5 3245 324 5 432 5 4325 32 45 345 342 5 3245 324 5324 5 3425 24 35 2345 234 543 52 345 3245 3245 2345 3245