import sys

input = sys.stdin.readline

def getLastDigit(num):
    tens = num // 10
    units = num % 10
    sumDigit  = tens + units
    unitsSum = sumDigit % 10
    return units * 10 + unitsSum

def solution():
    N = int(input())
    newN, isFound, count = N, False, 0
    while not isFound:
        newN = getLastDigit(newN)
        count += 1
        if newN == N:
            isFound = True
    print(count)
    
solution()