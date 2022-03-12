import numbers
from operator import le
from re import S


numbers = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
sum = 0 
number = input()
for i in range(len(number)):
    for j in numbers:
        if number[i] in j:
            sum += numbers.index(j)+3
print(sum)