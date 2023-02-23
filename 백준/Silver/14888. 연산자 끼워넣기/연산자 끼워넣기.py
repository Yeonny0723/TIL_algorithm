import sys
input = sys.stdin.readline

def dfs(ans, i, plus, minus, multiply, divide):

    if i == n:
        global minV, maxV
        minV = min(minV, ans)
        maxV = max(maxV, ans)
        return

    _ans = ans
    for op in ["+", "-", "/", "*"]:
        if op == "+":
            if plus == 0: continue # 이미 0이라면 추가 못하도록
            plus -= 1
            _ans += nums[i]
        elif op == "-":
            if minus == 0: continue
            minus -= 1
            _ans -= nums[i]
        elif op == "*":
            if multiply == 0: continue
            multiply -= 1
            _ans *= nums[i]
        else:
            if divide == 0: continue
            divide -= 1
            if _ans < 0:
                _ans = -((-_ans) // nums[i])
            else:
                _ans = _ans // nums[i]

        newOps.append(op)
        dfs(_ans, i+1, plus, minus, multiply, divide)
        _op = newOps.pop()
        _ans = ans # 이전값 복귀

        if _op == "+": # pop 후 복귀
            plus += 1
        elif _op == "-":
            minus += 1
        elif _op == "*":
            multiply += 1
        else:
            divide += 1

n = int(input())
nums = list(map(int, input().rstrip().split()))
plus, minus, multiply, divide = map(int, input().rstrip().split())
newOps, minV, maxV = [], int(1e8), -int(1e8)
dfs(nums[0], 1, plus, minus, multiply, divide)
print(maxV)
print(minV)