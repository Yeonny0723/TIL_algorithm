import sys

input = sys.stdin.readline

def dfs():
    if len(ans) == M: # dfs의 깊이가 M과 일치할 때까지 반복
        print(" ".join(map(str,ans)))
        return
    
    for i in range(1, N+1):
        if i in ans: # 이미 뽑은 원소는 중복하지 않도록
            continue
        # 1~N까지 경우에 대해 추가 
        ans.append(i) 
        # back-tracking 기법 사용
        dfs()
        # 앞서 추가한 원소를 pop
        ans.pop()
        
N, M = map(int, input().split())  # 1~N까지 수 중 M개를 뽑은 순열을 사전 순으로 정렬
ans = [] # 뽑을 원소를 담을 스택 
dfs()