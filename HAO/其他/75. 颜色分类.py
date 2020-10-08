def sortColors(nums) -> None:

    def swap(List, srcIndex, destIndex):
        List[srcIndex],List[destIndex] = List[destIndex], List[srcIndex]

    size = len(nums)
    zero, two = 0, size

    i = 0
    while i < two:
        if nums[i] == 0:
            swap(nums, i, zero)
            zero+=1
            i+=1
        elif nums[i] == 1:
            i+=1
        else:
            two-=1
            swap(nums, i, two)

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)