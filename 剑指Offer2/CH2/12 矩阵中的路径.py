def exist(board, word):
    def isValid(i, j):
        return 0 <= i < m and 0 <= j < n

    def DFS(i, j, seen):
        if len(seen) >= len(word):
            return True
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = i + dx, j + dy
            if isValid(x, y) and word[len(seen)] == board[x][y] and (x, y) not in seen:
                seen.add((x, y))
                if DFS(x, y, seen):
                    return True
                seen.discard((x, y))
        return False

    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0] and DFS(i, j, {(i, j)}):
                return True
    return False


################### Test ########################
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"


ans = exist(board, word)
print(ans)