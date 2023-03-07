`
주어진 숫자 배열이 등비수열인지, 등차수열인지 판단. 배열 그 다음 수 예측 후 반환. 
입력: 숫자 배열
출력: 주어진 수열 다음 수
조건: 공비는 0이 아닌 정수. 등비|등차 수열이 아닌 경우는 없음. 
접근: 
- 첫번째-두번째 원소, 두번재 세번째 원소를 비교하면 등비, 등차인지 알 수 있겠군...
`

function solution(common) {
    let isArith; // true: 등차, false: 등비
    let gap;
    if (common[1] - common[0] == common[2] - common[1]){
        isArith = true
        gap = common[1] - common[0]
    } else {
        isArith = false
        gap = common[1] / common[0]
    }
    
    return isArith ? common[common.length-1] + gap : common[common.length-1] * gap
}