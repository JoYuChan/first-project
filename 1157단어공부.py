A = input().upper()#알파벳 단어 입력
aList = list(set(A))#중복제거
B = []
for i in aList:
    C = A.count(i)
    B.append(C) #B +=[C]
if B.count(max(B))>1:
    print("?")
else:
    print(aList[B.index(max(B))])



