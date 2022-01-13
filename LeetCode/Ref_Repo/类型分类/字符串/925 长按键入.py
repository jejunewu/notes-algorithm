def isLongPressedName(name, typed):

    i=j=0
    while i< len(name) and j <len(typed):
        if name[i] == typed[j]:
            i+=1
            j+=1

        else:
            if j > 0 and typed[j] == typed[j-1]:
                j+=1
            else:
                return False

    if i < len(name) and j == len(typed):
        return False

    while i == len(name) and j <len(typed):
        if typed[j] != typed[j-1]:
            return False
        j+=1

    return True


################### Test ########################
name = "pyplrz"
typed = "ppyypllr"

ans = isLongPressedName(name, typed)
print(ans)