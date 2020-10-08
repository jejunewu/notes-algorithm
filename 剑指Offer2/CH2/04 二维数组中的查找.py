def findNumberIn2DArray(matrix, target: int) -> bool:

    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    rows, cols = len(matrix),len(matrix)
    i=0
    while i <rows:
        j=0
        while j<cols and i <rows:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i+=1
                j=0
            else:
                j+=1
        i+=1
    return False


################### Test ########################

# matrix = [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# target = 24

matrix = []
target = 1
ans = findNumberIn2DArray(matrix, target)
print(ans)