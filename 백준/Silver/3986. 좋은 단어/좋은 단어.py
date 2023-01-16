def solution():
    count = 0
    for _ in range(int(input())):
        stk = []
        s = input()
        for ch in s:
            if not stk:
                stk.append(ch)
                continue
            
            if stk[-1] == ch:
                stk.pop()
                continue
            else:
                stk.append(ch)

        if len(stk) == 0:
            count += 1 

    print(count)
            
solution()