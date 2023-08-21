def lemonadeChange(bills):
    myMoney = {5:0, 10:0}

    for bill in bills:
        if bill == 5:
            myMoney[5] += 1
        elif bill == 10:
            myMoney[10] +=1
            if myMoney[5] > 0:
                myMoney[5]-=1
            else:
                return False
        elif bill == 20:
            if myMoney[10]>0 and myMoney[5]>0:
                myMoney[10]-=1
                myMoney[5]-=1
            elif myMoney[5]>2:
                myMoney[5]-=3
            else:
                return False
    return True

bills = [5,5,5,10,20]
ans = lemonadeChange(bills)
print(ans)