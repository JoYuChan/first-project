case = int(input())
for i in range(case):
    A = input()
    B = list(A)
    sum = 0
    plus = 1
    for test in B:
        if test == 'O':
            sum += plus
            plus += 1
        elif test == 'X':
            plus = 1 
    print(sum)

