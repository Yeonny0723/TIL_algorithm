import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split(" "))
ans = []
newPpl = {input().rstrip():1 for _ in range(n)} 
for _ in range(m):
    name = input().rstrip()
    if newPpl.get(name):
        ans.append(name)

print("\n".join([str(len(ans)), *sorted(ans)]))