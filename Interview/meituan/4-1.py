n,m,a,b = 1,1,2,4
mw = [2]

if a > b:
    a,b = b,a

if m==0 and n-m >= 2:
    print('YES')
elif m==0 and n-m < 2:
    print('NO')
else:
    have = 0
    if a in mw:
        have+=1
    if b in mw:
        have+=1

    if min(mw)>=a and max(mw)<=b and n-m >= 2-have :
        print('YES')

    else:
        print('NO')
