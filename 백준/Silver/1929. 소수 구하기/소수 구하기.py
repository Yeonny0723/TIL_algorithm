import math
import sys

input = sys.stdin.readline

def solution():
    M, N = map(int, input().rstrip().split(" "))
    potentialPrime = math.floor(math.sqrt(N))
    for num in range(M, N+1):
        isPrimeNum = True if num != 1 else False # 소수 여부 확인 flag
        for prime in range(2, potentialPrime+1): # 나눌 수 있는 값 
            if num <= prime:
                continue
            if not isPrimeNum: # 소수가 아니라면
                break
            if (num % prime) == 0:
                isPrimeNum = False
    
        if isPrimeNum:
            print(num)

solution()

