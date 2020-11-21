def moveZeroes(nums) -> None:
    zeros, nonzeros = [],[]
    for num in nums:
        if num == 0:
            zeros.append(0)
        else:
            nonzeros.append(num)
    return nonzeros+zeros

def moveZeroes1(nums):

    i,cnt = 0,0
    while cnt<len(nums):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
        else:
            i+=1
        cnt+=1


nums = [0,1,0,3,12]
moveZeroes1(nums)
print(nums)