s = int(input())
for i in range(s):
    r,R = map(str,input().split())#   r, R = input().split() 이거 가능
    n =''
    for a in R:
        n += a*int(r)
    print(n)
'''n = int(input())

for _ in range(n):
    cnt, word = input().split()
    for x in word:
        print(x*int(cnt), end='')  # end='' 옆으로 붙임
    print()  # 줄넘김'''
    




