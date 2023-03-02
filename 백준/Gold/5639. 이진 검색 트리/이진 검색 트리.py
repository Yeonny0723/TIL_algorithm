"""
전위순회 결과가 주어졌을 떄, 후위순회 결과를 구하는 문제.
"""
import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

preorder = []
while True: # 입력의 길이를 모르기에, 입력을 안한 상태로 유지 -> 오류 -> break 하도록 설계
    try:
        preorder.append(int(input())) # 원소 추가
    except:
        break

def postorder(start, end): # 인덱스
    if start > end: # 재귀 중단
        return

    newStart = start + 1 # 분리되는 지점 찾기
    for i in range(start+1, end+1):
        if preorder[start] < preorder[i]:
            newStart = i
            break

    # 왼쪽 트리
    postorder(start + 1, newStart - 1) # left --(a)
    # 오른쪽 트리
    postorder(newStart, end) # right
    # 루트 출력
    print(preorder[start])

postorder(0, len(preorder)-1) # 시작과 끝 인덱스