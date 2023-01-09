import sys

input = sys.stdin.readline

def filter_multiples(lst, multiple):
    '''
    lst: 필터를 적용할 리스트
    multiple: 제외할 배수
    '''
    filtered_lst = []
    for idx in range(len(lst)): # 시간복잡도 O(N)
        if (idx+1) % multiple != 0:
            filtered_lst.append(lst[idx])
    return filtered_lst

def init():
    K = int(input())
    m = int(input())
    excludes = [int(input()) for _ in range(m)] # 제외할 배수 저장

    K_lst = list(range(1,K+1)) # 100최대 
    for exclude in excludes:
        K_lst = filter_multiples(K_lst, exclude)

    for num in K_lst:
        print(num)

init();