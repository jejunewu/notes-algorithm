def canCompleteCircuit(gas, cost):
    return gas

def isC(gas,cost):

    remainGas = gas[0]
    i = 0
    while remainGas - cost[i]:
        remainGas  -= cost[i]
        i+=1
        remainGas += gas[i]

    return i==len(gas)



################### Test ########################
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

gas1 =  [3,4,5,1,2]
cost1 = [5,1,2,3,4]
ans = canCompleteCircuit(gas, cost)
ans = isC(gas1,cost1)
print(ans)