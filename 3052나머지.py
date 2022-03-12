import sys
num=[]
a= list(map(int,sys.stdin.readlines()))
for i in a:
    num.append(i%42)
num = set(num)
print(len(num))

