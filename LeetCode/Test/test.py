n=4#int()
a=[2,1,3,4]#[int(i) for i in input().split()]

b=sorted(a)
c=[a[i] for i in range(n) if a[i]!=b[i]]
d=[b[i] for i in range(n) if a[i]!=b[i]]
c = c[::-1]
if len(c)>0 and c==d:
    print("yes")
else:
    print("no")


t = list('qwererty')
print(t)