def 한수(num):
    hansu = 0
    for i in range(1,num+1):
        numlist = list(map(int,(str(i))))
        if i <100:
                hansu += 1
        elif (numlist[0]-numlist[1]) == (numlist[1]-numlist[2]):
                hansu += 1
    return hansu
num = int(input())
print(한수(num))