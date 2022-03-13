N = int(input())
cnt = 0

A = list(map(int,input().split()))
for i in A:
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            cnt += 1

print(cnt)

