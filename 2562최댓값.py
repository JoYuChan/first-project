import sys
list = []
num = map(int,sys.stdin.readlines())
for i in num:
    list += [i]
print(max(list))
print(list.index(max(list))+1)



