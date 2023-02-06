import sys

input = sys.stdin.readline

words = {input().rstrip(): 1 for _ in range(int(input()))}
for word in words:
    word_flipped = word[::-1]
    if words.get(word_flipped):
        length = len(word)
        ch = word[length//2]
        print(length, ch)
        break
