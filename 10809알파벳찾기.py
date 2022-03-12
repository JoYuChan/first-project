# from string import ascii_lowercase

# s = input()
# for i in str(ascii_lowercase):
#     if i in s:
#         print(s.index(i),end=" ")
#     else:
#         print(-1,end=" ")

word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x))) #이게더 효율적이네
    


