def allCellsDistOrder(R: int, C: int, r0: int, c0: int):
    mesh = []
    manDist = []
    ans = []
    for r in range(R):
        for c in range(C):
            tmpDist = abs(r - r0) + abs(c - c0)
            mesh.append([r,c])
            manDist.append(tmpDist)
            # print(r,c)

    while manDist:
        minIdx = manDist.index(min(manDist))
        ans.append(mesh[minIdx])
        mesh.pop(minIdx)
        manDist.pop(minIdx)
    return ans

################### Test ########################

R = 2
C = 2
r0 = 0
c0 = 1
ans = allCellsDistOrder(R, C, r0, c0)
print(ans)
