N = int(input())

bag = 0
while N>=0:
    if N % 5 == 0:
       bag += N//5
       print(bag)
       break
    N -= 3
    bag +=1
else:
    print(-1)


'''inp = int(input())
Box = 0
while True:
    if (inp % 5) == 0:
        Box = Box + (inp//5)
        print(Box)
        break
    inp = inp-3
    Box += 1
    if inp < 0:
        print("-1")
        break'''

