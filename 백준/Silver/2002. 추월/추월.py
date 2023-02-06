import sys

input = sys.stdin.readline

n = int(input())
carsIn = {input().rstrip():i for i in range(n)}
carsOut = [input().rstrip() for _ in range(n)]

cnt = 0
for i in range(0, n-1):
    flag = False
    numIn = carsIn[carsOut[i]]
    for j in range(i+1, n):
        nxt = carsIn[carsOut[j]]
        if nxt < numIn:
            flag = True
            break
    if flag:
        cnt += 1

print(cnt)            
        