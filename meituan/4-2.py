# nx = [int(i) for i in input().split()]
n, x = 5,1#nx[0], nx[1]
score = [1,0,0,0,0]#[int(i) for i in input().split()]

score = sorted(score)[::-1]
if x == 0:
    print(0)
else:
    # print(score)
    ans = 0
    for i in range(x):
        if score[i]>0 :
            ans+=1
        else:
            break
    print(score)
    print(i)
    while i+1 < n and score[i]>0 and score[i] == score[i+1]:
        ans+=1
        i+=1

    print('ans:',ans)