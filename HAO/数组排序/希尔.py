import numpy as np
t = np.random.randint(1,10,10)
lens = len(t)
print(t)
#####希尔排序
def insertionSort(l):
    for i in range(1, len(l)):
        j=i-1
        tmp=l[i]
        while j>=0 and l[j]>tmp:
            l[j+1] = l[j]
            l[j] = tmp
            j-=1
    return l


gap = lens//2
while gap>0:
    for i in range(gap):
        insertionSort(t[i::gap])
        print(gap,t)
    gap//=2

print(t)