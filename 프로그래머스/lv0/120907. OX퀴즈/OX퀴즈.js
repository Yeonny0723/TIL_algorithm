`
입력: 수식 문자열 리스트
출력: "O", "X" <- 수식의 유효성을 배열 형태로
조건:
- 숫자 & 연산자 사이 항상 공백 하나
- 각 숫자는 정수 (음수 가능)
- 연산자는 + | -

계획:
- 배열 각 원소 순회
- 원소 "=" <- split()
- 쪼개진 왼쪽 문자 + 들어있다면(includes, indexOf 키워드 검색), + 기준 split, 양 쪽 숫자 더해주면되겠다
- -, - 기준 split, 양 쪽 숫자 빼주면 되겠다
- 왼쪽 결과값과 = 오른쪽 결과값을 비교 
`

function solution(quiz) {
    var answer = [];
    for (const q of quiz){
        const [formula, res] = q.split(" = ")
        const isPlus = formula.includes("+")
        
        let newRes;
        if (isPlus){
            const [num1, num2] = formula.split(" + ")
            newRes = +num1 + +num2
        } else {
            const [num1, num2] = formula.split(" - ")
            newRes = +num1 - +num2
        }
        
        if (newRes === +res){
            answer.push("O")
        } else {
            answer.push("X")
        }
        
    }
    return answer;
}




