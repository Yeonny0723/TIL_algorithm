text = input()

text_lst = []
for i in range(len(text)): # n
    text_lst.append(text[i:])
    
for char in sorted(text_lst): # 정렬 n*logn
    print(char)
