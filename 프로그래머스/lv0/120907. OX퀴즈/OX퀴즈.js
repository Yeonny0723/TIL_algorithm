`
입력: 수식 문자열 리스트
출력: 수식 유효성 리스트
조건: 
- 연산자는 + | - 1개. 
- 숫자는 정수 (음수 가능)

계획: 
"=" 문자 기준 쪼개고, 
수식에 "+", "-"가 포함된 케이스를 나누어,
각각의 경우에 계산해주고, 쪼개진 결과값과 비교하면 되겠다. 
`

function solution(quiz) {
    return quiz.map(q => {
        const [formula, res] = q.split(" = ")
        const isPlus = formula.includes("+")
        const [num1, num2] = formula.split(isPlus ? " + " : " - ") // (2)
        const newRes = +num1 + (+num2 * (isPlus ? 1 : -1)) // (3)
        return newRes === +res ? "O" : "X"
    })
}