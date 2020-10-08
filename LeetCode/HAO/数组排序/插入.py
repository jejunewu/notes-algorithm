import numpy as np
t = np.random.randint(1,10,10)
lens = len(t)
print(t)
#####插入排序

for i in range(1,lens):
    j=i-1
    tmp = t[i]
    while j>=0 and t[j]>tmp:
        t[j+1] = t[j]
        t[j] = tmp
        j-=1

print(t)