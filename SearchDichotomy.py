import time
from tabulate import tabulate
import matplotlib.pyplot as plt

aList=[]
iter =0
results = []

def search(a ,b, key):
    global iter

    iter = iter+1
    mid = int((a+b)/2)
    #print("Searching midpoint at ", str( aList[mid]) )
    if mid == 0:
        print("Key Not Found!" )
        return key
    elif key == aList[mid]:
        print("Key Found! at position : " + str(mid) )
        return aList[mid]
    elif key > aList[mid]:
        print( a, b )
        a=mid+1
        search( a, b, key )
    else:
        print( a, b )
        b = mid -1
        search( a, b, key )
    
# a=0
# b=24_000_000
# k=0
# aList = list(range(a, b))
# st = time.process_time()
# search( a, b, k)

# et = time.process_time()
# print("Temps = " , et-st)
# print( "iter = ", iter )
a = 0
b = 1000000
while b <= 10000000: 
    iter =0
    k=0
    st = time.process_time()
    aList = list(range(a, b))
    search(a,b,k)
    et = time.process_time()
    results.append({'n': b,'time':et-st, 'iter':iter })
    b+= 1000000

print(tabulate(results, headers={'n':'Pour n', 'time':'time', 'iter':'iterations'}))

plt.plot([x['n'] for x in results],[x['time'] for x in results])
plt.xticks([x['n'] for x in results])
plt.show()