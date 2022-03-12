N = int(input())
group_number = 0
for i in range(N):
    error = 0
    A = input()
    for j in range(len(A)-1): # 인덱스 범위 생성 : 0부터 단어개수 -1까지 
        if A[j] != A[j+1]:  # 연달은 두 문자가 다른 때,
            new_A = A[j+1:] # 현재글자 이후 문자열을 새로운 단어로 생성
            if new_A.count(A[j])>0:  # 남은 문자열에서 현재글자가 있있다면
                error +=1 # error에 1씩 증가.
    if error == 0:
        group_number +=1
print(group_number)

'''N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)'''

'''N=int(input())

answer=0

for i in range(N):
    word = input()
    for j in range(len(word)):
        if j!=len(word)-1:
            if word[j]==word[j+1]:
                pass
            elif word[j] in word[j+1:]:
                break
        else:
            answer+=1
print(answer)
 '''
