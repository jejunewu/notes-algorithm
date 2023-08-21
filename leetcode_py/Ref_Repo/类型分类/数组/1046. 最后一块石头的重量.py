def lastStoneWeight(stones):

    while len(stones) > 1:
        stones = sorted(stones)
        x,y = stones[-2],stones[-1]
        stones.pop(-2)
        stones.pop(-1)
        if y-x > 0:
            stones.append(y-x)

    return stones[0] if stones else 0

stones = [1,1,1,1]
ans = lastStoneWeight(stones)
print(ans)