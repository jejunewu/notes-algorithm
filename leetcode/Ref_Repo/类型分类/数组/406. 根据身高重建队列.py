def reconstructQueue(people):
    people.sort(key=lambda x: (-x[0], x[1]))
    n = len(people)
    ans = list()
    for person in people:
        ans[person[1]:person[1]] = [person]
    return ans

################### Test ########################
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

ans = reconstructQueue(people)
print(ans)