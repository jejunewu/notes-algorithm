# 超时
def exchange1(nums):
    count, i,size = 0,0,len(nums)

    while i<size-1:
        if count < size-i and nums[i] & 1 == 0:
            j = i+1
            while j<size:
                if nums[j] & 1 == 1:
                    nums.append(nums[i])
                    nums[i] = nums[j]
                    nums.pop(j)
                j+=1
        elif count >=size-i:
            return nums
        i+=1
    return nums

def exchange(nums):
    i,j = 0,len(nums)-1
    while i+1<j:
        if nums[i] & 1== 1:
            i+=1
        if nums[j] & 1== 0:
            j-=1
        if nums[i] & 1== 0 and nums[j] & 1 == 1:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1
    return nums


################### Test ########################
nums = [2,16,3,5,13,1,16,1,12,18,11,8,11,11,5,1]
nums1= [11,9,3,7,16,4,2,0]
ans = exchange(nums)
print(ans)
