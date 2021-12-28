## ***Arithmetic***

<br></br>
### Q 2588. 
> https://www.acmicpc.net/problem/2588<br>


```python
a = int(input())
b = input()[::-1] # reverse a string. select char from start to end ~ and step in -1
res = 0 
for idx, el in enumerate(b):
    r = a*int(el)
    print(r)
    res += r*10**idx
print(res)
```

     472
     385


    2360
    3776
    1416
    181720



```python

```
