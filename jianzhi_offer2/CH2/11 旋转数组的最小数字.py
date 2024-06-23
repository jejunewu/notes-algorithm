def minArray(numbers):

    i = 0
    while i<len(numbers)-1:
        print(i)
        if numbers[i] > numbers[i+1]:

            return numbers[i+1]
        i+=1


    return numbers[0]



################### Test ########################
numbers = [5,6,7,8,4]
ans = minArray(numbers)
print(ans)