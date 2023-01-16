def solution():
    open = False
    res, stk = [], []
    for ch in input():
        if ch == " ":
            while stk:
                res.append(stk.pop())  
            res.append(ch)
            continue

        if ch == "<":
            while stk:
                res.append(stk.pop())
            res.append(ch)
            open = True
            continue

        elif ch == ">":
            res.append(ch)
            open = False
            continue

        else: 
            if open:
                res.append(ch)
            else:
                stk.append(ch)
            continue

    while stk:
        res.append(stk.pop()) 

    print("".join(res).rstrip())

solution()