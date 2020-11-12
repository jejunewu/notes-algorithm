def kClosest(points, K):
    d2, ans = [], []
    for point  in points:
        d2.append(point[0]**2 + point[1]**2)

    print(d2)
    while len(ans) < K:
        minPoint = points[d2.index(min(d2))]
        if minPoint not in ans:
            ans.append(minPoint)
        points.remove(minPoint)
        d2.remove(min(d2))

    return ans

def kClosest2(points, K):
    points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2))
    return points[:K]

################### Test ########################
points = [[3,3],[5,-1],[-2,4]]
K = 2
ans = kClosest(points, K)
print(ans)