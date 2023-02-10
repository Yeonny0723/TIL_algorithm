import sys

input = sys.stdin.readline

def makeTree(root, h):
    if h == 1:
        return
    childLeft = root - 2**(h-2)
    childRight = root + 2**(h-2)
    h -= 1
    tree[h].append(nodes[childLeft-1])
    tree[h].append(nodes[childRight-1])
    makeTree(childLeft, h)
    makeTree(childRight, h)

h = int(input())
nodes = list(map(int, input().rstrip().split(" ")))
rootIdx = len(nodes) // 2 + 1
tree = [[] for _ in range(h+1)]
tree[h] = [nodes[rootIdx-1]]
makeTree(rootIdx, h)

for i in range(h,0,-1):
    print(*tree[i])