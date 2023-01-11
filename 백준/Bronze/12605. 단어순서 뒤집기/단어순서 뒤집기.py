import sys

input = sys.stdin.readline

N = int(input())
for i in range(1, N+1):
    char_lst = input().rstrip().split()
    print(f"Case #{i}:", end= " ")
    while char_lst:
        print(char_lst.pop(), end=" ")