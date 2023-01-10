import sys

input = sys.stdin.readline

class Node: # 노드 클래스
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
        
N = int(input())
for _ in range(N):
    s = input().rstrip()
    
    head = Node("")
    node = head
    
    for ch in s:
        if ch == "<":
            if node.prev:
                node = node.prev

        elif ch == ">":
            if node.next:
                node = node.next

        elif (ch == "-"):
            if node.prev: 
                if node.next: # 현 위치가 마지막 노드라면 
                    node.prev.next = node.next
                    node.next.prev = node.prev
                else:
                    node.prev.next = None
                node = node.prev

        else: # 새로운 노드 추가 
            new_node = Node(ch)
            new_node.prev = node
            if node.next: # 현 위치가 마지막이 아닌 경우
                node.next.prev = new_node
                new_node.next = node.next

            node.next = new_node
            node = node.next # 새로운 노드로 위치 이동  
            
    node = head
    while node:
        print(node.value, end="")
        node = node.next
    print()