a = [3,2,7,3,1,0]
b = [1,4,7,3,2,1]
c =[a,b]
print(c)

def f(a,b=[]):
    b+=[a]
    print(b)

f(1)
f(2,[])
f(3)