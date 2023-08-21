def intersection(nums1, nums2):
    res = []
    for n1 in nums1:
        if n1 in nums2:
            res.append(n1)

    return  list(set(res))


################### Test ########################

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
ans = intersection(nums1, nums2)
print(ans)