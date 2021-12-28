# ***Back Tracking***
- 불필요한 경로를 쳐내고 최대한 올바른 길로 가자. 반복문의 횟수를 줄일 수 있어 효율적임

<br></br>
### Q 15649. 
> https://www.acmicpc.net/problem/15649 <br>


```python
from itertools import permutations
N,M = map(int,input().split())
lst = list(range(1,N+1))
for seq in permutations(lst,M): # 순열 permuations
    for n in seq:
        print(n, end=" ")
    print()
```

     4 2


    1 2 
    1 3 
    1 4 
    2 1 
    2 3 
    2 4 
    3 1 
    3 2 
    3 4 
    4 1 
    4 2 
    4 3 


<br>

++ ***순열/조합 함수 직접 구현***

![Screen Shot 2021-12-28 at 5.10.21 PM.png](attachment:d935e7cf-64dd-4bdb-8e2d-7a687a8aee67.png)

조합: 서로 다른 n개의 대상에서 중복없이 r개를 뽑아 일렬로 배열한 것  (combination) <br>
순열: 서로 다른 n개의 대상에서 r개를 뽑는 모든 경우의 수 (permutation)

![Screen Shot 2021-12-28 at 6.12.06 PM.png](attachment:ea7d7e00-de4b-4e4f-b382-ce3ad9c708c2.png)

reference: https://www.techiedelight.com/find-all-permutations-string-python/


```python
def swap(arr, idx, i):
    temp = arr[idx]
    arr[idx] = arr[i]
    arr[i] = temp

def permutations(arr, idx=0):
    if idx + 1 == len(arr):
        print(''.join(arr))
    
    for i in range(idx, len(arr)):
        swap(arr, idx, i)
        permutations(arr, idx + 1) # recursion
        swap(arr, idx, i) # 원상복구 

s = 'ABC'
permutations(list(s))
```

    ABC
    ACB
    BAC
    BCA
    CBA
    CAB

