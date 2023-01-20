### 📐 무슨 레포지토리인가요?
> 알고리즘 문제풀이 저장소입니다. 

# 폴더 구조
tree=$(tree -tf --noreport -I '*~' --charset ascii $1 |
       sed -e 's/| \+/  /g' -e 's/[|`]-\+/ */g' -e 's:\(* \)\(\(.*/\)\([^/]\+\)\):\1[\4](\2):g')

printf "# Project tree\n\n${tree}"

### 사용 언어
> Python3를 사용합니다
