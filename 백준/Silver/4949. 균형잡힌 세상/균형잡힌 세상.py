def solution(s):
    stk = []
    res = "no"
    for ch in s:
        if ch == "]":
            if not stk:
                return res
            if stk[-1] == "[":
                stk.pop()
            else:
                return res
            
        elif ch == "[":
            stk.append(ch)

        elif ch == ")":
            if not stk:
                return res
            if stk[-1] == "(":
                stk.pop()
            else:
                return res
            
        elif ch == "(":
            stk.append(ch)
            
        else:
            continue
    
    if not stk: # stk이 비어있다면
        res = "yes"
    return res

while True:
    s = input()
    if s == ".":
        break
    else: 
        res = solution(s)
        print(res)