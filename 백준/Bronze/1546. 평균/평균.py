import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    scores = input().split(" ")
    scoreSum, maxScore = 0, 0
    for score in scores:
        score = int(score)
        scoreSum += score
        maxScore = max(maxScore, score)
    ans = (scoreSum/maxScore) * 100 / N
    print(ans)
        
        
solution()