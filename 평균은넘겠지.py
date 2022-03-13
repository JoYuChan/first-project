n = int(input())
for i in range(n+1):
    score = list(map(int,input().split()))
    sum = 0
    for a in score:
        sum += a
    print((sum-n)/n,"%") #이게되네
