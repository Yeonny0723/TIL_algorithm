"""
인오더 결과 & 포스트오더 결과가 주어질 때,프리오더를 출력하라
(자식 노드가 없는 경우도 고려)

- postorder 맨 마지막 값은 최상단 root 노드
- inorder에서 root 노드 기준 left, right 트리가 나뉨
- 나뉜 left 트리에서 가장 작은 값, right 트리에서 가장 작은 값이
  각 서브 트리의 root 노드

"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def preorder(inStart, inEnd, postStart, postEnd):
    if (inStart > inEnd) or (postStart > postEnd):
        return

    root = postorder[postEnd]
    ans.append(root)

    leftNode = idx[root] - inStart
    rightNode = inEnd - idx[root]

    preorder(inStart, inStart + leftNode - 1, postStart, postStart + leftNode - 1)
    preorder(inEnd - rightNode + 1, inEnd, postEnd - rightNode, postEnd - 1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
ans = []
idx = [0] * (n + 1)
for i in range(n):
    idx[inorder[i]] = i # 1-n까지 값이 inorder의 몇번째 인덱스에 있는지

preorder(0, n - 1, 0, n - 1)
print(*ans)