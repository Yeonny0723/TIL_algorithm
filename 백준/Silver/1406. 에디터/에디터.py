import sys

input = sys.stdin.readline

class Node:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
        
s = input().rstrip()
m = int(input())
head = Node('')
node = head
for ch in s:
    node.next = Node(ch)
    node.next.prev = node
    node = node.next


for _ in range(m): # 커서의 위치 == 커서 앞 문자 기준
    cmd = input().rstrip() 
    if (cmd == "L") and (node.prev): 
        node = node.prev #  이전 노드로 이동 
        continue
        
    if (cmd == "D") and (node.next):
        node = node.next # 다음 노드로 이동
        continue
        
    if (cmd == "B") and (node.prev): # 현재 노드 삭제
        if node.next: # 중간 노드일 때
            node.prev.next = node.next
            node.next.prev = node.prev
        else: # 마지막 노드일 때 
            node.prev.next = None
        
        node = node.prev # 커서 이동
        continue
        
    if ("P" in cmd): # 커서 뒤 원소 생성 (abc"d"x -> abcd"y"x). (abc"d"->abcd"x")
        new = cmd.split(" ")[-1]
        new_node = Node(new)
        new_node.prev = node
        new_node.next = node.next
        
        if node.next: # 중간에 위치한 경우 
            node.next.prev = new_node
            
        node.next = new_node
        node = node.next # 이동
        continue # 하위 코딩 무시 다음 루프
    

node = head
while node:
    print(node.value, end="")
    node = node.next