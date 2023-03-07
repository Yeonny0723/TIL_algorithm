`
num: 연속된 수
total: 총 합

조건: 
- 항상 답이 존재. 
- 정수 (음수 가능)

패턴:
예를 들어
num = 3, total = 12
x x+1 x+2
=> 합이 3x + (1+2) = 12
=> x = (12 - (1+2)) / 3
=> x = 3

num = 5, total = 5
x x+1 x+2 x+3 x+4
=> 합이 3x + (1+2+3+4) = 5
=> x = (5 - (1+2+3+4)) / 3
=> x = -1.6... (올림)
`

function solution(num, total) {
    
    const x = Math.ceil((total - ((num-1)*(num+1))/2) / num)
    
    let ans = []
    for(let i=0; i < num; i++){
        ans.push(x + i)
    }
    return ans;
}