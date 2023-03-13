"""
4보가 큰 모든 짝수는 두 홀수 소수 (a,b)의 합으로 나타낼 수 있다??! 검증하는 문제
조건: 여러개 조합이 있는 경우, b-a가 가장 큰 것 출력. 나타낼 수 없는 경우엔 "Goldbach's conjecture is wrong." 출력

입력: 4보다 큰 짝수(6<=n<=10^6). (0이 입력될 때까지 계속 검증)
출력: 입력짝수 = a + b

접근:
- 10^6+1 길이 배열 선언 (인덱스를 숫자로 갖도록)
- 2~10^3 수를 순회(a), a제외 그 배수 제거.
- 위 과정이 끝난 후 남은 숫자가 바로 소수.
- 제거한 배수를 순서대로 순회 -> n-a도 소수라면 출력.
"""
import sys
input = sys.stdin.readline

nums = [1] * (10**6+1) # 1: 소수, 0: 소수 아님.
for j in range(2, 10**3+1): # 제곱근
    i = 2
    while j * i < 10**6 + 1:
        nums[j * i] = 0
        i += 1

while True:
    n = int(input())
    res = "Goldbach's conjecture is wrong."
    if n == 0:
        break
    for i in range(2, n+1):
        if i % 2 == 1:
            if nums[i] == 1 and nums[n - i] == 1:
                res = f"{n} = {i} + {n-i}"
                break
    print(res)

