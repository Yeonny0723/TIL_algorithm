import sys

input = sys.stdin.readline

haligali = {}
for _ in range(int(input().rstrip())):
    s, n = input().rstrip().split(" ")
    
    if haligali.get(s):
        haligali[s] += int(n)
    else: 
        haligali[s] = int(n)
 
res = "NO"  
for k, v, in haligali.items():
    if v == 5:
        res = "YES"
print(res)