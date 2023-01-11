import sys
input = sys.stdin.readline

N = int(input())
for i in range(1, N+1):
    char_lst = input().rstrip().split()
    stk = []
    while char_lst:
        stk.append(char_lst.pop())
    print(f"Case #{i}:", " ".join(stk))