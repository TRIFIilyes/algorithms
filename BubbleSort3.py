import time
from tabulate import tabulate 
import matplotlib.pyplot as plt

results = []

def BubbleSort(a,b):
    data = list(range( a, b ))
    k = 0
    n=len(data)
    st = time.process_time()

    for i in range(n-1):
        swapped = False
        for j in range(0 , n-i-1 ):
            k=k+1
            # print("ok"+str(k))
            if data[  j  ] >  data[  j+1 ]:
                swapped = True
                data[ j ], data[ j+1 ] =  data[ j+1 ], data[ j ]
    et = time.process_time()
    print('Done for b= '+str(b))
    results.append({'n': n,'time': et-st, 'iter':k})
    #if not swapped:
    #    break

a = 0
b = 1000

while b <= 10000:
    BubbleSort(a,b)
    b += 1000


print(tabulate(results, headers={'n':'Pour N', 'time': 'Time', 'iter':'iterations'}))


plt.plot([x['n'] for x in results],[x['time'] for x in results])
plt.xticks([x['n'] for x in results])
plt.show()