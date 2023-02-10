def preorder(root):
    if root == ".":
        return
    global ansPre
    ansPre += root
    preorder(tree[root][0])  # left 노드로 먼저 이동
    preorder(tree[root][1])  # right 노드이동
 
def inorder(root):
    if root == ".":
        return
    inorder(tree[root][0])  # left 노드로 먼저 이동 
    global ansIn
    ansIn += root
    inorder(tree[root][1])  # right 노드 이동 
 
def postorder(root):
    if root == ".":
        return
    postorder(tree[root][0])  # left
    postorder(tree[root][1])  # right
    global ansPost
    ansPost += root


# 트리 생성
# {'A': ['B','C']} 형태 
tree = {}
for _ in range(int(input())):
    root, left, right = input().split()
    tree[root] = [left, right]

ansPre, ansIn, ansPost = '','',''
start = 'A'
preorder(start)
inorder(start)
postorder(start)
print("\n".join([ansPre, ansIn, ansPost]).rstrip())