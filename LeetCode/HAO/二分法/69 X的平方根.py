def mySqrt(x):

    left = 1
    right = x
    ans = -1
    while left <= right:
        mid = (left + right)//2
        if mid * mid <= x:
            ans = mid
            left = mid + 1
        else:
            right = mid -1
    return ans

t = mySqrt(0)
print(t)