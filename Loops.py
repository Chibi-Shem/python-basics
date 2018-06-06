num = 10
while(num > 0):
    print(num)
    num -= 1

lst = [1, 2, 3, 4, 5]

for x in lst:
    print(x)

for x in range(len(lst)):
    if x == 3:
        break
    print(lst[x])

while x in lst:
    for y in range(len(lst)):
        if y % 2 == 0:
            continue
        print(str(y) + " is odd")
    x += 1
    if x == 3:
        break
