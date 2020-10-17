## 递归：超时
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

##
def fib2(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    else:
        pre,post, idx = 0, 1, 2
        while idx <= n:
            tmp = post
            post = pre+post
            pre = tmp
            idx+=1
        return post % 1000000007

################### Test ########################
# ans = fib(101)
ans2 = fib2(50)
print('======')
print(ans2)