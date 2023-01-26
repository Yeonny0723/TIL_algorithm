def close(k):
    for i in range(1, n+1):
        if (i)%k == 0:
            x = doors[i-1] 
            doors[i-1] = 0 if x else 1 # 1이면 0, 0이면 1
            
doors = []
for _ in range(int(input())):
    n = int(input())
    doors = [0 for _ in range(n)] # 1: 열람, 0: 닫힘
    for k in range(1, n+1): # 1~n+1 방에 대하여 
        close(k)
    print(doors.count(1))