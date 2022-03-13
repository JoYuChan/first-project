import sys
m = int(sys.stdin.readline()) 
n = int(sys.stdin.readline())
new_mn = []
for i in range(m,n+1):
    if i >1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            new_mn.append(i)
if len(new_mn) == 0:
    print(-1)
else:
    print(sum(new_mn))
    print(min(new_mn))

'''start_num = int(input())
last_num = int(input())

sosu_list = []
for num in range(start_num, last_num+1):
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 num-1까지
            if num % i == 0:
                error += 1
                break  # 2부터 num-1까지 나눈 몫이 0이면 error가 증가하고 for문을 끝냄
        if error == 0:
            sosu_list.append(num)  # error가 없으면 소수리스트에 추가
            
if len(sosu_list) > 0 :
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print(-1)'''