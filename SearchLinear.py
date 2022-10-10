import time
from tabulate import tabulate
import matplotlib.pyplot as plt
aList = []
iter = 0
results = []

def search(key):
    global iter
    for i in range(len(aList)):
        iter = iter + 1
        if aList[i] == key:
            return i

    return -1


# a = 0
# b = 10000000
# k = 10000000

# aList = list(range(a, b))
# st = time.process_time()
# print(search(k))
# et = time.process_time()

# print("Pour N = ", len(aList))
# print("temps = ", et-st)
# print("iter = ", iter)
a = 0
b = 1000000
while b <= 10000000: 
    iter =0
    k=b
    aList = list(range(a, b))
    st = time.process_time()
    search(k)
    et = time.process_time()
    results.append({'n': b,'time':et-st, 'iter':iter })
    b+= 1000000

print(tabulate(results, headers={'n':'Pour n', 'tima':'time', 'iter':'iterations'}))
plt.plot([x['n'] for x in results],[x['time'] for x in results])
plt.xticks([x['n'] for x in results])
plt.show()