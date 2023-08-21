# DFS 递归深度搜索
def letterCombinations(digits: str):

    dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    res = []

    def findCombination(digits, index, s):
        if index == len(digits):
            res.append(s)
            return
        num = digits[index]
        letter = dict[num]
        for i in range(len(letter)):
            findCombination(digits, index+1, s+str(letter[i]))
        return

    findCombination(digits, 0, '')

    return res


digits = ""
ans = letterCombinations(digits)
print(ans)