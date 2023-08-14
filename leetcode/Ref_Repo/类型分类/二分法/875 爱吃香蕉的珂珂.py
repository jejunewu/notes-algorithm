
def minEatingSpeed(piles, H):

    def canEat(piles, speed, H):
        s = 0
        for pile in piles:
            s += pile//speed if pile%speed == 0 else (pile+speed)//speed
        return s > H

    L = 1
    R = max(1,max(piles))

    while L<R:
        mid = (L+R) >> 1
        if canEat(piles, mid, H):
            L = mid+1
        else:
            R = mid
    return L

piles = [3,6,7,11]
H = 8
t = minEatingSpeed(piles, H)
print(t)

