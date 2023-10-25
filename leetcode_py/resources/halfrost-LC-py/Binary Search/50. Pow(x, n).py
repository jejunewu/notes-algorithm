def myPow(x: float, n: int):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n<0:
        n = (-1)*n
        x = 1/x
    tmp = myPow(x, n//2)
    if n%2 == 0:
        return tmp**2
    return tmp**2*x

### 递归
ans = myPow(2, 10)
print(ans)