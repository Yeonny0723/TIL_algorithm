# 1000엔에서 지불할 돈을 제외한 거스름돈을 가장 적은 잔돈으로 돌려주는 조합을 찾자 
import sys

input = sys.stdin.readline

def getChange():
    P = 1000 - int(input())
    quotient, remains = 0, P
    count = 0
    for c in [500, 100, 50, 10, 5, 1]:
        quotient = remains // c
        remains = remains % c
        count += quotient
        
    return count
    
print(getChange())