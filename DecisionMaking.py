num = 99

if(num > 99):
    print("num is greater than 99")
elif(num is 99):
    print('num is 99')
else:
    print("num is less than 100")

if(num < 100):
    print('num is less than 100')

if(num < 100):
    if(num > 80):
        print('num is greater than 80 and less than 100')
    else:
        print('num is less than 81')

num = 1
num2 = 0
if(num == 0):
    print("num is 0")
elif(num is 1):
    print('num is 1')
else:
    print("num is another number")

if(num > num2):
    num2 += 2
    if(num2 % 2 == 0):
        print('num2 is even')
    else:
        print('num2 is not even')
else:
    print('num is less than num2')

num2 += num * 5
if(num2 > 0):
    print('num2 is greater than 0')
else:
    print('num2 is less than 1')

if(num2 > 0 and num > 0):
    print('both numbers are greater than 0')
    num -= 99
else:
    print('both numbers are not greater than 0')

if(num < 0 or num2 < 0):
    print('one number is negative')
else:
    print('no numbers are negative')

if(num + num2 > 0):
    print('the sum of both numbers are postive')
    if(num > 0 or num2 > 0):
        num -= 99
        num2 -= 99
else:
    print('the sum of both numbers are negative')
    if(num < 0 or num2 < 0):
        num += 99
        num2 += 99
        print('the numbers are ' + str(num) + ' and ' + str(num2))
