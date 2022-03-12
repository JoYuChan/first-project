import sys
A, B, C = map(int,sys.stdin.readline().split()) # 이건 구현은 했지만 시간초과로 실패
sell = 1
new_B = 0
new_C = 0
if C > B:
    while (True):
        new_B = new_B+B
        new_C = new_C+C
        if (A+new_B)>=new_C:
            sell += 1
        else:
            print(sell)
            break
        
else:
    print(-1)


'''A, B, C = map(int, input().split()) 

if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))'''