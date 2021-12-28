## ***Basic Mathmetics***

<br></br>
### Q 1712. 
> https://www.acmicpc.net/problem/1712<br>


```python
A,B,C = map(int,input().split())
```

     3 2 2



```python
res = int(A/(C-B)) + 1 if C-B != 0 else -1 # zerodivisionerror
print(res if res > 0 else -1)
```

    -1

