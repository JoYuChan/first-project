import sys
A,B,V = map(int,sys.stdin.readline().split()) # 시간초과
cnt = 0
distance = 0
while True:
    cnt += 1
    distance += A
    if distance >=V:
        break
    else:
        distance -= B
print(cnt)


'''a,b,v = map(int,input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)'''
