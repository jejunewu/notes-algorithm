def Perm(arrs):

    if len(arrs)==1:
        return [arrs]
    result = []  # 最终的结果（即全排列的各种情况）
    for i in range(len(arrs)):
        rest_arrs = arrs[:i]+arrs[i+1:]  # 取出arrs中的第 i个元素后剩余的元素
        rest_lists = Perm(rest_arrs)   # 剩余的元素完成全排列
        lists = []
        for term in rest_lists:
             lists.append(arrs[i:i+1]+term)  # 将取出的第 i个元素加到剩余全排列的前面
        result += lists
    return result

arrs = [1,2,3,4]
t = Perm(arrs)
print(t)