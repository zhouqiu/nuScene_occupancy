import multiprocessing
import time
import random
keys = ["q", "w", "e"]

def mini_fun(i,key):
    A[key] = i * 2


def fun(idx):
    global A
    A = {}
    print("process {}: A = {}".format(idx, A))

    mini_fun(idx,keys[idx])
    time.sleep(random.randint(1,10))
    print("process {}: A = {}".format(idx, A))



for i in range(3):

    m = multiprocessing.Process(target=fun, args=(i, ))
    m.start()