balls = [1,2,3]
for _ in range(int(input())):
    i, j = map(int, input().split())
    balls[i-1],balls[j-1] = balls[j-1], balls[i-1]
    
print(balls.index(1)+1)